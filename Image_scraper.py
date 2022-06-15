import requests
from bs4 import BeautifulSoup


# target URL
url = "https://en.wikipedia.org/wiki/Star_Wars:_The_Rise_of_Skywalker"

response = requests.request("GET", url)
data = BeautifulSoup(response.text, 'html.parser')

# finner elementer med img tag
images = data.find_all('img', src=True)

#printer antall bilder på siden
print('Number of Images: ', len(images))

#Printer alle src attributter for img elementer
image_src = [x['src'] for x in images]
image_src = [x for x in image_src ]
for image in image_src:
    print(image)