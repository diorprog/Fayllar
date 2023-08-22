import requests
from bs4 import BeautifulSoup

response = requests.get("https://daryo.uz/yangiliklar")
html = response.content.decode()
soup=BeautifulSoup(html,"html.parser")


# print(soup("div",{"class":"mini__article"}))

for i in soup.find_all("div",{"class":"mini__article"})[:4]:
    title = i.h3.text
    photo_link=i.find("a",{"class":"blur-up lazyloaded"}).src