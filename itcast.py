# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.cookies import CookieJar
import re
from w3lib.html import remove_tags
# from myweibo.spiders.excel import hgf

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['weibo.com']
    setitle = '醉酒男天桥坠落被司机用车顶接住'
    start_urls = ['https://s.weibo.com/weibo?q='+setitle+'&sudaref=passport.weibo.com&page=3']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'Cookie': 'SINAGLOBAL=8959082401648.818.1600058582906; SCF=AmQbwAlxLul73V9IqZ7jRPUrNyYqqjpBaxEjB91XTSQWshPhhOjvIkko7o03ecyWwhC37xcapCxxQt96VqU8r78.; SUHB=0qjk9hU47hT3cq; UOR=,,login.sina.com.cn; webim_unReadCount=%7B%22time%22%3A1600178477800%2C%22dm_pub_total%22%3A3%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A54%2C%22msgbox%22%3A0%7D; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WF_wWLhogDUM1VbUg_GnnIe; SUB=_2AkMoPFW1dcPxrARVmPkdyGznboxH-jyb6TxDAn7uJhMyAxh87noRqSVutBF-XI-1AzEJNYkVwTFn5ymnPqkrOE55; _s_tentry=-; Apache=2634798834534.1177.1600228443322; ULV=1600228443333:3:3:3:2634798834534.1177.1600228443322:1600172631833; WBtopGlobal_register_version=434eed67f50005bd; WBStorage=70753a84f86f85ff|undefined',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer':'https://s.weibo.com/weibo?q='+setitle+'&sudaref=passport.weibo.com'
    }}

    def parse(self, response):
        div = response.css('div.m-con-l > div > div.card-wrap')
        a = 1
        for i in div:
            #微博名
            name_id = i.css('a.name ::text').extract_first()
            #微博主id
            href = i.css('a.name ::attr(href)').extract_first()
            #发布内容
            conten = i.css('div.content > p.txt').extract_first()
            conten = remove_tags(conten)
            conten = re.sub(r'\s', '', conten )
            uy = '#'+ItcastSpider.setitle+'#'
            conten = conten.replace(uy,'')
            #评论、点赞、转发、收藏、发布时间
            tim = i.css('p.from > a ::text').extract()

            #发布时间
            fb = tim[0].strip().split()
            if len(fb) == 1:
                fb = fb[0]
            elif len(fb) == 2:
                ces = fb[1].find('转赞')
                if ces == -1:
                    fb = fb[0] + fb[1]
                else:
                    fb = fb[0]
            elif len(fb) == 3:
                fb = fb[0] + fb[1]
            #发布来源
            ly = len(tim)
            if ly > 1:
                ly = tim[1]
            else:
                ly = '无显示'

            #获取评论点赞
            pl = i.css('div.card-act > ul > li > a ').extract()
            lis = []
            for j in pl:
                j = remove_tags(j)
                j = re.sub(r'\s', '',j)
                lis.append(j)

            #分类列表
            sc = lis[0].replace('收藏', '')
            zfa = lis[1].replace('转发', '')
            pingl = lis[2].replace('评论', '')
            dianz = lis[3]
            #为空赋值
            if sc == '':
                sc = '0'
            if zfa == '':
                zfa = '0'
            if pingl == '':
                pingl = '0'
            if dianz == '':
                dianz = '0'
            print(ItcastSpider.setitle,'\n',name_id,'\n',href,'\n',conten,'\n',sc,'\n',zfa,'\n',pingl,'\n',dianz,'\n',fb,'\n',ly)
            #生成excel文件
            # hgf(ItcastSpider.setitle,name_id,href,conten,sc,zfa,pingl,dianz,fb,ly)

            print(a)
            a += 1
        # href = response.css('a.name ::attr(href)').extract_first()
        # id = response.css('a.name ::text').extract_first()
        # print(id)
        # ty = response.css('div.card-act > ul > li > a ::text')
        # print(ty)



from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('itcast')    #需要启动爬虫名称
    process.start()   #启动爬虫

