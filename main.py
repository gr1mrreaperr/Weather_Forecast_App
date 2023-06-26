import streamlit as st
import plotly.express as px
from backend import get_data


st.set_page_config(layout="wide")
st.title("Weather Forecast App")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")

option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# Get the Temperature or Sky Data
if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [i["main"]["temp"] for i in filtered_data]
        dates = [i["dt_txt"] for i in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature(Celsius)"}, markers=True)
        st.plotly_chart(figure)
    elif option == 'Sky':
        sky_data = [i["weather"][0]["main"] for i in filtered_data]
        image_dict = {"Clear": "images\\clear.png",
                      "Clouds": "images\\cloud.png",
                      "Rain": "images\\rain.png",
                      "Snow": "images\\snow.png"}
        image_paths = [image_dict[condition] for condition in sky_data]
        st.image(image_paths, width=115)


