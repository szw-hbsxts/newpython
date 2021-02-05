import scrapy
import ast
import json

class ChaogadgetSpider(scrapy.Spider):
    name = 'chaogadget'
    allowed_domains = ['chaogadget.com']
    start_urls = ['https://chaogadget.com/collections/all']

    def parse(self, response):
        href = response.css('#CollectionAjaxContent .grid--uniform .grid__item .grid-product__content')
        for i in href:
            link = i.css('.grid-product__link::attr(href)').extract_first()
            id = i.css('.quick-product__btn::attr(data-product-id)').extract_first()
            print(link,'<======>',id)
            yield scrapy.Request(url='https://chaogadget.com'+link,callback=self.products,meta={'id':id,'handle':link})

    def products(self,response):
        handle = response.meta['handle'].split('/')[-1]
        title = response.css('.grid-product__title::text').extract_first()
        description = response.xpath('.//*[@class="product-single__description rte"]').extract_first()
        vendor = response.xpath('.//*[@type="application/ld+json"]/text()').extract_first()
        print(type(vendor))
        print(vendor)
        # gdfhs = json.loads(vendor)
        # print(gdfhs)

        # print(description)
        print('\n')
        gtd = '#VariantsJson-'+response.meta['id']+'::text'
        text = response.css(gtd).extract_first().strip()
        text = text.replace('null','"null"')
        text = text.replace('true', '"true"')
        text = text.replace('false', '"false"')
        dicf = text.strip('[').strip(']')
        print(type(dicf))
        gfdg = eval(dicf)
        print(type(gfdg))
        if type(gfdg) == tuple:
            num = 0
            data = [handle]
            for i in gfdg:
                if num > 0:
                    data.append('')
                    data.append('')
                else:
                    data.append(title)
                    data.append(description)
                print(data)
                data = [handle]
                print('\n')
                num += 1
        else:
            print(gfdg)

    def cvs(self,data):
        pass


from scrapy.crawler import CrawlerProcess  # 导入CrawlerProcess类
from scrapy.utils.project import get_project_settings  # 导入获取项目设置信息

if __name__ == '__main__':  # 程序入口
    process = CrawlerProcess(get_project_settings())  # 创建CrawlerProcess类对象并传入项目设置信息参数
    process.crawl('chaogadget')  # 需要启动爬虫名称
    process.start()  # 启动爬虫