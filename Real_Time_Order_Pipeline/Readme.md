# 🚀 Real-Time Order Processing Pipeline

A real-time data engineering project that streams order events from Apache Kafka into PySpark Structured Streaming for real-time processing.

---

## 📌 Project Overview

This project demonstrates how streaming data can be ingested from Apache Kafka and processed using Apache Spark Structured Streaming.

The application continuously listens to a Kafka topic (`orders`) and reads incoming messages in real time.

---

## 🏗️ Architecture

```
Producer
    │
    ▼
Apache Kafka (orders Topic)
    │
    ▼
PySpark Structured Streaming
    │
    ▼
Console Output
```

---

## 🛠️ Tech Stack

- Python
- Apache Kafka
- Apache Spark 4.x
- PySpark
- Java 17
- Windows

---

## 📂 Project Structure

```
Real_Time_Order_Pipeline/
│
├── producer.py              # Kafka Producer
├── streaming.py             # Spark Streaming Consumer
├── requirements.txt
├── README.md
└── screenshots/
```

---

## ⚙️ Features

- Real-time streaming using Apache Kafka
- Spark Structured Streaming integration
- Reads data continuously from Kafka topic
- Console output for monitoring streaming events
- Checkpoint support for fault tolerance

---

## 📥 Kafka Topic

```
Topic Name : orders
```

---

## ▶️ Running the Project

### Start Kafka

```bash
bin\windows\kafka-server-start.bat config\kraft\server.properties
```

### Create Topic

```bash
bin\windows\kafka-topics.bat --create ^
--topic orders ^
--bootstrap-server localhost:9092
```

### Run Spark Streaming

```bash
spark-submit ^
--packages org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2 ^
streaming.py
```

### Produce Messages

```bash
bin\windows\kafka-console-producer.bat ^
--bootstrap-server localhost:9092 ^
--topic orders
```

Example:

```
OrderID:101,Product:Laptop,Amount:75000
OrderID:102,Product:Mouse,Amount:800
```

---

## 📌 Sample Output

```
-------------------------------------------
Batch: 0
-------------------------------------------

OrderID:101,Product:Laptop,Amount:75000

OrderID:102,Product:Mouse,Amount:800
```

---

## 📄 Spark Streaming Code

The application:

- Creates a Spark Session
- Connects to Kafka
- Subscribes to the `orders` topic
- Reads messages continuously
- Casts Kafka values to String
- Prints the stream to the console

---

## 📸 Screenshots

Add screenshots here:

- Kafka Server Running
- Topic Creation
- Spark Streaming Running
- Console Output

---

## 🚧 Challenges Faced

- Configuring Kafka on Windows
- Setting up Hadoop `winutils.exe`
- Managing Spark-Kafka package dependencies
- Resolving Kafka broker connection issues

---

## 📈 Future Improvements

- Parse JSON orders
- Validate incoming records
- Write streaming data to MySQL
- Store processed data in Parquet
- Integrate with AWS S3
- Build dashboards using Power BI
- Deploy using Docker

---

## 🎯 Learning Outcomes

Through this project I learned:

- Apache Kafka Fundamentals
- Kafka Topics and Producers
- Spark Structured Streaming
- Real-Time Data Processing
- Spark-Kafka Integration
- Checkpointing
- Streaming Architecture
- Data Engineering Workflow

---

## 👨‍💻 Author

Developed as part of a Data Engineering learning journey focusing on real-time streaming using Apache Kafka and PySpark.