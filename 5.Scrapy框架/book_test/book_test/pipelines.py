# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookTestPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", user="root", passwd="7458", db="sys", port=3306)
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            author = item["author"][i]
            price = item["price"][i]
            sources = item["sources"][i]
            introduction = item["introduction"][i]
            sql = "insert into book_db(title,author,price,sources,introduction) values('" + title + "','" + author + "','" + price + "','" + sources + "','" + introduction + "')"
            self.cur.execute(sql)
            self.conn.commit()
        return item
        conn.close()
