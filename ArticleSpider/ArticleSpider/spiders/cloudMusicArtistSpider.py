# -*- coding: utf-8 -*-
import scrapy
import  re
import  random
from urllib import parse
from scrapy.http import Request
import os

#
# def mkdirs_if_not_exists(dir_):
#     if not os.path.exists(dir_) or not os.path.isdir(dir_):
#         os.makedirs(dir_)

class CloudmusicartistspiderSpider(scrapy.Spider):
    name = "cloudMusicArtistSpider"
    allowed_domains = ["www.cloudMusic.com"]
    start_urls = ['http://www.cloudMusic.com/']
    index = 0


    def start_requests(self):
        urls = [
            'http://music.163.com/#/discover/artist/cat?id=1001',
            # 'http://music.163.com/#/discover/artist/cat?id=1002',
            # 'http://music.163.com/#/discover/artist/cat?id=1003',
            # 'http://music.163.com/#/discover/artist/cat?id=2001',
            # 'http://music.163.com/#/discover/artist/cat?id=2002',
            # 'http://music.163.com/#/discover/artist/cat?id=2003',
            # 'http://music.163.com/#/discover/artist/cat?id=6001',
            # 'http://music.163.com/#/discover/artist/cat?id=6002',
            # 'http://music.163.com/#/discover/artist/cat?id=6003',
            # 'http://music.163.com/#/discover/artist/cat?id=7001',
            # 'http://music.163.com/#/discover/artist/cat?id=7002',
            # 'http://music.163.com/#/discover/artist/cat?id=7003',
            # 'http://music.163.com/#/discover/artist/cat?id=4001',
            # 'http://music.163.com/#/discover/artist/cat?id=4002',
            # 'http://music.163.com/#/discover/artist/cat?id=4003',
        ]
        for url in urls:
            suburls = [url + '&initial=%d' % i for i in range(65, 91)]  # from A to Z
            for suburl in suburls:
                yield scrapy.Request(url=suburl, cookies={'store_language': 'en'}, callback=self.parse)
                self.index += 1

    def parse(self, response):
        # mkdirs_if_not_exists('./data/')
        for i in range(self.index):
            with open('data.txt' , mode='wt', encoding='utf-8') as f:
                f.write(response.text)
                f.flush()
                f.close()

            self.log('Saved file successfully~')


