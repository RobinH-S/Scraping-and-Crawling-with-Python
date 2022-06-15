"""
-Start crawling from https://en.wikipedia.org/wiki/Web_scraping
-Using BeautifulSoup's find_all() function getall the links from 'See also' section
-for each link do the following
-Loads selected article page
- Print out selected articles first paragraph.
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup



html = urlopen('https://en.wikipedia.org/wiki/Web_scraping').read()
bs = BeautifulSoup(html, 'html.parser')


text = urlopen('https://en.wikipedia.org/wiki/Web_scraping').read()


#Finds and shows see all seksjonen
data = bs.findAll('div',attrs={'class':'div-col'})
for div in data:
    links = div.findAll('a'

    #iterating through all links found
    for a in links:
        print ("https://en.wikipedia.org/" + a['href'])
        url = "https://en.wikipedia.org" + a['href']
        html = urlopen(url).read()
        bs = BeautifulSoup(html, 'html.parser')

        #Goes through all the webpages and prints the first paragraph
        for item in bs.select("#mw-content-text"):
            required_data = [p_item.text.strip() for p_item in item.select("p")][1:4]
            print('\n'.join(required_data))





