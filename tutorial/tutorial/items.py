# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    company_name = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    pass
