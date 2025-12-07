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
    step=