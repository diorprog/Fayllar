# import subprocess
#
# usb_path = "/dev/sdX"  # Usb manzili (X o'rniga qo'yilgan harfni qo'llang)
#
# try:
#     subprocess.run(["sudo", "umount", usb_path + "*"], check=True)
#     subprocess.run(["sudo", "mkfs.fat", "-F32", usb_path], check=True)
#     print("Usb muvaffaqiyatli formatlandi.")
# except subprocess.CalledProcessError as e:
#     print("Xatolik yuz berdi:", e)
#
#
#
#
# '''
# Terminalda:
# lsblk
# sudo su
# python format_usb.py
#
# '''




"""
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





#2
varchar() -- Matn ma'lumotlarini saqlaydi
Integer -- Butun sonlarni ifodalaydi
BIGINT -- kattaroq butun sonlar uchun ishlatiladi
char --- belgilar qatorlari
json --- json formatidagi ma'lumotlarini saqlaydi.
date --- sanani saqlaydi
time --- vaqtni saqlaydi


#3

--terminal

crontab -e

pg_dump -U $postgres $diyorbek > $BACKUP_DIR/db_backup_$timestamp.sql


--sql

create table car_detail (
    id serial primary key,
    car_id integer references car(id),
    detail text
);

insert into car_detail (car_id, detail) values
(1, 'Detail 1 for Car 1'),
(2, 'Detail 2 for Car 1'),
(1, 'Detail 1 for Car 2'),
(3, 'Detail 1 for Car 3'),
(4, 'Detail 1 for Car 4');


--ter

02***/bin/bash /path/to/backup.sh


#4


create or replace function filter_car_price(from_price numeric,to_price numeric)
returns table (id int, name varchar(255), brand varchar(255), price numeric)
as $$
begin
    return query
    select id, name, brand, price
    from car
    where price between from_price and to_price;
end;
$$ language plpgsql;


select * from filter_car_price(10000, 20000);


#5

---sql

CREATE OR REPLACE FUNCTION save_deleted_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO delete_users(id, fullname, username, password, join_at)
    VALUES(OLD.id, OLD.fullname, OLD.username, OLD.password, OLD.join_at);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER user_deleted_trigger
BEFORE DELETE ON users
FOR EACH ROW
EXECUTE FUNCTION save_deleted_user();


--py


import psycopg2
from psycopg2.extras import execute_values

def save_deleted_user(trigger_data):
    dbname = "diyorbek"
    user = "postgres"
    password = "1"
    host = 'localhost'
    port = 5432

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cur = conn.cursor()

    insert_query = 'INSERT INTO delete_users(id, fullname, username, password, join_at) VALUES %s;'
    execute_values(
        cur, insert_query, [trigger_data]
    )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    trigger_data = [(1, "John Doe", "johndoe", "password123", "2020-01-10")]
    save_deleted_user(trigger_data)

"""