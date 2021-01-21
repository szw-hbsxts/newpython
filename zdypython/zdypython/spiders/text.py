#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/31 13:36
# @Author  : Ryu
# @Site    : 
# @File    : text.py
# @Software: PyCharm

import scrapy
import re,os

class ShopifSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['biduo.cc']
    start_urls = ['https://www.biduo.cc/biquge/39_39996/c13571637.html']

    def parse(self, response):
        #获取文章标题
        title = response.xpath(".//*[@class='bookname']/h1/text()").extract_first()
        print(title)
        #获取文章内容
        content = response.xpath('.//*[@id="content"]').extract_first()
        content = re.sub(r'\s', '',content)
        content = content.replace('<divid="content">','')
        content = content.replace('</div>', '').strip()
        content = content.replace('<br><br>', '\n\t')

        # 获取当前文件位置
        yth = os.getcwd()
        # 打开追加文件
        flie = open(yth + '/all/彪悍的人生.txt', 'a', encoding='utf-8')
        # 填写追加内容
        flie.write(title + '\n\n\t' + content + '\n\n')
        # 关闭文件
        flie.close()
        # 获取下一页地址
        next = response.xpath(".//*[@class='bottem1']/a")
        for i in next:
            name = i.xpath("text()").extract_first()
            if name == '下一章':
                href = i.xpath("@href").extract_first()
                print(href)
                # 提交下一页
                yield response.follow(href, self.parse)



from scrapy.crawler import CrawlerProcess  # 导入CrawlerProcess类
from scrapy.utils.project import get_project_settings  # 导入获取项目设置信息

if __name__ == '__main__':  # 程序入口
    process = CrawlerProcess(get_project_settings())  # 创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('text')  # 需要启动爬虫名称
    process.start()  # 启动爬虫
