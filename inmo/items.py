import scrapy
import chompjs
from scrapy.loader import ItemLoader
from itemloaders.processors import Identity, MapCompose, Join
from w3lib.html import remove_tags

""" Ideally we should clean up the extracted data using a function"""


class InmoItem(scrapy.Item):

    data = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=Join(separator=""),
    )
