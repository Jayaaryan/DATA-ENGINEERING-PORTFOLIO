import requests
import pandas as pd
import mysql.connector
import logging

response=requests.get("https://jsonplaceholder.typicode.com/users")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryan@2017"
)

logging.basicConfig(
    filename="etl1.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("LOADING DATA INTO PANDAS")
userdata=pd.DataFrame(response.json())

logging.info("DATA VALIDATION")
df=userdata[["id","name","email"]].copy()
df.drop_duplicates(inplace=True)

data = list(df.itertuples(index=False, name=None))
logging.info(f"{len(data)}rows prepared")

cursor=conn.cursor()

logging.info("USING DATABASE TO LOAD")

cursor.execute("USE company")

logging.info("TABLE CREATION")
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
ID INT PRIMARY KEY,
USERNAME VARCHAR(50),
EMAIL VARCHAR(40) )""")

logging.info("DATA INSERTION INTO MYSQL")
cursor.executemany("INSERT INTO users VALUES (%s,%s,%s)",data)

conn.commit()

cursor.execute("SELECT * FROM users")

rows=cursor.fetchall()

for row in rows:
    print(row)
logging.info("DATA UPLOADED AND COMPLETED")
df.to_csv("NEW USER.csv",index=False)
cursor.close()
conn.close()
