# Users Posts Analytics Pipeline using PySpark and Databricks

## Project Overview

This project demonstrates an end-to-end ETL and analytics pipeline using PySpark in Databricks.

Data is extracted from two public REST APIs containing user and post information. The datasets are transformed, joined, analyzed, ranked using window functions, and finally stored as a Databricks managed table.

The project simulates a real-world analytics workflow where data from multiple sources is combined to generate business insights.

---

## Technologies Used

* Python
* Requests
* Pandas
* PySpark
* Spark SQL
* Databricks

---

## Data Sources

### Users API

https://jsonplaceholder.typicode.com/users

Contains user information including:

* User ID
* Name
* Address
* Company Details

### Posts API

https://jsonplaceholder.typicode.com/posts

Contains:

* Post ID
* User ID
* Post Title
* Post Content

---

## Project Architecture

Users API
↓
Posts API
↓
JSON Extraction
↓
Pandas DataFrames
↓
Spark DataFrames
↓
Data Transformation
↓
Join Operation
↓
Aggregation
↓
Window Function Ranking
↓
Spark SQL Analysis
↓
Databricks Managed Table

---

## ETL Workflow

### Extract

* Retrieved user data from the Users API.
* Retrieved post data from the Posts API.
* Converted JSON responses into Pandas DataFrames.
* Converted Pandas DataFrames into Spark DataFrames.

### Transform

Selected and renamed relevant columns:

Users Dataset:

* id
* name
* city
* company

Posts Dataset:

* userId
* id
* title

Flattened nested JSON fields:

* address.city
* company.name

### Join

Joined Users and Posts datasets using:

User ID = Post User ID

This created a consolidated dataset containing:

* Post ID
* User ID
* Post Title
* User Name
* City
* Company

### Aggregation

Calculated:

* Total posts created by each user
* Total posts by city

Using:

groupBy()
count()

### Window Function

Applied ranking using:

rank()

to rank users based on total posts created.

### Spark SQL

Created a temporary view:

users_post_summary

Executed SQL queries for analytical reporting.

### Load

Stored the final ranked dataset in a Databricks managed table:

users_post_summary

---

## Output Dataset

| Column      | Description                   |
| ----------- | ----------------------------- |
| name        | User Name                     |
| TOTAL_POSTS | Number of Posts Created       |
| rank        | User Rank Based on Post Count |

---

## Key PySpark Concepts Used

* createDataFrame()
* select()
* selectExpr()
* join()
* groupBy()
* agg()
* count()
* Window Functions
* rank()
* createOrReplaceTempView()
* spark.sql()
* saveAsTable()

---

## Sample Business Questions Answered

* How many posts has each user created?
* Which users are the most active contributors?
* How are posts distributed across cities?
* How can multiple APIs be combined for analytics?

---

## Skills Demonstrated

* REST API Integration
* JSON Processing
* Data Transformation
* Data Joining
* Aggregation and Analytics
* Window Functions
* Spark SQL
* Databricks Table Management
* End-to-End ETL Development

---

## Project Outcome

Successfully built a multi-source analytics pipeline that:

* Extracts data from APIs
* Processes data using PySpark
* Combines datasets through joins
* Performs aggregations and ranking
* Stores analytical results in Databricks

This project demonstrates practical Data Engineering concepts commonly used in real-world ETL and analytics workflows.
