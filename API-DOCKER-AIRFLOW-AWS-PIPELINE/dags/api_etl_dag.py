from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime,timedelta

from api_functions import(extract_api,
                          upload_to_bronze,
                          download_from_bronze,
                          convert_to_csv,
                          clean_data,
                          upload_to_silver,
                          create_gold,
                          upload_to_gold)

default_args={
    "owner":"Jaya",
              "retries":2,
              "retry_delay":timedelta(minutes=2)
              }

with DAG(
    dag_id="api_etl_pipeline",
    start_date=datetime(2026, 7, 23),
    schedule="*/5 * * * *",
    catchup=False,
    default_args=default_args) as dag:

    extract = PythonOperator(
        task_id="extract_api",
        python_callable=extract_api
    )

    bronze = PythonOperator(
        task_id="upload_to_bronze",
        python_callable=upload_to_bronze
    )

    download = PythonOperator(
        task_id="download_from_bronze",
        python_callable=download_from_bronze
    )

    convert = PythonOperator(
        task_id="convert_to_csv",
        python_callable=convert_to_csv
    )

    clean = PythonOperator(
        task_id="clean_data",
        python_callable=clean_data
    )

    silver = PythonOperator(
        task_id="upload_to_silver",
        python_callable=upload_to_silver
    )

    gold = PythonOperator(
        task_id="create_gold",
        python_callable=create_gold
    )

    upload_gold = PythonOperator(
        task_id="upload_gold",
        python_callable=upload_to_gold
    )

    extract >> bronze >> download >> convert >> clean >> silver >> gold >> upload_gold
