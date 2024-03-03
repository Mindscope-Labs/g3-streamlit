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
    page_icon='🌍')

st.title(":blue[G3] :green[Carbon Calculator] :orange[App]")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", 
                       [
                           "🇮🇳 India",
                           "🇰🇪 Kenya",
                           "🇺🇸 United States",
                           "🇨🇦 Canada",
                           "🇬🇧 United Kingdom"
                        ]
                       )

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily compute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")
    
    st.subheader("⚡ Monthly electricity consumption (in kwh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")
    
    
with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")
    
    st.subheader("🍲 Number of meals per day (in kwh)")
    meals = st.number_input("Meals", 0, key="meals_input")
   

# Normalize the inputs
if distance > 0:
    distance = distance * 365 # convert daily distance to yearly

if electricity > 0:
    electricity = electricity * 12 # convert monthly electricity to yearly

if waste > 0:
    waste = waste * 52 # convert weekly waste to yearly

if meals > 0:
    meals = meals * 365 # convert daily meals to yearly
       
# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]['Transportation'] * distance         
electricity_emissions = EMISSION_FACTORS[country]['Electricity'] * electricity          
waste_emissions = EMISSION_FACTORS[country]['Waste'] * waste 
meals_emissions = EMISSION_FACTORS[country]['Meals'] * meals  
   
# Convert emissions to tons of CO2. Round off to 2 decimal places
total_emissions = round(
    
)   
   
   
   