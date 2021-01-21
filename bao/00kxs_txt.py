# _*_ coding： utf-8 _*_
# 开发团队：个人测试
# 开发人员：song
# 开发目的：个人学习
# 开发时间：2020/8/12 9:36
# 运行版本：python3.7
# 文件名称：00kxs.PY
# 开发工具：PyCharm

#爬取小说零点看书

import os
import re
import scrapy


class QuotesSpider(scrapy.Spider):
    name = '00kxs_txt'
    def start_requests(self):
        url = 'http://www.00kxs.com/html/6/6023/70261.html'
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        #获取文章标题
        title = response.xpath(".//*[@class='bookname']/h1/text()").extract_first()
        print(title)
        title = title.strip()
        #获取文章内容
        content = response.xpath(".//*[@id='content']").extract_first()
        #替换文章无用标签
        content = re.sub(r'\s', '', content)
        content = content.replace('<p>', '\n\t')
        content = content.replace('</p>', '')
        # content = content.replace('<br><br>', '\n\t')
        content = content.replace('<divid="content">', '')
        content = content.replace('</div>', '').strip()
        # print(content)
        #获取当前文件位置
        yth = os.getcwd()
        #打开追加文件
        flie = open(yth + '/cunchu/txt/我的美女公寓.txt','a',encoding='utf-8')
        #填写追加内容
        flie.write('\n' + title + '\n\n\t' + content + '\n\n')
        #关闭文件
        flie.close()
        #获取下一页地址
        next = response.xpath(".//*[@class='bottem2']/a")
        for i in next:
            name = i.xpath("text()").extract_first()
            if name == '下一章':
                href = i.xpath("@href").extract_first()
                print(href)
                #提交下一页
                yield response.follow(href,self.parse)

from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('00kxs_txt')    #需要启动爬虫名称
    process.start()   #启动爬虫
