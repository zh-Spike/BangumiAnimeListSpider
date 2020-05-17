# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BGM_SpiderItem(scrapy.Item):

    ranking = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
    Tip = scrapy.Field()
    summary = scrapy.Field()
    chinese_name = scrapy.Field()
    episode = scrapy.Field()
    content = scrapy.Field()