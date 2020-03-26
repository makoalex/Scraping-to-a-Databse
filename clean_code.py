from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.bookdepository.com/category/2638/History-Archaeology/browse/viewmode/all"
parser = BeautifulSoup(urlopen(url), 'html.parser')


def get_title():
    for title in parser.find_all(class_='title'):
        book = title.find('a').next.strip()
        print(book)


def get_author():
    for a in parser.find_all('p', {'class': 'author'}):
        author = a.find('span')['itemscope']
        print(author)


def get_date():
    for d in parser.find_all('p', {'class': 'published'}):
        publish_date = d.next.strip()
        print(publish_date)


def get_cover():
    for c in parser.find_all('p', {'class': 'format'}):
        cover = c.get_text().strip()
        print(cover)


def get_price():
    for i in parser.find_all('span', {'class': 'rrp'}):
        initial_price = i.get_text()
        price = initial_price.replace('NOK', "")
        print(price + " "'NOK')


def get_discount():
    for s in parser.find_all('p', {'class': 'price-save'}):
        saved_sum = s.get_text().replace('Save', "").replace("NOK", "").strip()
        print(saved_sum + " " 'NOK')


functions = [get_title(), get_author(), get_date(), get_cover(), get_price(), get_discount()]
