import scrapy


class TudinetSpider(scrapy.Spider):
    name = 'tudinet'
    allowed_domains = ['tudinet.com']
    start_urls = ['http://tudinet.com/']

    def parse(self, response):
        pass
