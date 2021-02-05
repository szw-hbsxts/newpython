import scrapy
from shujutit import shag
import random
import re

class ShopifSpider(scrapy.Spider):
    name = 'shopif'
    allowed_domains = ['chaogadget.com']
    start_urls = ['https://www.chaogadget.com/collections/all']
    cp_id = 215
    url = []
    page = 2

    def parse(self, response):
        html = response.text
        # print(html)
        a = r'.*?(href="/collections/all/products/.+").*'
        b = re.findall(a,html)
        fd = []
        for i in b:
            c = r'.*?(/collections/all/products/.+").*'
            d = re.search(c,i)
            e = d.group(1).split('"')[0]
            fd.append(e)
        if len(fd) > 0:
            [self.url.append(v) for v in fd if not v in self.url]
            uuu = self.start_urls[0] + '?page=' + str(self.page)
            self.page += 1
            if self.page < 10:
                # 提交下一页
                yield response.follow(uuu, self.parse)
            else:
                for n in self.url:
                    m = n.replace('/collections/all', '')
                    yield scrapy.Request(url='https://www.' + self.allowed_domains[0] + m, callback=self.sdhjs)
        else:
            # hg = []
            for n in self.url:
                m = n.replace('/collections/all', '')
                yield scrapy.Request(url='https://www.'+self.allowed_domains[0]+m, callback=self.sdhjs)



        # lis_gf = response.xpath('.//a/@href').extract()
        # print(lis_gf)

        # yield scrapy.Request(url=href, callback=self.terge)


    def sdhjs(self, response):
        html = response.text
        # html = html.encode('utf-8')
        # print(html)

        hgs = shag()
        fd = hgs.zzpp(html)

        print(fd)

        id = fd['product']['id']
        variants = fd['product']['variants']

        cs = r'.*?({"id":'+str(id)+',"title".+"content":".*"}).*'
        kd = hgs.tiqu(cs,html)
        item = ['dsks','kij','mbbc','fdva','rtey','ljjk']
        nan = kd['variants']
        num = len(nan)
        title = kd['title']
        print(title)

        hgh = 'WD-jsjsn'+str(self.cp_id)+'-'+random.choice(item)
        description = str(kd['description'])
        description = description.replace('\\/', '/')
        description = description.replace('\\"', '"')
        print(type(description))

        ytr = 'catalog'
        im = kd['images']
        images = ''
        for immm in range(len(im)):
            if immm == len(im)-1:
                images += 'https:'+im[immm]
            else:
                images += 'https:'+im[immm]+', '
        if num > 1:
            su = 'variable'
            options = kd['options']

            dshg = [self.cp_id,su,hgh,title,'This is a variable product.',description,ytr,images,options]
            self.cp_id += 1
            print(dshg)
            opti01 = []
            opti02 = []
            opti03 = []
            for i in nan:
                su1 = i['option1']
                su2 = i['option2']
                su3 = i['option3']

                opti01.append(su1)
                opti02.append(su2)
                opti03.append(su3)

            c1 = []
            [c1.append(k1) for k1 in opti01 if not k1 in c1]
            c2 = []
            [c2.append(k2) for k2 in opti02 if not k2 in c2]
            c3 = []
            [c3.append(k3) for k3 in opti03 if not k3 in c3]

            ki = []
            if len(options) == 1:
                ki.append(c1)
            elif len(options) == 2:
                ki.append(c1)
                ki.append(c2)
            elif len(options) == 3:
                ki.append(c1)
                ki.append(c2)
                ki.append(c3)
            dshg.append(ki)
            print(dshg)
            kmn = hgs.tiancong(dshg)
            print(kmn)


            for nmn in nan:
                su = 'variation'
                sku = nmn['sku']
                pri = nmn['price']
                com = nmn['compare_at_price']
                opt = nmn['options']
                src = ''
                if nmn['featured_image'] != None:
                    src = nmn['featured_image']['src']

                sdjk = [self.cp_id,su,sku,title,pri,com,src,hgh,options,opt]
                print(sdjk)
                gfs = hgs.tiancong(sdjk)
                print(gfs)
                self.cp_id += 1

        else:

            su = 'simple'
            price = kd['price']
            compare_at_price = kd['compare_at_price']
            gfsg = [self.cp_id,su,hgh,title,'This is a simple product.',description,price,compare_at_price,ytr,images]
            gfs = hgs.tiancong(gfsg)
            print(gfs)

            self.cp_id += 1



from scrapy.crawler import CrawlerProcess      #导入CrawlerProcess类
from scrapy.utils.project import get_project_settings   #导入获取项目设置信息

if __name__ == '__main__':    #程序入口
    process = CrawlerProcess(get_project_settings())  #创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('shopif')    #需要启动爬虫名称
    process.start()   #启动爬虫
