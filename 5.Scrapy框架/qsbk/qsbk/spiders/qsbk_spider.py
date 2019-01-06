# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs:
            #使用xpath进行提取数据，提取出来的数据是一个‘Selector’或‘SelectorList’对象
            #若要获取对象中的字符串，使用getall()和get()方法
            #getall()：获取‘Selector’中的所有文本，返回一个列表
            #get()：获取‘Selector’中的第一个文本，返回一个str类型
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            #duanzi = {"作者：": author,"内容：": content}按照字典返回
            item = QsbkItem(author = author,content = content)
            #交付给pipline处理
            yield item #变成生成器
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain + next_url,callback=self.parse)
