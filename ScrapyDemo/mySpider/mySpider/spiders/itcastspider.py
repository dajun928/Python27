#!/usr/bin/env python
# -*- coding:utf-8 -*-
#单个网页爬虫Demo
import scrapy
from ..items import ItcastItem
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#" ]

    def parse(self, response):
        # with open("teacher.html", "w") as f:
        #     f.write(response.body)
        # # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        for each in teacher_list:
            print "分割线1".center(100, '-')
            item = ItcastItem()
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            yield item


