from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib.request

#start page
html = urlopen('https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker').read()
bs = BeautifulSoup(html, 'html.parser')

list_of_links = []
#Finds all link elm on the webpage
data = bs.findAll('a', href=True)

#iterating through all links
for i in data:
    link = str(i['href'])
    url = link.lower()

    #checking if the link starts with /wiki or # or //  to identify internal links
    if url.startswith(('/wiki')) or url.startswith('#') or url.startswith('/w') or url.startswith('//'):
        print('internal url')
        print("https://en.wikipedia.org/" + i['href'])
    #printing remaining links as external links
    else:
        print('external url')
        print(i['href'])




