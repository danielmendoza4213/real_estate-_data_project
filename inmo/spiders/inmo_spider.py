import scrapy
import json
from inmo.items import InmoItem
from scrapy.loader import ItemLoader

""" Import of a list of linsk from inmoweb using selenium -> links_for_scrapy in file: data_cleaning.py  """

with open("list_of_links.json", "r") as file:
    links = json.load(file)


class Inmo(scrapy.Spider):
    name = "inmo"

    def start_requests(self):
        urls = links

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        l = ItemLoader(item=InmoItem(), response=response)

        l.add_xpath("data", "head/script[1]")
        try:
            yield l.load_item()
        except:
            pass


""" to run the spider, run in the terminal ->  scrapy crawl inmo -o data_inmo.json
    It is necessay to use the name 'data_inmo.json """
