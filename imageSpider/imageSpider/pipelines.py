# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request
import json
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


class ImagespiderPipeline(object):
    def process_item(self, item, spider):
        if item['img_url'][0:2] == '/r':
            item['img_url'] = 'https://www.dota2.com.cn' + item['img_url']
        elif item['img_url'][0:2] == '//':
            item['img_url'] = 'http:' + item['img_url']
        url = item['img_url']

        name = url[-8:]
        with open('test.json', 'ab') as f:
            text = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(text.encode('utf-8'))
        with open('dota2images/' + name, 'wb') as f:
            img = request.urlopen(url)
            f.write(img.read())
        return item
