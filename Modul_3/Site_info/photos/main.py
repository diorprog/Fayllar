import requests
import sqlite3

response = requests.get('https://jsonplaceholder.typicode.com/photos')
data = response.json()

conn = sqlite3.connect('photos.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS photos (
                     id INTEGER PRIMARY KEY,
                     title TEXT,
                     url TEXT,
                     thumbnailUrl TEXT
                 )''')

for photo in data:
    cursor.execute('''INSERT INTO photos (id, title, url, thumbnailUrl)
                       VALUES (?, ?, ?, ?)''', (photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']))

conn.commit()
conn.close()


