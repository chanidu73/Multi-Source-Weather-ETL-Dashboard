# 🌦️ Multi-Source Weather ETL Dashboard

This project implements a complete end-to-end **ETL pipeline** that pulls real-time weather data from multiple sources, processes and loads it into a **Snowflake data warehouse**, and presents the data through a live monitoring **dashboard**. The data pipeline is orchestrated with **Apache Airflow**

---

## Features

-  **Weather Data Ingestion** from multiple cities via OpenWeatherMap API  
-  **Data Cleaning & Transformation** using Pandas  
-  **Snowflake Data Warehouse Integration**  
-  **ETL Scheduling & Monitoring** via Apache Airflow  
-  **Interactive Dashboard** for real-time visualization  
-  **Basic Error Handling** and logging throughout the pipeline

---

## 🧰 Tech Stack

| Component        | Technology        |
|------------------|-------------------|
| ETL Language     | Python (pandas, requests) |
| Workflow Engine  | Apache Airflow    |
| Data Storage     | Snowflake         |
| Dashboard        | FastAPI / Flask   |
| Dev Environment  | GitHub Codespaces |
| Data Source      | OpenWeatherMap API|

---

## 📁 Project Structure

multi_source_etl_dashboard/
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── snowflake_loader.py
│ └── run_weather_etl.py
│
├── dags/
│ └── weather_etl_dag.py 
│
├── dashboard/
│ └── app.py 
│
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com//chanidu73/Multi-Source-Weather-ETL-Dashboard.git
cd multi-source-etl-dashboard
### 2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
### 3. Configure Snowflake & API Keys
Set your Snowflake credentials and OpenWeatherMap API key in a .env or configuration file.

Example:

env
Copy
Edit
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=your_account
SNOWFLAKE_DATABASE=your_db
SNOWFLAKE_SCHEMA=your_schema
OPENWEATHER_API_KEY=your_api_key
### 4. Run the ETL Pipeline
bash
Copy
Edit
python etl/run_weather_etl.py
### 5. Start Airflow (Optional for Orchestration)
bash
Copy
Edit
airflow db migrate
airflow users create --username admin --role Admin --email admin@example.com --firstname Admin --lastname User --password admin
airflow webserver --port 8080
airflow scheduler
### 6. Start the Dashboard
bash
Copy
Edit
cd dashboard
uvicorn app:app --reload --port 8081
