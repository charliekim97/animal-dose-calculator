import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. Configuration & Constants
# ---------------------------------------------------------
st.set_page_config(page_title="BIDMC Metabolic Dose Calc", page_icon="🧬", layout="wide")

# HED (Human Equivalent Dose) Scaling Factors (FDA Guidelines)
KM = {
    "human": 37,
    "mouse": 3,
    "rat": 6,
}

# Drug Database (Metabolic Agents)
DRUG_DB = {
    "insulin_glargine": {
        "label": "Insulin Glargine (Basal)",
        "class": "Insulin",
        "unit": "U/kg",
        "typical_human_dose_per_kg": 0.2, # Conservative start
    },
    "insulin_lispro": {
        "label": "Insulin Lispro (Prandial)",
        "class": "Insulin",
        "unit": "U/kg",
        "typical_human_dose_per_kg": 0.1,
    },
    "pioglitazone": {
        "label": "Pioglitazone (TZD)",
        "class": "Small Molecule",
        "unit": "mg/kg",
        "typical_human_dose_mg_per_day": 30.0,
        "typical_human_weight_kg": 70.0,
    },
    "dapagliflozin": {
        "label": "Dapagliflozin (SGLT2i)",
        "class": "Small Molecule",
        "unit": "mg/kg",
        "typical_human_dose_mg_per_day": 10.0,
        "typical_human_weight_kg": 70.0,
    },
    "metformin": {
        "label": "Metformin",
        "class": "Biguanide",
        "unit": "mg/kg",
        "typical_human_dose_mg_per_day": 1000.0,
        "typical_human_weight_kg": 70.0,
    },
     "custom": {
        "label": "Custom (Manual Input)",
        "class": "Experimental",
        "unit": "mg/kg",
        "typical_human_dose_mg_per_day": 0.0,
        "typical_human_weight_kg": 70.0,
    }
}

# ---------------------------------------------------------
# 2. Helper Functions
# ---------------------------------------------------------

def calc_human_mg_per_kg_from_daily(dose_mg_per_day: float, weight_kg: float) -> float:
    return dose_mg_per_day / weight_kg

def hed_scale_mg_per_kg(human_mg_per_kg: float, species: str) -> float:
    """Calculate Human Equivalent Dose based on BSA (Km factors)"""
    km_h = KM["human"]
    km_a = KM[species]
    return human_mg_per_kg * (km_h / km_a)

def per_animal_mass(dose_per_kg: float, animal_weight_g: float) -> float:
    return dose_per_kg * (animal_weight_g / 1000.0)

def volume_from_stock(amount: float, stock_conc_per_ml: float) -> float:
    if stock_conc_per_ml == 0: return 0
    vol_ml = amount / stock_conc_per_ml
    return vol_ml * 1000.0 # Convert to uL

def calc_dose_levels(base: float):
    return {
        "Low (0.5x)": 0.5 * base,
        "Mid (1x)": base,
        "High (2x)": 2.0 * base,
    }

