# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy import Request
from scrapy.spiders import Spider
from AnimeSpider.items import BGM_SpiderItem
import re


class BGM_Spider(Spider):
    name = 'BGM_Spider'
    start_urls = {
        'http://bgm.tv/anime/browser?sort=rank'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://bgm.tv/anime/browser?sort=rank'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.xpath(
            '//div[@class="section"]/ul/li/div[@class="inner"]')
        for movie in movies:
            AnimeItemLoader = ItemLoader(
                item=BGM_SpiderItem(), response=response)
            #用item方法，放上级目录爬取总会到第4页会出现缺失，
            #而使用Itemload读取数据并不会缺失
            summary_url = 'http://bgm.tv' + \
                movie.xpath('.//h3/a/@href').extract()[0]
            yield Request(url=summary_url, meta={'item': AnimeItemLoader.load_item()}, callback=self.detail_parse, dont_filter=True)

        next_url = response.xpath(
            './/div[@class="clearit"]/div[@class="page_inner"]/a[@class="p"]/@href').extract()[-2]
        #一个巧妙的翻页技巧，利用了py数组的特性
        if next_url:
            next_url = 'http://bgm.tv/anime/browser' + next_url
            yield Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        NextAnimeItemLoader = ItemLoader(
            item=response.meta['item'], response=response)

        NextAnimeItemLoader.add_xpath(
            'summary', '//*[@id="subject_summary"]/text()')
        NextAnimeItemLoader.add_xpath(
            'movie_name', '//body[@class="bangumi"]/div[@id="wrapperNeue"]/div[@id="headerSubject"]/h1/a/text()')
        NextAnimeItemLoader.add_xpath(
            'chinese_name', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='中文名: (.*)')
        NextAnimeItemLoader.add_xpath(
            'episode', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='话数: (.*)')
        NextAnimeItemLoader.add_xpath(
            'ranking', '/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/small[2]', re='\d+')
        NextAnimeItemLoader.add_xpath(
            'score', '/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[1]/div[2]/span[1]', re='\d.\d+')
        NextAnimeItemLoader.add_xpath(
            'score_num', '/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/div/div[3]/div/small/span', re='\d+')
        NextAnimeItemLoader.add_xpath(
            'director', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='导演: (.*)')
        NextAnimeItemLoader.add_xpath(
            'tv_time', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='放送开始: (.*)')
        NextAnimeItemLoader.add_xpath(
            'week', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='放送星期: (.*)')
        NextAnimeItemLoader.add_xpath(
            'movie_time', '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div/ul/li', re='上映年度: (.*)')

        return NextAnimeItemLoader.load_item()
