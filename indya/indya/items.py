# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IndyaItem(scrapy.Item):
    title = scrapy.Field()
    cost_price = scrapy.Field()
    sale_price = scrapy.Field()
    description = scrapy.Field()
    img0 = scrapy.Field()
    img1 = scrapy.Field()
    img2 = scrapy.Field()
    img3 = scrapy.Field()
    img4 = scrapy.Field()
    img5 = scrapy.Field()

    pass
