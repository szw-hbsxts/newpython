# _*_ coding： utf-8 _*_
# 开发团队：个人测试
# 开发人员：song
# 开发目的：个人学习
# 开发时间：2020/6/2 8:31
# 运行版本：python3.7
# 文件名称：qqmusic.PY
# 开发工具：PyCharm

#爬取小说

import scrapy
import os
import requests
import json
from zdypython.items import ZdypythonItem

class QuotesSpider(scrapy.Spider):
    name = 'qqmusic_gsmc'
    def start_requests(self):
        soso = input("输入需要搜索分类名称：")
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=56851395523970476&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=99&w='+soso+'&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        self.name = soso
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        text = response.text  # xpath('html').extract_first()
        print(text)
        print(type(text))
        # music_info = eval(text)
        music_info = json.loads(text)
        print(type(music_info))
        print(music_info)
        music_list = music_info["data"]["song"]["list"]
        print(music_list)
        num = 1
        for li in music_list:
            title = li['title']
            time_gfs = li['interval']
            time_gfs = self.get_time(time_gfs)
            print(num,'\t\t',title,'\t\t',self.name,'\t\t',end='\t\n')
            self.songmid = li['mid']
            # 获取真正的key
            key_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey626277975566637&g_tk=5381&jsonpCallback=getplaysongvkey626277975566637&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"552068528","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"552068528","songmid":["' + self.songmid + '"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'
            key = requests.get(key_url)
            key_api = key.text.replace(r"getplaysongvkey626277975566637(", "")[:-1]
            key_api = json.loads(key_api)
            print(key_api)
            purl = key_api["req_0"]["data"]["midurlinfo"][0]["purl"]
            num += 1
            if purl == '':
                print(str(num-1) + title +'无法下载！！！')
                continue
            else:
                print(purl)
                http = 'http://ws.stream.qqmusic.qq.com/'
                item = ZdypythonItem()
                #weuu = '.m4a'    #大分类
                weuu = title + '.m4a'   #人名
                item['title'] = 'mp3/' + weuu
                item['url'] = [http + purl]
                yield item


    def get_time(self,time_gfs):
        m = time_gfs // 60
        s = time_gfs % 60
        return str(m) + ":" + str(s)




from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('qqmusic_gsmc')    #需要启动爬虫名称
    process.start()   #启动爬虫