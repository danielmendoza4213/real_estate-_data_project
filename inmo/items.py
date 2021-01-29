import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import json


def remove_space(value):
    return value.strip()


def replace_n(value):
    return " ".join(value.split())


class InmoItem(scrapy.Item):
    data1 = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space),
        output_processor=TakeFirst(),
    )
    data2 = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_space, replace_n),
        output_processor=TakeFirst(),
    )
    data3 = scrapy.Field()
