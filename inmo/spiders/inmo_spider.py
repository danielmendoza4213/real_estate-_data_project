import scrapy
import json
from inmo.items import InmoItem
from scrapy.loader import ItemLoader
from data_cleaning import links_for_scrapy

""" Import of a list of linsk from inmoweb using selenium -> links_for_scrapy in file: data_cleaning.py  """


class Inmo(scrapy.Spider):
    name = "inmo"

    def start_requests(self):
        urls = links_for_scrapy
        """ for some reason, scrapy does not follow all the items in the list,
             list has at least 800 intem(links ) TODO: verify this"""
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        l = ItemLoader(item=InmoItem(), response=response)
        l.add_xpath("data", "head/script[1]")

        yield l.load_item()


""" to run the spider, run in the terminal ->  scrapy crawl inmo -o data_inmo.json
    It is necessay to use the name 'data_inmo.json """
