# -*- coding: utf-8 -*-
import scrapy
from book_test.items import BookTestItem
from bs4 import BeautifulSoup
import requests

class BookSpiderSpider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ['phei.com.cn']
    start_urls = ['https://www.phei.com.cn/module/goods/searchkey.jsp?Page=1&searchKey=python']

    def parse(self, response):
        title = response.xpath("//span[@class='book_title']/a/text()").getall()
        author = response.xpath("//span[@class='book_author']/text()").getall()
        price = response.xpath("//span[@class='book_price']/b/text()").getall()
        book_urls = response.xpath("//span[@class='book_title']/a/@href").getall()

        sources=[]
        for book_url in book_urls:
            sources.append("https://www.phei.com.cn"+book_url)

        introduction=[]
        for source in sources:
            response_source = requests.get(source).content.decode("utf8")
            soup = BeautifulSoup(response_source,'html5lib')
            source_introduction = soup.find('div',class_='book_inner_content')
            introduction.append(source_introduction.find('p').text)
        item = BookTestItem(title=title,author=author,price=price,sources=sources,introduction=introduction)
        yield item

        for i in range(2,6):
            next_url = "https://www.phei.com.cn/module/goods/searchkey.jsp?Page="+str(i)+"&searchKey=python"
            yield scrapy.Request(next_url,callback=self.parse)
