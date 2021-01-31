import scrapy
import chompjs
from scrapy.loader import ItemLoader
from itemloaders.processors import Identity, MapCompose, Join
from w3lib.html import remove_tags

""" Ideally we should clean up all the extracted data using a function in this file."""
""" Class InmoItem will procces the data extracted from the links and do some manipulation before store it
    in the exported file. As mentioned above, ideally, we could clean it better adding more functions
    The Field() method has the remove_tags function that will remove the tags <script> and the 
    Join method that will make the content a string
    """


class InmoItem(scrapy.Item):

    data = scrapy.Field(
        input_processor=MapCompose(remove_tags), output_processor=Join(separator=""),
    )
