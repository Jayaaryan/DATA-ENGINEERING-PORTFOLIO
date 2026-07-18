import boto3
import pandas as pd

s3=boto3.client("s3")

bucketname="jaya-data-engineering-2026"
localfile=r"C:\Users\jayaa\OneDrive\Desktop\employeeSMED.csv"
bronzekey="bronze/employeeSMED.csv"
downloadfile=r"C:\Users\jayaa\Downloads\employeeSMED.csv"
silverkey ="silver/employee_clean.csv"
outputfile=r"C:\Users\jayaa\Downloads\employee_clean.csv"


def uploadtobronze():
    print("UPLOAD TO BRONZE")
    s3.upload_file(localfile,bucketname,bronzekey)
    print("done success")

def downloadfrombronze():
    print("downlaod form bronze")
    s3.download_file(bucketname,bronzekey,downloadfile)
    print("download file")

def clean_data():
    print("data clean start")
    df=pd.read_csv(downloadfile)
    df=df.drop_duplicates()
    df=df.fillna("Unknown")
    df.to_csv(outputfile,index=False)
    print("OUTPUT GOT SUCCESSFULLY")

def uploadtosilver():
    s3.upload_file(outputfile,bucketname,silverkey)
    print("Uploaded to Silver")

def listfile():
    print("silver files:")
    response=s3.list_objects_v2(Bucket=bucketname,Prefix="silver/")

    if "Contents" in response:
        for obj in response["Contents"]:
            if obj["Size"] > 0:
                print(obj["Key"])

def main():
    uploadtobronze()
    downloadfrombronze()
    clean_data()
    uploadtosilver()
    listfile()

main()
