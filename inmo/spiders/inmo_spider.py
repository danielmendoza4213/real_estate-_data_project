import scrapy
import json
from inmo.items import InmoItem
from scrapy.loader import ItemLoader

links = [
    "https://www.immoweb.be/fr/annonce/maison/a-louer/woluwe-saint-pierre/1150/9131268?searchId=601146c9a750b",
    "https://www.immoweb.be/fr/annonce/maison/a-vendre/erpent/5101/9140658?searchId=60130c640828e",
    "https://www.immoweb.be/en/classified/apartment/for-sale/anderlecht/1070/9081505?searchId=6011b04a00f66",
    "https://www.immoweb.be/en/classified/flat-studio/for-sale/forest/1190/9120080?searchId=6011b04a00f66",
    "https://www.immoweb.be/en/classified/apartment/for-sale/roeselare/8800/9101632?searchId=6011b04a00f66",
    "https://www.immoweb.be/en/classified/apartment/for-sale/gilly/6060/9074926?searchId=6011b04a00f66",
    "https://www.immoweb.be/en/classified/apartment/for-sale/tohogne/6941/9027050?searchId=6011b04a00f66",
]


class Inmo(scrapy.Spider):
    name = "inmo"

    def start_requests(self):
        urls = links
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        a = response.xpath("head//script[1]/text()").getall()

        yield {"a": a}
        # for row in response.xpath("/html/head"):

        #     l = ItemLoader(item=InmoItem(), selector=row)
        #     l.add_xpath("data1", "//script/")
        #     l.add_xpath("data2", "td")
        #     l.add_value("data3", "test")

        #     yield l.load_item()

