# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义item数据模型
class QsbkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    pass
