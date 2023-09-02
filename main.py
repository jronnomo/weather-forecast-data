import streamlit as st

st.title("Weather Forecast for Upcoming Days")
place = st.text_input("Place: ")
forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Select number of days to forecast")
forecast_type = st.selectbox("Select Data To View", options=("Temperature", "Sky"))

st.subheader(f"{forecast_type} forecast for the next {forecast_days} in {place}")