
import requests
import sqlite3


response = requests.get('https://jsonplaceholder.typicode.com/comments')
data = response.json()


conn = sqlite3.connect('comments.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        postId INTEGER,
        name TEXT,
        email TEXT,
        body TEXT
    );
''')


for comment in data:
    cur.execute('''
        INSERT INTO comments (id, postId, name, email, body)
        VALUES (?, ?, ?, ?, ?);
    ''', (comment['id'], comment['postId'], comment['name'], comment['email'], comment['body']))

conn.commit()

