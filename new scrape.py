from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen("https://www.bookdepository.com/category/2638/History-Archaeology/browse/viewmode/all")
parser = BeautifulSoup(url, 'html.parser')
books = parser.find_all(class_='item-info')
for book in books:
    print(book.find('a').next.strip())
    print(book.find('span')['itemscope'])
    print(book.find_next('p', {'itemprop': 'datePublished'}).next.strip())
    print(book.find_next('p', {'class': 'format'}).next.strip())
    print(book.find_next('span', {'class': 'rrp'}).next)
    print(book.find_next('p', {'class': 'price-save'}).next.strip())