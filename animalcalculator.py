import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="BIDMC Mouse Dose Calc", page_icon="🐭")

# 2. Title and Description
st.title("🐭 Mouse Dosing Calculator")
st.markdown("### Standardized Dosing for Metabolic Studies @ BIDMC")
st.info("Created by Sangeon Kim (PharmD Candidate)")

# 3. Sidebar Inputs
st.sidebar.header("Input Parameters")

weight_g = st.sidebar.number_input(
    "Mouse Weight (g)", 
    min_value=10.0, 
    max_value=60.0, 
    value=25.0, 
    step=0.1
)

dosage_mgkg = st.sidebar.number_input(
    "Target Dosage (mg/kg)", 
    min_value=0.1, 
    value=10.0, 
    step=0.1
)

concentration_mgml = st.sidebar.number_input(
    "Drug Concentration (mg/ml)", 
    min_value=0.01, 
    value=1.0, 
    step=0.1
)

# 4. Calculation Logic
if concentration_mgml > 0:
    # Weight conversion: g -> kg
    weight_kg = weight_g / 1000.0
    
    # Required drug amount (mg)
    required_drug_mg = weight_kg * dosage_mgkg
    
    # Injection volume (ml) = mg / (mg/ml)
    injection_volume_ml = required_drug_mg / concentration_mgml
    
    # Volume conversion: ml -> ul
    injection_volume_ul = injection_volume_ml * 1000.0
else:
    injection_volume_ml = 0
    injection_volume_ul = 0

# 5. Display Results
st.divider()
st.subheader("🧪 Calculation Result")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Injection Volume (μL)", value=f"{injection_volume_ul:.1f} μL")

with col2:
    st.metric(label="Injection Volume (mL)", value=f"{injection_volume_ml:.4f} mL")

# 6. Safety Warnings (PharmD Expertise)
st.divider()
if injection_volume_ul > 500:
    st.error(f"⚠️ WARNING: {injection_volume_ul:.1f} μL is too high for a standard mouse IP injection! Please check the concentration.")
elif injection_volume_ul < 10:
    st.warning(f"⚠️ NOTE: {injection_volume_ul:.1f} μL is very small. Ensure pipette accuracy.")
else:
    st.success("✅ Volume is within the safe range for IP injection.")

# Disclaimer
st.caption("Disclaimer: For Research Use Only. Not for clinical or diagnostic use.")