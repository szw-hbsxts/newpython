# _*_ coding： utf-8 _*_
# 开发团队：个人测试
# 开发人员：song
# 开发目的：个人学习
# 开发时间：2020/9/15 20:18
# 运行版本：python3.7
# 文件名称：weibo.PY
# 开发工具：PyCharm

import sys
import requests
from bs4 import BeautifulSoup
import base64
import os,sys,time
import json

class weibo():
    def __init__(self):
        print('测试数据')
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAkkPGQQ_i8J7Giee5FBumF0cpzm1Eh2Xw-ZWaiF1XkmU&count=21&max_cursor=0&aid=1128&_signature=z1B7rgAAkDnGHAG7du4eoc9Qe7&dytk='
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer': 'https://www.iesdouyin.com/share/user/72955161571?sec_uid=MS4wLjABAAAAkkPGQQ_i8J7Giee5FBumF0cpzm1Eh2Xw-ZWaiF1XkmU&timestamp=1600242902&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': 'MONITOR_WEB_ID=9ee710fd-26eb-4bcc-b927-307efb140f2b'
        }
        self.requests(url,headers)

    def requests(self,url,headers):
        print('002')
        txt = requests.get(url,headers=headers)
        txt.encoding = 'gbk2312'  # 设置编码方式
        print(txt)
        print(txt.text)
        # print(json.loads(txt.text))



if __name__ == '__main__':
    weibo()
