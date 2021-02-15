# coding:utf-8
# !/usr/bin/env python 布隆过滤器 高效去重


from pybloom_live import BloomFilter
import scrapy
from bs4 import BeautifulSoup as BS
import os

ls = os.linesep


class DmozSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = [
        "http://baike.baidu.com/item/%E7%BA%B3%E5%85%B0%E6%98%8E%E7%8F%A0"
    ]

    def parse(self, response):

        # fname = "/media/common/娱乐/Electronic_Design/Coding/Python/Scrapy/tutorial/tutorial/spiders/temp"
        #
        # html = response.xpath('//html').extract()[0]
        # fobj = open(fname, 'w')
        # fobj.writelines(html.encode('utf-8'))
        # fobj.close()

        # bloom = BloomFilter(100, 10)
        bloom = BloomFilter(1000, 0.001)
        animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle',
                   'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear',
                   'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
        # First insertion of animals into the bloom filter
        for animal in animals:
            bloom.add(animal)

        # Membership existence for already inserted animals
        # There should not be any false negatives
        for animal in animals:
            if animal in bloom:
                print('{} is in bloom filter as expected'.format(animal))
            else:
                print('Something is terribly went wrong for {}'.format(animal))
                print('FALSE NEGATIVE!')

        # Membership existence for not inserted animals
        # There could be false positives
        other_animals = ['badger', 'cow', 'pig', 'sheep', 'bee', 'wolf', 'fox',
                         'whale', 'shark', 'fish', 'turkey', 'duck', 'dove',
                         'deer', 'elephant', 'frog', 'falcon', 'goat', 'gorilla',
                         'hawk']
        for other_animal in other_animals:
            if other_animal in bloom:
                print('{} is not in the bloom, but a false positive'.format(other_animal))
            else:
                print('{} is not in the bloom filter as expected'.format(other_animal))

a = DmozSpider()
b = ''
a.parse(b)