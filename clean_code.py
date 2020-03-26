from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.bookdepository.com/category/2638/History-Archaeology/browse/viewmode/all"

all_data= []
def get_scrape(url):
    global all_data
    parser = BeautifulSoup(urlopen(url), 'html.parser')
    books = parser.find_all(class_='item-info')
    all_data = []
    for book in books:
        data = (get_title(book), get_author(book), get_date(book), get_cover(book), get_price(book), get_discount(book))
        all_data.append(data)
    print(all_data)


def get_title(book):
    return book.find('a').next.strip()


def get_author(book):
    return book.find('span')['itemscope']


def get_date(book):
    return book.find_next('p', {'itemprop': 'datePublished'}).next.strip()


def get_cover(book):
    return book.find_next('p', {'class': 'format'}).next.strip()


def get_price(book):
    price = book.find_next('span', {'class': 'rrp'}).next
    new_price = price.replace('NOK', "")
    return new_price + " "'NOK'


def get_discount(book):
    save = book.find_next('p', {'class': 'price-save'}).next.strip()
    saved_sum = save.replace('Save', "").replace("NOK", "").strip()
    return saved_sum + " " 'NOK'

get_scrape("https://www.bookdepository.com/category/2638/History-Archaeology/browse/viewmode/all")
