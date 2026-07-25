import os
import sys

sys.path.append(os.path.dirname(__file__))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

from etl_functions import (
    uploadtobronze,
    downloadfrombronze,
    clean_data,
    uploadtosilver,
    listfile,
    create_gold,
    upload_to_gold
)
default_args={
    "owner": "Jaya",
    "retries":3,
    "retry_delay":timedelta(minutes=2),
}
with DAG(
    dag_id="employee_etl_pipeline",
    start_date=datetime(2026, 7, 22),
    schedule="0 6 * * *",
    catchup=False,
    default_args=default_args
) as dag:

    task1 = PythonOperator(
        task_id="upload_to_bronze",
        python_callable=uploadtobronze,
    )

    task2 = PythonOperator(
        task_id="download_from_bronze",
        python_callable=downloadfrombronze,
    )

    task3 = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data,
    )

    task4 = PythonOperator(
        task_id="upload_to_silver",
        python_callable=uploadtosilver,
    )

    task5 = PythonOperator(
        task_id="list_files",
        python_callable=listfile,
    )
    task6=PythonOperator(
        task_id="creategold",
        python_callable=create_gold,
        )
    task7=PythonOperator(
        task_id="uploadtogold",
        python_callable=upload_to_gold,
        )

    task1 >> task2 >> task3 >> task4 >> task5 >> task6 >> task7
