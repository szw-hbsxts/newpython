# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import scrapy

from scrapy.pipelines.files import FilesPipeline


class FilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        url = item['url'][0]
        yield scrapy.Request(url=url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        title = item['title']
        return title
