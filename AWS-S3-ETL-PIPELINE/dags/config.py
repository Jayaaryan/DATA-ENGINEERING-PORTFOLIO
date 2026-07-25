from airflow.models import Variable

bucketname = Variable.get("bucket_name")
bronzekey = Variable.get("bronze_key")
silverkey = Variable.get("silver_key")

localfile = "/opt/airflow/data/employeeSMED.csv"

downloadfile = "/opt/airflow/data/employeeSMED.csv"

outputfile = "/opt/airflow/data/employee_clean.csv"
