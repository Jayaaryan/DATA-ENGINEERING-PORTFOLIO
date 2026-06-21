import requests
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import length,count,sum,min,max
spark=SparkSession.builder.getOrCreate()
response=requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()

pdf = pd.json_normalize(data)
df = spark.createDataFrame(pdf)

df.printSchema()
df = df.selectExpr("id","name","email","website","`address.city` as city","`company.name` as company")
df=df.fillna("Unknown")
df=df.withColumn("name_length",length("name"))
df=df.filter(df.name_length>10)
df.groupBy("city").agg(count("*").alias("Total_users")).show()
df.createOrReplaceTempView("user_view")
spark.sql("""select * from user_view""").show()
#df.write.mode("overwrite").saveAsTable("user_table")
spark.table("user_table").show()
