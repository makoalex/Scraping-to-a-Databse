from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.bookdepository.com/category/2638/History-Archaeology/browse/viewmode/all"
parser = BeautifulSoup(urlopen(url), 'html.parser')
titles = parser.find_all(class_='title')
for title in titles:
    book = title.find('a').next
    # print(book)
authors = parser.find_all('p', {'class': 'author'})
for a in authors:
    author = a.find('span')['itemscope']

date = parser.find_all('p', {'class': 'published'})
for d in date:
    publish_date = d.next
for p in parser.find_all('p', {'class': 'format'}):
    cover = p.get_text()
for i in parser.find_all('span', {'class': 'rrp'}):
    initial_price = i.get_text()
for s in parser.find_all('p', {'class': 'price-save'}):
    saved_sum = s.get_text()
data = parser.find_all(class_='star')
print(data)

