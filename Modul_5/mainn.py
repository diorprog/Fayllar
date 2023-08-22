# 1

import psycopg2
from faker import Faker
import random

dbname = "diyorbek"
user = "postgres"
password = "1"
host = 'localhost'
port = 5432

fake = Faker()

brands = ['BMW', 'Mercedes', 'AUDI', 'FERRARI']

car_data = []

for _ in range(501):
    car_name = fake.word()
    brand = random.choice(brands)
    price = round(random.uniform(10000, 50000), 2)
    created_at = fake.date_time_this_year()

    car_data.append((car_name, brand, price, created_at))

conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
cur = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS car (
    id SERIAL PRIMARY KEY,
    name TEXT,
    brand TEXT,
    price NUMERIC,
    created_at TIMESTAMP
);
'''
cur.execute(create_table_query)

insert_query = 'INSERT INTO car (name, brand, price, created_at) VALUES (%s, %s, %s, %s);'

for (name, brand, price, created_at) in car_data:
    cur.execute(insert_query, (name, brand, price, created_at))

conn.commit()
cur.close()
conn.close()

print("Ma'lumotlar bazaga yozildi.")
