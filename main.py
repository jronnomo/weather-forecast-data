import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of days to forecast")
option = st.selectbox("Select Data To View", options=("Temperature", "Sky"))

try:
    if days == 1:
        st.subheader(f"{option} forecast for the next day in {place.title()}")
    else:
        st.subheader(f"{option} forecast for the next {days} days in {place.title()}")

    dates, values = get_data(kind=option, days=days, place=place)

    figure = px.line(x=dates, y=values, labels={"x": "Date", "y": "Temperature (F)"})
    st.plotly_chart(figure)
except KeyError:
    st.subheader("Please enter a location")
