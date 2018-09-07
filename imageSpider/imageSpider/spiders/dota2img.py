# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import ImagespiderItem


class Dota2imgSpider(scrapy.Spider):
    name = 'dota2img'
    allowed_domains = ['www.dota2.com.cn']
    start_urls = ['https://www.dota2.com.cn/enjoy/gamewall/index' + str(num) + '.html' for num in range(1, 4)]
    def parse(self, response):
        for url in response.xpath('/html/body/div[1]/div/div[1]/div[3]/ul/li/p/span[1]/a/@href'):
            item = ImagespiderItem()
            item['img_url'] = url.extract()
            yield item
        scrapy.Request

