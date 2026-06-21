import pandas as pd
import mysql.connector
import logging


logging.basicConfig(
    filename="etl.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s -%(message)s"
)

logging.info("ESTABLISHING CONNECTION TO MYSQL:")
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryan@2017"
)

cursor=conn.cursor()
logging.info("CONNECTING TO DB")
cursor.execute("USE company")

cursor.execute("DROP TABLE IF EXISTS employeesnew")

logging.info("CREATING TABLE FOR INSERTION")
cursor.execute("""
CREATE TABLE IF NOT EXISTS employeesnew (
id INT PRIMARY KEY,
name VARCHAR(50),
department VARCHAR(50),
salary INT )
""")

df=pd.read_csv(r"F:\python\basics\DE\EXAMPLE PROJECTS\CSV TO MYSQL\employee.csv")
logging.info("CSV LOADED")

logging.info("DATA VALIDATION")
df["department"] = df["department"].fillna("Unknown")
df["salary"] = df["salary"].fillna(0)
df = df.drop_duplicates(subset=["name","department","salary"])

data=list(df.itertuples(index=False,name=None))

logging.info("INSERTING DATA INTO SQL")
cursor.executemany("INSERT INTO employeesnew VALUES (%s,%s,%s,%s)",data)
conn.commit()

logging.info(f"{cursor.rowcount} rows inserted")

cursor.execute("SELECT * FROM employeesnew")

for row in cursor.fetchall():
    print(row)
df.to_csv("EmployeeUpdate.csv",index=False)
cursor.close()
conn.close()

