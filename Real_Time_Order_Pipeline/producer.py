from kafka import KafkaProducer
from faker import Faker
import json
import random
import time
from datetime import datetime

fake=Faker("en_IN")

producer=KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

products = ["Laptop","Mobile","Headphones","Keyboard","Mouse","Monitor",
            "Smart Watch"]

categories = ["Electronics","Accessories"]

payment_methods = ["UPI","Credit Card","Debit Card","Net Banking",
                   "Cash on Delivery"]

order_id=1001

for order_id in range(1001, 1011):
    order={
        "order_id":order_id,
        "customer":fake.name(),
        "city":fake.city(),
        "products":random.choice(products),
        "category":random.choice(categories),
        "quantity":random.randint(1,5),
        "price":random.randint(500,50000),
        "payment_method":random.choice(payment_methods),
        "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send("orders",order)
    producer.flush()
    print(f"Order Sent:{order}")
    order_id+=1
    time.sleep(1)
    
