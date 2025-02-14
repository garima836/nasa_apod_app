import streamlit as st
import requests

# NASA API key
API_KEY = "pn3wqbnUItXfPvdyDl0vVwg8AdBOXyDhGugFJtla"

# Streamlit app title
st.title("NASA Astronomy Picture of the Day")

# Fetch APOD data from NASA API
def fetch_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    return response.json()

# Display APOD data
def display_apod(apod_data):
    st.header(apod_data["title"])
    st.image(apod_data["url"], caption=apod_data["title"], use_column_width=True)
    st.write(apod_data["explanation"])

# Main function
def main():
    apod_data = fetch_apod(API_KEY)
    display_apod(apod_data)

if __name__ == "__main__":
    main()
