# API → Docker → Airflow → AWS S3 ETL Pipeline

## Project Overview

This project demonstrates an end-to-end automated ETL pipeline using **Apache Airflow**, **Docker**, **Python**, and **AWS S3**.

The pipeline extracts user data from a public REST API, stores the raw JSON data in an AWS S3 Bronze layer, downloads it locally, converts it into CSV format, performs data cleaning and transformation, and generates analytical reports.

The entire workflow is orchestrated using Apache Airflow running inside Docker containers.

---

## Architecture

```
Public API
     │
     ▼
Extract JSON
     │
     ▼
Docker + Airflow
     │
     ▼
AWS S3 (Bronze Layer)
     │
     ▼
Download JSON
     │
     ▼
Convert JSON → CSV
     │
     ▼
Clean & Transform Data
     │
     ▼
Generate Summary Reports
```

---

## Tech Stack

- Python
- Apache Airflow
- Docker
- Docker Compose
- AWS S3
- Boto3
- Pandas
- JSON
- CSV

---

## Project Workflow

### Task 1 – Upload to Bronze

- Fetch user data from REST API
- Store raw JSON locally
- Upload JSON file to AWS S3 Bronze Layer

### Task 2 – Download from Bronze

- Download JSON file from AWS S3
- Store locally for processing

### Task 3 – Convert to CSV

- Read JSON file
- Convert JSON into CSV using Pandas

### Task 4 – Data Cleaning

- Remove unnecessary columns
- Handle missing values
- Remove duplicates
- Save cleaned dataset

### Task 5 – Analytics

Generate reports such as:

- Department Summary
- API User Summary
- Employee Summary

---

## Airflow DAG

The Airflow DAG executes the tasks in the following order:

```
Upload to Bronze
        ↓
Download from Bronze
        ↓
Convert to CSV
        ↓
Clean Data
        ↓
Generate Reports
```

---

## Project Structure

```
API-DOCKER-AIRFLOW-AWS-PIPELINE
│
├── config/
├── dags/
│   ├── api_etl_dag.py
│   ├── api_functions.py
│   ├── api_config.py
│
├── data/
│
├── screenshots/
│
├── docker-compose.yaml
│
├── .env.example
│
├── .gitignore
│
└── README.md
```

---

## Features

- Automated ETL Pipeline
- Dockerized Airflow Environment
- AWS S3 Bronze Layer Storage
- Modular Python Functions
- Airflow Task Scheduling
- Data Cleaning using Pandas
- CSV Generation
- Summary Report Creation

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Apache Airflow DAG development
- Docker containerization
- AWS S3 integration using Boto3
- Building modular ETL pipelines
- Task orchestration
- Data transformation using Pandas
- Automating data workflows

---

## Future Enhancements

- Silver & Gold Data Layers
- Snowflake Integration
- Data Validation Checks
- Email Notifications
- Cloud Deployment
- Apache Spark Processing

---

## Screenshots

(Add Airflow DAG, successful task execution, AWS S3 bucket, and output files here.)

---

## Author

**Jaya Aryan**

Data Engineer | Python | SQL | PySpark | Airflow | Docker | AWS | Snowflake
