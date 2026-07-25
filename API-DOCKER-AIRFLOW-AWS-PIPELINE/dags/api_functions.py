import requests
import boto3
import pandas as pd
import logging

from api_config import *
logging.basicConfig(filename="api_pipeline.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

print("API ETL Started")
logging.info("API ETL Started")
s3 = boto3.client("s3")

def extract_api():
    try:
        print("Extraction data from api...")
        logging.info("EXTRACTING DATA FROM API")

        response=requests.get(api_url)
        response.raise_for_status()
        data=response.json()
        df=pd.DataFrame(data)
        df.to_json(api_json,orient="records",indent=4)

        print("API Data saved as json")
        logging.info("API DATS EXTRACTED AS JSON")
    except Exception as e:
        print(f"EXTRACTION FAILED: {e}")
        logging.error(f"EXTRACTION FAILED: {e}")
        raise

def upload_to_bronze():
    try:
        print("Uploading json to bronze aws")
        logging.info("UPLOADING JSON TO BRONZE")

        s3.upload_file(api_json,bucketname,bronzekey)

        print("upload successfully")
        logging.info("UPLOADED SUCCESSFULLY")
    except Exception as e:
        print(f"UPLOAD FAILED:{e}")
        logging.error(f"UPLOAD FAILED :{e}")
        raise

def  download_from_bronze():
    try:
        print("DOWNLAOD FROM AWS")
        logging.info("DOWNLOAD FROM AWS TO LOCAL")

        s3.download_file(bucketname,bronzekey,api_download)

        print("DOWNLOAD SUCCESS")
        logging.info("DOWNLOADING DONE")
    except Exception as e:
        print(f"DOWNLOAD FAILED:{e}")
        logging.error(f"DOWNLOADING FAILED:{e}")
        raise

def convert_to_csv():
    try:
        print("CONVERT TO CSV")
        logging.info("CONVERTING TO CSV")

        df=pd.read_json(api_download)
        df.to_csv(api_csv,index=False)

        print("JSON CONVERTED TO CSV")
        logging.info("JSON TO CSV DONE")
    except Exception as e:
        print(f"CONVERSION FAILED:{e}")
        logging.error(f"CONVERTING JSON TO CSV FAILED:{e}")
        raise

def clean_data():
    try:
        print("CLEANING STARTED")
        logging.info("DATA TRANSFORMATION STARTED")

        df=pd.read_csv(api_csv)
        df=df.drop_duplicates()
        df=df.fillna("Unknown")
        df=df[["id","name","username","email","phone","website"]]
        df.to_csv(api_clean,index=False)

        print("Data Cleaned Successfully")
        logging.info("DATA CLEANED")

    except Exception as e:
        print(f"CLEANING FAILED: {e}")
        logging.error(f"CLEANING FAILED: {e}")
        raise

def upload_to_silver():
    try:
        print("Uploading csv to silver aws")
        logging.info("UPLOADING CSV TO SILVER")

        s3.upload_file(api_clean,bucketname,silverkey)

        print("upload successfully")
        logging.info("UPLOADED SUCCESSFULLY")
    except Exception as e:
        print(f"UPLOAD FAILED:{e}")
        logging.error(f"UPLOAD FAILED :{e}")
        raise

def create_gold():
    try:
        print("CREATING GOLD LAYER")
        logging.info("CREATING GOLD LAYER")

        df=pd.read_csv(api_clean)

        df=df.groupby("website").size().reset_index(name="Total_Users")
        df.to_csv(api_gold,index=False)

        print("GOLD CREATED")
        logging.info("GOLD CREATED SUCCESSFULLY")

    except Exception as e:
        print(f"GOLD CREATION FAILED: {e}")
        logging.error(f"GOLD CREATION FAILED: {e}")
        raise

def upload_to_gold():
    try:
        print("UPLOADING GOLD TO AWS")
        logging.info("UPLOADING GOLD TO AWS")

        s3.upload_file(api_gold,bucketname,goldkey)

        print("GOLD UPLOADED SUCCESSFULLY")
        logging.info("GOLD UPLOADED SUCCESSFULLY")

    except Exception as e:
        print(f"GOLD UPLOAD FAILED: {e}")
        logging.error(f"GOLD UPLOAD FAILED: {e}")
        raise
