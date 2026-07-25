import boto3
import pandas as pd
import logging
from config import *

logging.basicConfig(
    filename="etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("ETL Pipeline Started")
logging.info("ETL Pipeline Started")

s3 = boto3.client("s3")


def uploadtobronze():
    try:
        print("Uploading raw file to Bronze...")
        logging.info("UPLOADING RAW INTO AWS S3 BUCKET")

        s3.upload_file(localfile, bucketname, bronzekey)

        print("Upload completed successfully.")
        logging.info("UPLOADED SUCCESSFULLY")

    except Exception as e:
        print(f"UPLOAD FAILED: {e}")
        logging.error(f"UPLOAD FAILED: {e}")
        raise


def downloadfrombronze():
    try:
        print("Downloading file from Bronze...")
        logging.info("DOWNLOADING FROM AWS THE RAW FILE")

        s3.download_file(bucketname, bronzekey, downloadfile)

        print("Download completed successfully.")
        logging.info("THE FILE HAS BEEN DOWNLOADED")

    except Exception as e:
        print(f"DOWNLOAD FAILED: {e}")
        logging.error(f"DOWNLOAD FAILED: {e}")
        raise


def clean_data():
    try:
        print("Cleaning data...")
        logging.info("DATA CLEANING AND TRANSFORMING")

        df = pd.read_csv(downloadfile)

        df = df.drop_duplicates()

        # Fill only text columns
        df["department"] = df["department"].fillna("Unknown")
        df["name"] = df["name"].fillna("Unknown")

        # Convert salary to numeric
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

        # Replace missing salary with 0 (or drop them)
        df["salary"] = df["salary"].fillna(0)
        df.to_csv(outputfile, index=False)

        print("Data cleaned successfully.")
        logging.info("DATA CLEANED")

    except Exception as e:
        print(f"DATA CLEANING FAILED: {e}")
        logging.error(f"DATA CLEANING FAILED: {e}")
        raise


def uploadtosilver():
    try:
        print("Uploading cleaned file to Silver...")
        logging.info("UPLOADING TO AWS THE CLEANED FILE")

        s3.upload_file(outputfile, bucketname, silverkey)

        print("Silver upload completed.")
        logging.info("UPLOADED THE FILE")

    except Exception as e:
        print(f"UPLOAD TO SILVER FAILED: {e}")
        logging.error(f"UPLOAD TO SILVER FAILED: {e}")
        raise


def listfile():
    try:
        print("Listing Silver files...")
        logging.info("LISTING SILVER FILES")

        response = s3.list_objects_v2(
            Bucket=bucketname,
            Prefix="silver/"
        )

        if "Contents" in response:
            for obj in response["Contents"]:
                if obj["Size"] > 0:
                    print(obj["Key"])
                    logging.info(obj["Key"])

        print("Listing completed.")

    except Exception as e:
        print(f"LISTING FAILED: {e}")
        logging.error(f"LISTING FAILED: {e}")
        raise

def create_gold():
    try:
        print("GOLD LAYER CREATING")
        logging.info("CREATING A GOLD LAYER")
        df = pd.read_csv(outputfile)
        gold = (df.groupby("department")["salary"].mean().reset_index(name="Average_Salary"))
        gold.to_csv("/opt/airflow/data/department_summary.csv",index=False)
        logging.info("GOLD LAYER DONE")
        print("Gold Layer Created")
    except Exception as e:
        print(f"CREATION FAILED:{e}")
        logging.error(f"CREATE FAILED IN GOLD:{e}")
        raise

def upload_to_gold():
    try:
        print("Uploading cleaned file to Gold...")
        logging.info("UPLOADING TO AWS THE GOLD FILE")
        s3.upload_file("/opt/airflow/data/department_summary.csv",bucketname,"gold/department_summary.csv")
        print("gold upload completed.")
        logging.info("UPLOADED THE FILE")

    except Exception as e:
        print(f"UPLOAD TO GOLD FAILED: {e}")
        logging.error(f"UPLOAD TO GOLD FAILED: {e}")
        raise
