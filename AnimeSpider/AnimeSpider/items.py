# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
from scrapy.loader.processors import MapCompose, TakeFirst
import re


def get_number(value):
    pattern = re.compile(r'\d+')
    num = re.findall(pattern, value)
    if num:
        num = int(num[0])
    else:
        num = ' '
    return num


def get_Chinese(value):
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    Chinese = re.findall(pattern, value)
    if Chinese:
        Chinese = str(Chinese[0])
    else:
        Chinese = ' '
    return Chinese


def CleanBlank(value):
    cleaner = re.sub('\s', '', value)
    return cleaner


def convert_datetime(value):
    value = value.replace('年', '/')
    value = value.replace('月', '/')
    value = value.replace('日', '/')
    daytime = re.findall(r"(\d{4}/\d{1,2}/\d{1,2})", value)

    return daytime


class BGM_SpiderItem(scrapy.Item):

    ranking = scrapy.Field(
        output_processor=TakeFirst()
    )
    movie_name = scrapy.Field(
        output_processor=TakeFirst()
    )
    score = scrapy.Field(
        output_processor=TakeFirst()
    )
    score_num = scrapy.Field(
        output_processor=TakeFirst()
    )

    director = scrapy.Field(
        input_processor=MapCompose(get_Chinese),
        output_processor=TakeFirst()
    )
    chinese_name = scrapy.Field(
        input_processor=MapCompose(get_Chinese),
        output_processor=TakeFirst()
    )
    episode = scrapy.Field(
        input_processor=MapCompose(get_number),
        output_processor=TakeFirst()
    )

    summary = scrapy.Field(
        input_processor=MapCompose(CleanBlank),
        output_processor=TakeFirst()
    )
    week = scrapy.Field(
        input_processor=MapCompose(get_Chinese),
        output_processor=TakeFirst()
    )
    tv_time = scrapy.Field(
        input_processor=MapCompose(convert_datetime),
        output_processor=TakeFirst()
    )

    movie_time = scrapy.Field(
        input_processor=MapCompose(convert_datetime),
        output_processor=TakeFirst()
    )
