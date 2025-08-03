from weather_etl import fetch_weather_data, transform_weather_data
from snowflake_loader import load_to_snowflake
import json 
def run_weather_pipeline():
    cities = ['colombo', 'London' , 'New York' , 'Tokyo']
    with open("config/secrets.json") as f:
        config = json.load(f)
    api_key = config["api_key"]
    conn_params = {
        "user": config["user"],
        "password": config["password"],
        "account": config["account"],
        "warehouse": config["warehouse"],
        "database": config["database"],
        "schema": config["schema"]
    }
    for city in cities:
        df = fetch_weather_data(city , api_key)
        df = transform_weather_data(df)
        load_to_snowflake(df ,conn_params)

if __name__ == "__main__":
    run_weather_pipeline()