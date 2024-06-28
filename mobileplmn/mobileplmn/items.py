# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MobileplmnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mcc = scrapy.Field()
    mnc = scrapy.Field()
    iso = scrapy.Field()
    country = scrapy.Field()
    country_code = scrapy.Field()
    network = scrapy.Field()
    pass
