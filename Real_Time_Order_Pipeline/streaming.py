from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("Real_Time_Order_Pipeline") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")


kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders") \
    .option("startingOffsets", "earliest") \
    .load()

print("Connected to Kafka Successfully!")


result = kafka_df.select(
    col("value").cast("string")
)


query = result.writeStream \
    .format("console") \
    .outputMode("append") \
    .option("checkpointLocation", "C:/tmp/spark_checkpoint") \
    .start()


query.awaitTermination()
