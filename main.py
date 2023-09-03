import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of days to forecast")
option = st.selectbox("Select Data To View", options=("Temperature", "Sky"))

if place:
    try:
        if days == 1:
            st.subheader(f"{option} forecast for the next day in {place.title()}")
        else:
            st.subheader(f"{option} forecast for the next {days} days in {place.title()}")

        dates, values = get_data(kind=option, days=days, place=place)

        if option == "Temperature":
            figure = px.line(x=dates, y=values, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        else:
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            with col1:
                for item in range(0, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])

            with col2:
                for item in range(1, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])

            with col3:
                for item in range(2, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])

            with col4:
                for item in range(3, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])

            with col5:
                for item in range(4, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])

            with col6:
                for item in range(5, len(values), 6):
                    st.image(values[item])
                    st.write(dates[item])
    except KeyError:
        st.subheader("Please enter a valid location")

else:
    st.subheader("Please enter a location")
