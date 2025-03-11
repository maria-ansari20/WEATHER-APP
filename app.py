import streamlit as st
import requests

# Function to get weather data from wttr.in
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    return response.text

# Streamlit UI
st.title("Weather App 🌞")

# Input city
city = st.text_input("Enter city name:")

if city:
    weather_data = get_weather(city)

    if weather_data:
        st.write(f"### Weather in {city.capitalize()}:")
        st.write(weather_data)
    else:
        st.write(f"### Weather data for {city} not found.")

