from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
from pyspark.sql.functions import avg,sum,min,max,row_number,rank,dense_rank
from pyspark.sql.window import Window

df=spark.table("workspace.default.employees")
df.printSchema()

window_spec=Window.partitionBy("department").orderBy(df.salary.desc())

df=df.fillna({'salary':0})
df=df.withColumn("bonus",df.salary+5000)
df=df.filter(df.salary>50000)
df.groupBy("department").agg(sum("salary").alias("total_salary"),avg("salary").alias("avg_salary")).show()
df.withColumn("ROWNUMBER",row_number().over(window_spec)).withColumn("RANK",rank().over(window_spec)).withColumn("DENSE_RANK",dense_rank().over(window_spec)).show()
df.write.mode("overwrite").saveAsTable("employees_clean")

spark.table("employees_clean").show()
spark.table("employees_clean").printSchema()
spark.sql("""select department,avg(salary) from employees_clean group by department""")
df.createOrReplaceTempView("employees_view")
spark.sql("""select * from employees_view """).show()

