# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wechatapp.items import WechatappItem

class WechatSpiderSpider(CrawlSpider):
    name = 'wechat_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=1&page=1']

    #限定爬取的url，类似正则表达式
    #callback:回调函数，表示是否要对该url调用这里的函数
    #follow：是否跟进
    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=1&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback="parse_detail",follow=False)
    )
    rules = (
        Rule(LinkExtractor(allow=r'.+Page=\d&searchKey=python'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):

        title = response.xpath("//h1[@class='ph']/text()").get()
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        pub_time = author_p.xpath(".//span/text()").get()
        content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(content).strip()
        item = WechatappItem(title = title,author = author,pub_time = pub_time,content = content)
        yield item

