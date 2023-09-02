import streamlit as st
import plotly.express as px


st.title("Weather Forecast for Upcoming Days")
place = st.text_input("Place: ")
forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Select number of days to forecast")
forecast_type = st.selectbox("Select Data To View", options=("Temperature", "Sky"))

st.subheader(f"{forecast_type} forecast for the next {forecast_days} in {place}")

dates = ["2022-25-10", "2022-26-10", "2022-27-10", "2022-28-10", "2022-29-10"]
temperatures = [55, 60, 57, 62, 65]

temperatures = temperatures[:forecast_days]
dates = dates[:forecast_days]

figure =px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (F)"})
st.plotly_chart(figure)