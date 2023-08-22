import requests
from bs4 import BeautifulSoup

response = requests.get("https://kundalik.com")
html = response.content.decode()
soup=BeautifulSoup(html,"html.parser")
# print(soup.prettify())

# for i in soup.find_all("li",{"class":"menu__layout_unit"}):
#     print(i.a["href"])


for i in soup("li",{"class":"menu__layout_unit"}):
    with open(i.a["href"].split("/")[-1],'w') as f:
        f.write()
    for _ in i:
        response=requests.get(i)
