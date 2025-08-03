import requests
import pandas as pd
from datetime import datetime

def fetch_weather_data(city, api_key):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the weather data {response.text}")
    
    data = response.json()
    weather_info = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind_speed": data["wind"]["speed"],
        "cloud_cover": data["clouds"]["all"],
        "timestamp": datetime.utcnow()
    }

    df = pd.DataFrame([weather_info])
    return df

def transform_weather_data(df):
    df["city"] = df["city"].str.title()
    df.drop_duplicates(subset=["city", "timestamp"], inplace=True)
    return df
