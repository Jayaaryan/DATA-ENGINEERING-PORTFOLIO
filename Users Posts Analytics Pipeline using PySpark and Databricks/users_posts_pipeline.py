import requests
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import count,rank
from pyspark.sql.window import Window

spark = SparkSession.builder.getOrCreate()

users_response = requests.get("https://jsonplaceholder.typicode.com/users")
posts_response = requests.get("https://jsonplaceholder.typicode.com/posts")
users = users_response.json()
posts = posts_response.json()

users_pdf=pd.json_normalize(users)
posts_pdf=pd.DataFrame(posts)
users_df=spark.createDataFrame(users_pdf)
posts_df=spark.createDataFrame(posts_pdf)

users_df.printSchema()
posts_df.printSchema()

users_df=users_df.selectExpr("id","name","`address.city` as city","`company.name`as company")
posts_df=posts_df.select("userId","id","title")

joined_df=posts_df.join(users_df,posts_df.userId==users_df.id,"inner").select(
    posts_df.id.alias("post_id"),
    posts_df.userId,
    posts_df.title,
    users_df.name,
    users_df.city,
    users_df.company
)
users_posts=joined_df.groupBy("name").agg(count("*").alias("TOTAL_POSTS"))
city_posts=joined_df.groupBy("city").agg(count("*").alias("TOTAL_POSTS"))

window_spec=Window.orderBy(users_posts.TOTAL_POSTS.desc())
ranked_df=users_posts.withColumn("rank",rank().over(window_spec))
ranked_df.show()

users_posts.createOrReplaceTempView("users_post_summary")
spark.sql("""SELECT * FROM users_post_summary ORDER BY TOTAL_POSTS DESC""").show()

ranked_df.write.mode("overwrite").saveAsTable("users_post_summary")
spark.table("users_post_summary").show()
