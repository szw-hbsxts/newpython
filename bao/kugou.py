# -*- coding: utf-8 -*-
import scrapy
import time
import json
from myweibo.spiders.kugoufz import hhgg
from myweibo.items import MyweiboItem

class KugouSpider(scrapy.Spider):
    name = 'kugou'
    allowed_domains = ['www.kugou.com']
    start_urls = ['https://wwwapi.kugou.com']

    def parse(self, response):
        print('1、单首歌，2、歌手或歌曲类型')
        num = input('请选择搜索类型：')
        ttt = True
        while ttt:
            if num == '1' or num == '2':
                ttt = False
            else:
                print('1、单首歌，2、歌手或歌曲类型')
                print()
                num = input('输入的不符合规则，请选择搜索类型：')
        print(num)
        if num == '1':
            title = input('请输入歌曲名称:')
        else:
            title = input('请输入歌手或歌曲类型:')
        print(title)
        mn = hhgg().hg(num,title)
        print(mn)
        for j in mn:
            item = MyweiboItem()
            item['title'] = '/mp3/'+j[1]+'-'+j[0]+'.mp3'
            item['url'] = [j[2]]
            yield item



from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('kugou')    #需要启动爬虫名称
    process.start()   #启动爬虫
