import streamlit as st
import pandas as pd
import snowflake.connector
import json

with open("config/secrets.json") as f:
    conn_params = json.load(f)


conn = snowflake.connector.connect(**conn_params)
query = "SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 100"
df = pd.read_sql(query, conn)
conn.close()


st.title("🌦️ Weather Data Dashboard")

cities = df["CITY"].unique()
selected_city = st.selectbox("Select City", cities)

city_data = df[df["CITY"] == selected_city]

st.line_chart(city_data.set_index("TIMESTAMP")[["TEMPERATURE", "HUMIDITY"]])
st.bar_chart(city_data.set_index("TIMESTAMP")[["PRESSURE", "WIND_SPEED"]])