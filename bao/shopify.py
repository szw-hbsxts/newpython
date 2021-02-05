#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 10:08
# @Author  : Ryu
# @Site    : 
# @File    : shopify.py
# @Software: PyCharm

import os
import pandas as pd
import chardet
import csv


class Shopify_csv():
    def __init__(self):
        #公共路径
        url = "D:\\python\\newpython\\zdypython\\zdypython\\spiders\\all\\"
        #目标文件
        path = url+"products_export_1.csv"
        #链接路径
        fsdfdssd = open(path, 'rb')
        #读取文件
        dataasdas = fsdfdssd.read()
        #获取文件编码
        encoding = chardet.detect(dataasdas)['encoding']
        #打印编码
        print(encoding)

        #读取文件
        xg_jh = pd.read_csv(path)
        #打印文件标头
        print(len(xg_jh.loc[1:]))
        #定义列表
        dss = []
        #遍历
        for numh in range(len(xg_jh.loc[0:])):
            #添加至列表
            dss.append(numh)
        #打印自定义列表
        print(dss)

        #生成
        data_new = xg_jh.drop(dss)

        new_txt = url+"betting_new_adbhdg.csv"
        data_new.to_csv(new_txt,encoding=encoding,index=0,header=0)
        print(chardet.detect(open(new_txt, 'rb',).read()))

        df_org = pd.read_csv(path)
        print(df_org.columns)

        aaa1 = open(new_txt, "w",encoding=encoding)  # 创建csv文件
        writer = csv.writer(aaa1)  # 创建写的对象
        # 先写入columns_name
        writer.writerow(df_org.columns)  # 写入列的名称
        # 写入多行用writerows                                #写入多行
        # writer.writerows([])
        aaa1.close()


if __name__ == '__main__':
    Shopify_csv()
