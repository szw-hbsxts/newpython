# _*_ coding： utf-8 _*_
# 开发团队：个人测试
# 开发人员：song
# 开发目的：个人学习
# 开发时间：2020/5/30 16:46
# 运行版本：python3.7
# 文件名称：QQmusic_MP3.PY
# 开发工具：PyCharm


#爬取小说

import scrapy
import os
import requests
import json
from zdypython.items import ZdypythonItem

class QuotesSpider(scrapy.Spider):
    name = 'QQmusic_MP3'
    def start_requests(self):
        name = input("输入需要搜索歌曲名称：")
        self.headers = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=52055982925834080&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=30&w=' + name + '&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        #获取文章标题
        pass
        print(response)
        text = response.text#xpath('html').extract_first()
        music_info = eval(text)
        music_list = music_info["data"]["song"]["list"]
        print(music_list)
        print('测试')
        #输出获取列表
        #歌曲名称
        #歌手名称
        yt = 1
        print('编号：' + '\t\t歌名：' + '\t\t\t\t歌手：' + '\t\t\t\t时长：')
        for i in music_list:
            gqmc = i['title']
            gs = i['singer']
            if len(gs) == 1:
                ykju = gs[0]['name']
            else:
                ykju = ''
                for n in gs:
                    title = n['title']
                    ykju += title + '/'
            time_gfs = i['interval']
            time_gfs = self.get_time(time_gfs)
            print(str(yt) + '\t\t\t' + gqmc + '\t\t\t\t' + ykju + '\t\t\t' +time_gfs)
            yt += 1
        tr = input("输入需要下载的歌曲编号：")
        num = int(tr)
        #获取当前选择的歌曲
        nbv = music_list[num-1]
        ces = music_list[num-1]['singer']
        if len(ces) == 1:
            ykju = ces[0]['name']
        else:
            ykju = ''
            for n in ces:
                title = n['title']
                ykju += title + '、'

        print("您选择下载\n\t\t第"+tr+'条，歌曲:'+nbv['title']+"\t\t\t歌手:"+ykju+'\t\t时长：'+self.get_time(nbv['interval']))
        self.weuy = nbv['title']
        self.weuu = ykju
        self.songmid = nbv['mid']
        print(self.songmid)
        #获取真正的key
        key_url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey626277975566637&g_tk=5381&jsonpCallback=getplaysongvkey626277975566637&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"552068528","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"552068528","songmid":["' + self.songmid + '"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'
        yield scrapy.Request(url=key_url,callback=self.get_key)
        # key = requests.get(key_url)


    def get_time(self,time_gfs):
        m = time_gfs // 60
        s = time_gfs % 60
        return str(m) + ":" + str(s)

    def get_key(self,response):
        text = response.text  # xpath('html').extract_first()
        print(text)
        key_api = text.replace(r"getplaysongvkey626277975566637(", "")[:-1]
        print(key_api)
        print(self.songmid)
        key_api = json.loads(key_api)
        print(key_api)
        urs_list = key_api['req_0']['data']['midurlinfo'][0]['purl']
        print(urs_list)
        http = 'http://ws.stream.qqmusic.qq.com/'
        item = ZdypythonItem()
        self.weuu = self.weuu + '.m4a'
        self.weuu = self.weuu.replace('、.', '.')
        item['title'] = 'mp3/'+ self.weuy + ' - ' + self.weuu
        item['url'] = [http + urs_list]
        yield item



from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('QQmusic_MP3')    #需要启动爬虫名称
    process.start()   #启动爬虫