#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 9:49
# @Author  : Ryu
# @Site    : 
# @File    : cs.py
# @Software: PyCharm

import os
import pandas as pd
import chardet
import csv
import codecs
import json
import re

class fds():
    def __init__(self):
        self.id = 545
        #获取当前文件位置
        yth = os.getcwd()
        flie = open(yth + '\\data\\txt.txt', 'r', encoding='utf-8')
        f = flie.read()
        f = f.split()
        #获取csv数据
        data = pd.read_csv(yth+"\\data\\products_export.csv")  # 读取csv文件



        path = yth+"\\data\\sample_products_gfd.csv"
        fsdfdssd= open(path, 'rb')
        dataasdas = fsdfdssd.read()
        print(chardet.detect(dataasdas))
        xg_jh = pd.read_csv(path)  # 读取csv文件
        print(xg_jh.loc[0])
        print(chardet.detect(dataasdas))

        print(len(xg_jh.loc[1:]))
        dss = []
        for numh in range(len(xg_jh.loc[0:])):
            dss.append(numh)
        print(dss)
        data_new = xg_jh.drop(dss)

        new_txt = yth+"\\data\\betting_new.csv"
        data_new.to_csv(new_txt,encoding='UTF-8-SIG',index=0,header=0)
        print(chardet.detect(open(new_txt, 'rb',).read()))

        df_org = pd.read_csv(yth+"\\data\\products_sdv.csv")
        print(df_org.columns)

        aaa1 = open(yth+"\\data\\betting_new.csv", "w",encoding='UTF-8-SIG')  # 创建csv文件
        writer = csv.writer(aaa1)  # 创建写的对象
        # 先写入columns_name
        writer.writerow(df_org.columns)  # 写入列的名称
        # 写入多行用writerows                                #写入多行
        # writer.writerows([])
        aaa1.close()

        print(chardet.detect(open(yth+"\\data\\betting_new.csv", 'rb',).read()))

        name_list = []
        gf = {}
        mc = []
        zhi = []
        for i in range(len(data.loc[0:])):
            fd = data.loc[i,['Handle']]
            dhu = fd.values[0]
            sku = data.loc[i, ['Variant SKU']].values[0]
            Price1 = data.loc[i, ['Variant Price']].values[0]
            Price2 = data.loc[i, ['Variant Compare At Price']].values[0]
            img = data.loc[i,['Image Src']].values[0]
            gsh = [sku,img,Price1,Price2]
            aq = []
            tag = data.loc[i,['Tags']].values[0]
            if str(tag) == 'nan':
                tag = ''

            if dhu in name_list:
                if str(data.loc[i,['Option1 Value']].values[0]) != 'nan':
                    gf[dhu]['Option'].append(gsh)
                    if str(img) != 'nan':
                        gf[dhu]['image'].append(img)
                    g = len(gf[dhu]['zhi'])
                    for mkl in range(g):
                        yhyty = 'Option'+str(mkl+1)+' Value'
                        gf[dhu]['zhi'][mkl].append(data.loc[i, [yhyty]].values[0])
                        aq.append(data.loc[i,[yhyty]].values[0])
                else:
                    if str(img) != 'nan':
                        gf[dhu]['image'].append(img)
                gsh.append(aq)
                gsh.append(tag)
                print(gsh)
            else:
                name_list.append(dhu)
                title = data.loc[i, ['Title']].values[0]
                boy = data.loc[i, ['Body (HTML)']].values[0]
                ko = []
                attr_na1 = data.loc[i, ['Option1 Name']].values[0]
                if attr_na1 != 'nan':
                    attr_va1 = data.loc[i, ['Option1 Value']].values[0]
                    mc.append(attr_na1)
                    ko.append(attr_va1)
                    aq.append(attr_va1)
                    zhi.append(ko)
                    ko = []
                    attr_na2 = data.loc[i, ['Option2 Name']].values[0]
                    if str(attr_na2) != 'nan':
                        attr_va2 = data.loc[i, ['Option2 Value']].values[0]
                        mc.append(attr_na2)
                        ko.append(attr_va2)
                        aq.append(attr_va2)
                        zhi.append(ko)
                        ko = []
                        attr_na3 = data.loc[i, ['Option3 Name']].values[0]
                        if str(attr_na3) != 'nan':
                            mc.append(attr_na3)
                            attr_va3 = data.loc[i, ['Option3 Value']].values[0]
                            ko.append(attr_va3)
                            aq.append(attr_va3)
                            zhi.append(ko)
                            ko = []
                gsh.append(aq)
                gsh.append(tag)
                sku_zhu = 'wenjhf-'
                gf[dhu] = {'title':title,'boy':boy,'sku':sku_zhu,'Option':[gsh],'image':[img],'mc':mc,'zhi':zhi}
                print(gf)
            mc = []
            zhi = []
        self.a(name_list,gf)


    def a(self,name,gf):
        for i in name:
            nb = gf[i]['mc']
            gimn = gf[i]['image']
            gimn = ', '.join(gimn)
            fsdjs = []
            zhu_id = str(self.id)
            ghfh = gf[i]['sku']+zhu_id
            if nb[0] != 'Title':
                hgjs = [zhu_id,'variable',ghfh,gf[i]['title'],1,0,'visible','',gf[i]['boy'],'','','taxable','',1,
                      '',0,0,'','','','',1,'','','','gefds','','',str(gimn),'','','','','','','','',0
                      ]
                self.id += 1
                for l in range(len(nb)):
                    hgjs.append(nb[l])
                    lkpp = gf[i]['zhi'][l]

                    list2 = []
                    for ds in lkpp:
                        if ds not in list2:
                            list2.append(ds)
                    list2 = ', '.join(list2)
                    hgjs.append(list2)

                    hgjs.append(1)
                    hgjs.append(1)

                for n in range(12 - len(nb) * 4):
                    hgjs.append('')
                hgjs.append('1')
                ydsf = self.b(hgjs)
                print(ydsf)
                poio = gf[i]['Option']
                print(poio)
                dsjknjs = []
                for iljh in range(len(poio)):
                    dsjknjs.append(iljh)

                mlo = 1
                for lmn in dsjknjs:
                    print(lmn)
                    kjjj_sku = poio[lmn][0]
                    if str(kjjj_sku) == 'nan':
                        kjjj_sku = gf[i]['sku']
                    pingk = poio[lmn][1]
                    if str(pingk) == 'nan':
                        pingk = ''
                    self.id += 1
                    loi1 = poio[lmn][2]
                    loi2 = poio[lmn][3]
                    if int(loi1) > int(loi2):
                        loi2 = loi1
                    tie = gf[i]['title'] + ' - ' + ', '.join(poio[lmn][4])

                    jhfh = [str(self.id), 'variation',kjjj_sku,tie, 1, 0, 'visible', '', '', '', '',
                            'taxable', 'parent', 1,
                            '', 0, 0, '', '', '', '',1, '',str(loi1),str(loi2),
                            '',poio[lmn][5],'',pingk,'','',ghfh,
                            '','','','','',str(mlo)
                            ]
                    loi1 = ''
                    loi2 = ''
                    mlo += 1
                    self.id += 1
                    for q in range(len(nb)):
                        jhfh.append(nb[q])
                        eedh = poio[lmn][4][q]
                        jhfh.append(eedh)
                        jhfh.append('')
                        jhfh.append(1)

                    for sd in range(12 - len(nb) * 4):
                        jhfh.append('')
                    mn = self.b(jhfh)
                    print(mn)
            else:
                print(gf[i]['title'])
                print(gf[i]['Option'])
                xj = gf[i]['Option'][0][2]
                yj = gf[i]['Option'][0][3]
                if xj > yj:
                    yj = xj
                dsiu = [str(self.id), 'simple', gf[i]['sku'], gf[i]['title'], '1', '0', 'visible', '', gf[i]['boy'],
                        '', '', 'taxable', 'parent', 1,
                        '', '0', '0', '', '', '', '', '1', '',xj,yj, '', '', '', str(gimn), '', '', '', '', '', '',
                        '', '', '0'
                        ]
                ytr = self.b(dsiu)
                print(ytr)

                self.id += 1

            self.id += 1



    def b(self,data):
        print(data)

        # 获取当前文件位置
        url_fd = os.getcwd()
            # # 打开追加文件
            # flie = open(url_fd + '/data/东方红就是.txt', 'a', encoding='utf-8')
            # # 填写追加内容
            # flie.write(t.decode(encoding="utf8",errors="xmlcharrefreplace"))
            # # 关闭文件
            # flie.close()


        csvFile = open(url_fd+'/data/betting_new.csv',"a",encoding='UTF-8-SIG',newline="")  # 创建csv文件
        writer = csv.writer(csvFile)  # 创建写的对象
        # 先写入columns_name
        # writer.writerow(["index", "a_name", "b_name"])  # 写入列的名称
        # 写入多行用writerows                                #写入多行
        writer.writerows([data])
        csvFile.close()

        print(chardet.detect(open(url_fd + "\\data\\betting_new.csv", 'rb', ).read()))

if __name__ == '__main__':
    fds()