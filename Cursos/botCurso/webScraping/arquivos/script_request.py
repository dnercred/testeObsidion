import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.digitalocean.com/community/tutorials/como-fazer-scraping-em-paginas-web-com-beautiful-soup-and-python-3-pt")

if page.status_code == 200:
    soup = BeautifulSoup(page.text)

    for link in soup.find(class_= language-python):
        print(link.get("href", ""))
else:
    print("HTTP error ", page.status_code)


