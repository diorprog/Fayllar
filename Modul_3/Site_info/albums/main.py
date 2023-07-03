
import sqlite3
import json
import requests


conn = sqlite3.connect("albums.db")
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS albums (
                id INTEGER PRIMARY KEY,
                userId INTEGER,
                title TEXT
            )""")


response = requests.get("https://jsonplaceholder.typicode.com/albums")
data = json.loads(response.text)

for album in data:
    album_id = album["id"]
    user_id = album["userId"]
    title = album["title"]

    c.execute("INSERT INTO albums (id, userId, title) VALUES (?, ?, ?)", (album_id, user_id, title))


conn.commit()
conn.close()

