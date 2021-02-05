#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 16:32
# @Author  : Ryu
# @Site    : 
# @File    : weiwenxinyu.py
# @Software: PyCharm



import scrapy

class ShopifSpider(scrapy.Spider):
    name = 'weiwenxinyu'
    allowed_domains = ['author.baidu.com']
    start_urls = ['https://author.baidu.com/home?from=bjh_article&app_id=1550883859845077']

    def parse(self, response):
        html = response.text
        print(html)




from scrapy.crawler import CrawlerProcess  # 导入CrawlerProcess类
from scrapy.utils.project import get_project_settings  # 导入获取项目设置信息

if __name__ == '__main__':  # 程序入口
    process = CrawlerProcess(get_project_settings())  # 创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('weiwenxinyu')  # 需要启动爬虫名称
    process.start()  # 启动爬虫

