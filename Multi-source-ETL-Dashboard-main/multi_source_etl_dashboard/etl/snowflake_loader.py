import snowflake.connector

def load_to_snowflake(df, conn_params):
    conn = snowflake.connector.connect(**conn_params)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather_data (city, temperature, humidity, pressure, wind_speed, cloud_cover, timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row["city"],
            row["temperature"],
            row["humidity"],
            row["pressure"],
            row["wind_speed"],
            row["cloud_cover"],
            row["timestamp"].strftime("%Y-%m-%d %H:%M:%S")        ))

    conn.commit()
    cursor.close()
    conn.close()
