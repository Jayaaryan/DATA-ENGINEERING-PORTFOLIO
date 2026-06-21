# API to MySQL ETL Pipeline

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python.

The pipeline extracts user data from a public REST API, performs basic data validation and cleaning using Pandas, and loads the transformed data into a MySQL database.

---

## Technologies Used

* Python
* Requests
* Pandas
* MySQL
* MySQL Connector
* Logging

---

## Workflow

### Extract

Data is extracted from the public API:

https://jsonplaceholder.typicode.com/users

### Transform

The following transformations are performed:

* Convert JSON response to a Pandas DataFrame
* Select required columns:

  * id
  * name
  * email
* Remove duplicate records
* Prepare data for database insertion

### Load

* Connect to MySQL database
* Create the users table if it does not exist
* Insert cleaned records into MySQL
* Verify data insertion
* Export cleaned data to a CSV file

---

## Database Schema

| Column   | Data Type   |
| -------- | ----------- |
| ID       | INT         |
| USERNAME | VARCHAR(50) |
| EMAIL    | VARCHAR(40) |

---

## Logging

The pipeline uses Python logging to track:

* Data extraction
* Data validation
* Table creation
* Data insertion
* Pipeline completion

Logs are stored in:

etl1.log

---

## Output

### MySQL Table

Cleaned user records are loaded into the MySQL users table.

### CSV File

A cleaned CSV file is generated:

NEW USER.csv

---

## Skills Demonstrated

* API Integration
* ETL Development
* Data Validation
* Pandas Data Processing
* MySQL Database Operations
* Logging and Monitoring
* Python Automation

---

## Future Enhancements

* Exception Handling
* Environment Variables for Credentials
* Incremental Data Loading
* Automated Scheduling with Airflow
* Cloud Storage Integration
