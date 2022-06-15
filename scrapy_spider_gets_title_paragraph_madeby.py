import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

"""
•	Create a spider class by extending scrapy.Spider or scrapy.spiders.Crawlspider
•	Only crawl over the following domain: theverge.com
•	Start crawling from url: https://www.theverge.com/reviews
•	The spider should only parse pages that has the following pattern in their link href attribute:https://www.theverge.com/<INTEGER-NUMBER>/<ANY-SYMBOLWITHOUT '/' >
"""
#https://www.theverge.com/
class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = [' https://www.theverge.com']
    start_urls = ['https://www.theverge.com/reviews']

    #regex pattern for pages that can be parsed
    rules = [Rule(LinkExtractor(allow=r'(https?://www.theverge.com/)([\d +][ ^ /] * ) / ([ ^/]) *$'), callback='parse_items', follow=True)]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']//span[@class='text']/text()").extract()
        print(quotes)
        yield {'quotes': quotes}

