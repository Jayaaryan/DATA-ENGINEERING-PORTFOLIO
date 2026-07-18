# AWS S3 ETL Pipeline

## Project Overview

This project demonstrates an end-to-end ETL pipeline using Python, Pandas, AWS S3 and Boto3.

## Workflow

1. Upload raw CSV to S3 Bronze layer
2. Download file from Bronze
3. Read data using Pandas
4. Remove duplicate records
5. Handle missing values
6. Save cleaned CSV locally
7. Upload cleaned CSV to S3 Silver layer
8. List files available in the Silver layer

## Technologies Used

- Python
- Pandas
- AWS S3
- Boto3

## Architecture

Local CSV
↓
S3 Bronze
↓
Download
↓
Pandas Data Cleaning
↓
S3 Silver