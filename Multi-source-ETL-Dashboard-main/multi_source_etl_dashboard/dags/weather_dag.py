from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from etl.run_weather_etl import run_weather_pipeline

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='weather_etl_pipeline',
    default_args=default_args,
    schedule_interval='@hourly',  
    catchup=False
) as dag:
    
    run_etl = PythonOperator(
        task_id='run_weather_etl',
        python_callable=run_weather_pipeline
    )

    