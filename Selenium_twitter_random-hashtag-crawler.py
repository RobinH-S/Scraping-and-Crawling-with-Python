from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


# Access to Twitter
#intitial url
start_url = r'https://twitter.com/search?q=%23Scraping'

#html.startswith('hashtag')
#hashtags.append(html)
visited = []

def sel_scrape(start_url, visited):
    #lokal path til chromedriver
    driver = webdriver.Chrome('D:\INFOVIT UIB\VÅR 2022\INFO 215 - Web Science\Oppgaver og Innleveringer\Oblig3\chromedriver')
    #maks antall sider som skal besøkes
    max_visited = 6
    #Sider som er besøkt
    #legger til start_url til i listen over besøkte sider
    visited.append(start_url)
    #En liste over hashtags på den besøkte siden
    hash_Tag = []

    #Går til den ny siden
    driver.get(start_url)
    # venter 10 sekunder til siden har lastet
    driver.implicitly_wait(10)
    #legger til de første 100 linkene fra hashtagene i liste, for å så velge en tileldig link senere
    elems = driver.find_elements(By.XPATH,'//span[@class = "r-18u37iz"]/a[@href]')
    for elem in elems:
        hash_Tag.append(elem.get_attribute("href"))

    #print(hash_Tag)

    #sjekker om programmet har besøkt 6 sider, om det har det så avbryter programmet. Ellers kjører det på nytt
    if len(visited) >= max_visited:
        #skriver ut alle besøkte sider
        print(visited)


    else:
        #velger en ny tilfeldig side som start_url
        start_url = random.choice(hash_Tag)
        str(start_url)
        # kaller funksjonen på nytt og går til en tilfeldig hashtags side
        sel_scrape(start_url, visited)


sel_scrape(start_url, visited)