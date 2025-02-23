from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mikel',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def read_gsheet():
    print("Reading Google Sheets...")

def clean_data():
    print("Cleaning data...")

def portfolio():
    print("Calculating portfolio...")

with DAG('devproject_dag', default_args=default_args, schedule=timedelta(days=1)) as dag:
    task1 = PythonOperator(
        task_id='read_gsheet',
        python_callable=read_gsheet,
    )

    task2 = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    task3 = PythonOperator(
        task_id='portfolio',
        python_callable=portfolio,
    )

    task1 >> task2 >> task3