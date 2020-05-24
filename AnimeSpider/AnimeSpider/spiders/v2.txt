# -*- coding: utf-8 -*-

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
        movies = response.xpath('//div[@class="section"]/ul/li/div[@class="inner"]')
        print('=============================================')

        for movie in movies:

            item = BGM_SpiderItem()

            item['ranking'] = movie.xpath(
                './/span[@class="rank"]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/p/small/text()').extract()[0]
            item['score_num'] = re.findall(r'\d+',movie.xpath(
                './/p/span[@class="tip_j"]/text()').extract()[0])
            item['Tip'] = re.sub('\s','',movie.xpath(
                './/p[@class="info tip"]/text()').extract()[0])

            summary_url = 'http://bgm.tv' + movie.xpath('.//h3/a/@href').extract()[0]

            yield Request(url=summary_url, meta={'item': item}, callback=self.detail_parse)
            # yield item

        next_url = response.xpath('.//div[@class="clearit"]/div[@class="page_inner"]/a[@class="p"]/@href').extract()[-2]
        if next_url:
            next_url = 'http://bgm.tv/anime/browser' + next_url
            
            yield Request(next_url)

    def detail_parse(self, response):

        item = response.meta['item']
               
        pageA_inner = response.xpath(
            '///body[@class="bangumi"]/div[@id="wrapperNeue"]/div[@class="mainWrapper"]/div[@class="columns clearit"]/div[@id="columnSubjectHomeA"]/div[@id="bangumiInfo"]')
        pageB_inner = response.xpath(
            './/body[@class="bangumi"]/div[@id="wrapperNeue"]/div[@class="mainWrapper"]/div[@class="columns clearit"]/div[@id="columnSubjectHomeB"]/div[@class="subject_section"]')
        
    
        item['summary'] =re.sub('\s','',str(response.xpath(
            './/*[@id="subject_summary"]/text()').extract()[0]))
        item['movie_name'] = response.xpath(
            '//body[@class="bangumi"]/div[@id="wrapperNeue"]/div[@id="headerSubject"]/h1/a/text()').extract()[0]
        item['chinese_name']= pageA_inner.xpath(
            './/div/ul/li/text()').extract()[0]
        item['episode'] = pageA_inner.xpath(
            './/div/ul/li/text()').extract()[1]
        
        item['content'] = re.sub('\s','',str(pageB_inner.xpath(
            './/div[@class="content_inner clearit"]/div[@id="entry_list"]/div[@class="item clearit"]/div[@class="entry"]/div[@class="content"]/text()').extract()[0]))
        
        return item





