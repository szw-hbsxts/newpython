#爬取小说零点看书

import scrapy
import json
import csv
import os
from numpy import *

class QuotesSpider(scrapy.Spider):
    name = 'cs'
    allowed_domains = ['funpinpin.com']
    start_urls = ['https://funpinpin.com/housebeauty/shop/']
    numm = 2
    cp_id = 121

    def parse(self, response):
        #获取文章标题
        # title = response.text
        # print(title)
        li = response.css('div.py-container ol li a.py-img')
        print(li)
        for yt in li:
            href = yt.css('::attr(href)').extract_first()
            yield scrapy.Request(url=href, callback=self.terge)
        url = self.start_urls[0]+'page/'+str(self.numm)+'/'
        # 提交下一页
        yield response.follow(url, self.parse)
        #self.numm += 1

    def terge(self,response):
        # title = response.text
        # print(title)
        gf = response.css('div.px-quantity-box').extract()
        if gf != []:
            title = response.css('h1.product-title ::text').extract_first()
            title = title.strip()
            # sku = title.replace(" ","-")
            # sku = sku.replace("【", "")
            # sku = 'woo-'+ sku.replace("】", "-")
            sku = "woo-fnjhs-" + str(self.cp_id)

            img = response.css('div.woocommerce-product-gallery figure.woocommerce-product-gallery__wrapper div.woocommerce-product-gallery__image a ::attr(href)').extract()
            uy = ''
            nnn = len(img)
            for ing in img:
                if ing == img[nnn - 1]:
                    uy += ing
                else:
                    uy += ing + ", "

            price = response.css('p.price.variable span.woocommerce-Price-amount.amount').extract()
            num = len(price)
            print(num)
            if num == 0:
                #打折商品没有选项
                pass
                tr = response.css('p.price.simple ::text').extract()
                if len(tr) > 0:
                    print(tr)
            elif num == 1:
                #固定价格商品，选项有
                pass

                trr = response.css('form.variations_form.cart table.variations tr')
                ytjh = []
                for ijih in trr:
                    nmnn = ijih.css('label.uk-form-label ::text').extract()
                    uom = ijih.css('button ::text').extract()
                    nmkj = len(uom)
                    ytjh.append(nmnn[0])
                    mjhk = ''
                    for kjk in uom:
                        if kjk == uom[nmkj - 1]:
                            mjhk += kjk
                        else:
                            mjhk += kjk + ", "
                    ytjh.append(mjhk)
                data = [self.cp_id,'variable',sku,title,'This is a variable product.','sdbghs',uy]
                data.append(ytjh)
                print(data)
                self.kloijsd(data)
                self.cp_id += 1

                tr = response.css('form.variations_form ::attr(data-product_variations)').extract()
                tt = tr[0].replace("['[{", "\"{").replace("'}]']", "}\"")
                tt = json.loads(tt)

                for i in tt:
                    m_sku = 'woo-gfd-'+str(self.cp_id)
                    lis_hg = [self.cp_id,'variation',m_sku]
                    shux = i['attributes']
                    lis_hg.append(title)
                    lis_hg.append(i['display_price'])
                    lis_hg.append(i['display_regular_price'])
                    lis_hg.append(i['image']['url'])
                    lis_hg.append(sku)
                    dfns = []
                    for vb in shux:
                        gfg = vb.replace("attribute_", "")
                        dfns.append(gfg)
                        dfns.append(shux[vb])
                    lis_hg.append(dfns)
                    self.cp_id += 1
                    self.kloijsd(lis_hg)
                    print(lis_hg)




            else:

                pass
                tr = response.css('form.variations_form ::attr(data-product_variations)').extract()
                tt = tr[0].replace("['[{", "\"{").replace("'}]']", "}\"")
                tt = json.loads(tt)

                trr = response.css('form.variations_form.cart table.variations tr')
                ytjh = []
                for ijih in trr:
                    nmnn = ijih.css('label.uk-form-label ::text').extract()
                    uom = ijih.css('button ::text').extract()
                    nmkj = len(uom)
                    ytjh.append(nmnn[0])
                    mjhk = ''
                    for kjk in uom:
                        if kjk == uom[nmkj - 1]:
                            mjhk += kjk
                        else:
                            mjhk += kjk + ", "
                    ytjh.append(mjhk)

                data = [self.cp_id,'variable',sku,title,'This is a variable product.','sdbghs']
                data.append(uy)
                data.append(ytjh)
                print(data)
                self.kloijsd(data)

                self.cp_id += 1

                for i in tt:
                    m_sku = 'woo-gfd-' + str(self.cp_id)
                    lis_hg = [self.cp_id,'variation',m_sku,title]
                    shux = i['attributes']
                    dfns = []
                    for vb in shux:
                        gfg = vb.replace("attribute_", "")
                        dfns.append(gfg)
                        dfns.append(shux[vb])
                    xj = i['display_price']
                    yj = i['display_regular_price']
                    img = i['image']['url']

                    lis_hg.append(yj)
                    lis_hg.append(xj)
                    lis_hg.append(img)
                    lis_hg.append(sku)
                    lis_hg.append(dfns)
                    print(lis_hg)
                    self.kloijsd(lis_hg)
                    self.cp_id += 1
        self.cp_id += 1


    def kloijsd(self,data):
        new_data = []
        a1 = '1'
        a2 = '0'
        a3 = 'visible'
        a4 = ''
        a5 = 'taxable'
        if data[1] == 'variable':
            new_data.append(data[0])
            new_data.append(data[1])
            new_data.append(data[2])
            new_data.append(data[3])
            new_data.append(a1)
            new_data.append(a2)
            new_data.append(a3)
            new_data.append(data[4])
            new_data.append(data[5])
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a5)
            new_data.append(a4)
            new_data.append(a1)
            new_data.append(a4)
            new_data.append(a2)
            new_data.append(a2)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a1)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(data[1])
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(data[6])
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a2)

            numhgg = len(data[7])

            for y in range(numhgg):
                new_data.append(data[7][y])
                if y == 1 or y == 3 or y == 5:
                    new_data.append(a1)
                    new_data.append(a1)
            for i in range(12-numhgg*2):
                    new_data.append(a4)

            new_data.append(a1)

        elif data[1] == 'variation':
            new_data.append(data[0])
            new_data.append(data[1])
            new_data.append(data[2])
            new_data.append(str(data[3]))
            new_data.append(a1)
            new_data.append(a2)
            new_data.append(a3)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a5)
            new_data.append(a4)
            new_data.append(a1)
            new_data.append(a4)
            new_data.append(a2)
            new_data.append(a2)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a2)
            new_data.append(a4)
            new_data.append(str(data[5]))
            new_data.append(str(data[4]))
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(data[6])
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(data[7])
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a4)
            new_data.append(a2)

            numhgg = len(data[8])
            for K in range(numhgg):
                new_data.append(data[8][K])
                if K == 1 or K == 3 or K == 5:
                    new_data.append(a4)
                    new_data.append(a1)
            for H in range(12-numhgg*2):
                    new_data.append(a4)

        elif data[1] == 'simple':
            print(data)


        url_fd = os.getcwd()
        # 1. 创建文件对象
        f = open(url_fd + '\\all\\products_sdv.csv', 'a',encoding='UTF-8-SIG',newline="")
        print(f)
        # 2. 基于文件对象构建 csv写入对象
        csv_writer = csv.writer(f)
        # 3. 构建列表头
        # csv_writer.writerow(["姓名", "年龄", "性别"])
        # 4. 写入csv文件内容
        csv_writer.writerow(new_data)
        # 5. 关闭文件
        f.close()

from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('cs')    #需要启动爬虫名称
    process.start()   #启动爬虫
