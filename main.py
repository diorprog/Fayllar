import sqlite3


con = sqlite3.connect("D:\Python\product.sqlite")
cur = con.cursor()

n=input('Ma\'lumot o\'zgartirmoqchi bo\'lsangiz-0 ; Ma\'lumot qo|\'shsangiz-1 ; O\'chirmoqchi bo\'lsangiz-2 : ')
if n==1:
    id=int(input('ID: '))
    name=input('Nomi: ')
    price=int(input('Narxi: '))
    query = """insert into productes(id, name, price) values (?,?,?)"""
elif n==2:
    id=int(input('ID bo\'yicha qaysi birini o\'chirsin: '))
    query = """delete from productes where id=?"""
elif n==0:
    m = int(input('ID bo\'yicha qaysi birini nomini o\'zgartirsin: '))
    name=input('Nomi: ')
    query = """update productes set name = ? where id=1"""

cur.execute(query)
con.commit()