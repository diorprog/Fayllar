
import requests
import sqlite3


response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()


conn = sqlite3.connect('posts.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS posts
                (id INTEGER PRIMARY KEY,
                title TEXT,
                body TEXT,
                userId INTEGER)''')


for item in data:
    cursor.execute("INSERT INTO posts (id, title, body, userId) VALUES (?, ?, ?, ?)",
                   (item['id'], item['title'], item['body'], item['userId']))
conn.commit()


conn.close()

