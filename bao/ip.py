#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 9:25
# @Author  : Ryu
# @Site    : 
# @File    : ip.py
# @Software: PyCharm


import geoip2.database
database_reader = geoip2.database.Reader('D:\\BaiduNetdiskDownload\\GeoLite2-City.mmdb')
def get_ip_info(ip):
    res = database_reader.city(ip)
    print(res)
    ip_info={}
    ip_info['地区']=res.continent.names["zh-CN"]
    ip_info['国家']=res.country.names['zh-CN']
    ip_info['省']=res.subdivisions.most_specific.names['zh-CN']
    ip_info['市'] = res.city.names['en']
    ip_info['经度']=res.location.longitude
    ip_info['纬度']=res.location.latitude
    return ip_info
ip = '128.1.133.117'
html = get_ip_info(ip)
print(html)