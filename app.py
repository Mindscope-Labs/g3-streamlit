import streamlit as st

EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14, # kgCo2/km
        "Electricity": 0.82, # kgCO2/KwH
        "Diet": 1.25, # kgCO2/meal
        "Waste": 0.1, # kgCO2/kg
    }
}

st.set_page_config(
    layout="wide", 
    page_title="G3 Carbon Calculator",
    page_icon=':bar_chart:')

st.title(":blue[G3] :green[Carbon Calculator] :orange[App]")

# User inputs
st.subheader("Your Country")
country = st.selectbox("Select", 
                       [
                           "India",
                           "Kenya",
                           "United States",
                           "Canada",
                           " United Kingdom"
                        ]
                       )