# ---------------------------------------------------------
# 3. Main Application Logic
# ---------------------------------------------------------
def main():
    # Header
    st.title("🧬 Metabolic Dose Calculator")
    st.markdown("""
    **Translational Dosing Tool (Human → Rodent)** based on FDA Body Surface Area (BSA) normalization.
    *Designed for BIDMC Metabolic Research Labs.*
    """)
    
    col_l, col_r = st.columns([1, 2])

    # --- Sidebar / Left Panel ---
    with col_l:
        st.subheader("1. Settings")
        
        # Drug Selection
        drug_key = st.selectbox(
            "Select Drug / Agent",
            options=list(DRUG_DB.keys()),
            format_func=lambda k: DRUG_DB[k]["label"],
        )
        
        # Species & Weight
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            species = st.selectbox("Species", ["mouse", "rat"])
        with col_s2:
            animal_weight_g = st.number_input(
                "Animal Weight (g)", min_value=10.0, max_value=500.0, value=25.0, step=1.0
            )
            
        # Stock Concentration
        stock_conc = st.number_input(
            "Stock Concentration (mg/mL or U/mL)",
            min_value=0.01, max_value=5000.0, value=10.0, step=1.0,
            help="Concentration of your prepared solution."
        )

        st.info(f"**Selected:** {DRUG_DB[drug_key]['label']} ({species})")

    # --- Main Panel ---
    with col_r:
        info = DRUG_DB[drug_key]
        unit = info["unit"]
        
        st.subheader("2. Human-to-Animal Conversion")
        
        # Logic for mg/kg (Small Molecules)
        if unit == "mg/kg" and drug_key != "custom":
            use_typical = st.checkbox("Use Typical Human Clinical Dose?", value=True)
            
            if use_typical:
                human_dose_mg_day = info["typical_human_dose_mg_per_day"]
                human_weight_kg = info["typical_human_weight_kg"]
                st.caption(f"Based on clinical dose: **{human_dose_mg_day} mg/day** for a **{human_weight_kg} kg** human.")
            else:
                c1, c2 = st.columns(2)
                with c1: human_dose_mg_day = st.number_input("Human Dose (mg/day)", value=30.0)
                with c2: human_weight_kg = st.number_input("Human Weight (kg)", value=70.0)

            human_mgkg = calc_human_mg_per_kg_from_daily(human_dose_mg_day, human_weight_kg)
            
            # HED Calculation
            animal_mgkg_mid = hed_scale_mg_per_kg(human_mgkg, species)
            dose_levels = calc_dose_levels(animal_mgkg_mid)
            
            st.success(f"Human Eq. Dose: **{human_mgkg:.2f} mg/kg** ➡️ {species.capitalize()} Eq. Dose (BSA Scaled): **{animal_mgkg_mid:.2f} mg/kg**")

        # Logic for U/kg (Insulin) - HED scaling usually not applied directly, but 1:1 or adjusted
        elif unit == "U/kg":
            use_typical = st.checkbox("Use Typical Human Basal/Prandial Dose?", value=True)
            if use_typical:
                human_ukg = info["typical_human_dose_per_kg"]
            else:
                human_ukg = st.number_input("Target Human Dose (U/kg)", value=0.5)
            
            st.markdown(f"**Human Dose:** {human_ukg:.2f} U/kg")
            
            # Insulin scaling is tricky. Usually rodents need higher doses due to metabolism.
            # Offering a multiplier option.
            scaling_factor = st.slider(f"Scaling Factor (Human -> {species})", 1.0, 10.0, 1.0, 0.5, help="Rodents often require higher U/kg than humans due to faster clearance.")
            
            animal_ukg_mid = human_ukg * scaling_factor
            dose_levels = calc_dose_levels(animal_ukg_mid)
            
            st.success(f"Target {species.capitalize()} Dose: **{animal_ukg_mid:.2f} U/kg** (Factor x{scaling_factor})")
            
        else: # Custom
            animal_mgkg_mid = st.number_input(f"Target {species} Dose ({unit})", value=10.0)
            dose_levels = calc_dose_levels(animal_mgkg_mid)

        # ---------------------------------------------------------
        # 3. Final Table Generation
        # ---------------------------------------------------------
        st.subheader("3. Final Dosing Table")
        
        rows = []
        warning_flag = False
        
        for label, perkg in dose_levels.items():
            amount = per_animal_mass(perkg, animal_weight_g)
            vol_ul = volume_from_stock(amount, stock_conc)
            
            # Safety Check
            status = "✅"
            if vol_ul > 500:
                status = "⚠️ High Vol"
                warning_flag = True
            elif vol_ul < 10:
                status = "⚠️ Low Vol"
            
            rows.append({
                "Dose Level": label,
                f"Target ({unit})": f"{perkg:.2f}",
                "Amount / Animal": f"{amount:.3f}",
                "Inj. Vol (µL)": f"{vol_ul:.1f}",
                "Check": status
            })
            
        st.table(rows)
        
        if warning_flag:
            st.error("⚠️ WARNING: Some injection volumes exceed 500 µL. Consider increasing stock concentration.")

        # Disclaimer
        st.divider()
        st.caption("Developed by **Sangeon Kim (PharmD Candidate)** for internal research use only.")
        st.caption("Calculation Reference: *FDA Guidance for Industry: Estimating the Maximum Safe Starting Dose in Initial Clinical Trials for Therapeutics in Adult Healthy Volunteers (2005)*")

if __name__ == "__main__":
    main()