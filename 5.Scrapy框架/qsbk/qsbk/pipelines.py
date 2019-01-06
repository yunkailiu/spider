# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
方法一：
import json
#专门用来保存数据
class QsbkPipeline(object):
    #初始化
    def __init__(self):
        self.fp = open("duanzi.json",'w',encoding="utf-8")
    #开始执行爬虫
    def open_spider(self,spider):
        print("爬虫开始。。。")
    #当爬虫有item传过来时会被调用
    def process_item(self, item, spider):
        item_jsom = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_jsom+'\n')
        return item
    #关闭爬虫
    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束。。。")
'''
'''
方法二：使用自带的法方法，但这是先将数据存储到内存，然后调用finish_exporting写回json文件，比较耗内存
from scrapy.exporters import JsonItemExporter
class QsbkPipeline(object):
    #初始化
    def __init__(self):
        self.fp = open("duanzi.json",'wb')
        self.exporter = JsonItemExporter(self.fp,ensure_ascii=False)
        self.exporter.start_exporting()
    #开始执行爬虫
    def open_spider(self,spider):
        print("爬虫开始。。。")
    #当爬虫有item传过来时会被调用
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    #关闭爬虫
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print("爬虫结束。。。")
'''
#方法三：适合存储大量的数据
from scrapy.exporters import JsonLinesItemExporter
class QsbkPipeline(object):
    #初始化
    def __init__(self):
        self.fp = open("duanzi.json",'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False)
    #开始执行爬虫
    def open_spider(self,spider):
        print("爬虫开始。。。")
    #当爬虫有item传过来时会被调用
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    #关闭爬虫
    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束。。。")
