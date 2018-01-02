# - * - coding: utf-8 - * -

from scrapy.spiders import CrawlSpider
from JDSpider.items import JdspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup
import random
import time
import requests
import re, json

class JdSpider(CrawlSpider):
    name = "JD"
    redis_key = "JDSpider:start_urls"
    start_urls = ["https://list.jd.com/list.html?cat=737,738,751&ev=exbrand_12380%7C%7C18136%7C%7C3085%7C%7C7420"]##电风扇
    # start_urls = [
    # # "https://search.jd.com/Search?keyword=%E5%90%B8%E5%B0%98%E5%99%A8&enc=utf-8&wq=%E5%90%B8%E5%B0%98%E5%99%A8&pvid=3019c1965d6741a3aa7a85bf0b888c56",##吸尘器
    # #               "https://search.jd.com/Search?keyword=%E5%8E%9F%E6%B1%81%E6%9C%BA&enc=utf-8&suggest=1.def.0.T15&wq=yuan&pvid=8f501a6d8afd4a9ea97501725c703265"##源汁机
    #            "https://search.jd.com/Search?keyword=%E7%94%B5%E9%A3%8E%E6%89%87&enc=utf-8&wq=%E7%94%B5%E9%A3%8E%E6%89%87&pvid=2c9b3a3b572a40c2bc7499c674563a45"
    #             ]
    # #
    def parse(self, response):
        item = JdspiderItem()
        selector = Selector(response)
        Products = selector.xpath('//*[@id="plist"]/ul/li')
        for each in Products:
            temphref = each.xpath('div/div[@class="p-img"]/a/@href').extract()
            temphref = str(temphref)
            ProductID = str(re.search('com/(.*?)\.html',temphref).group(1))


            product_typ_url="https://item.jd.com/"+ ProductID+".html"
            print("====product_typ_url:",product_typ_url)
            # product_typ=Selector(response).xpath('//html/body/div[9]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[2]/li[11]/text()').extract()
            product_typ=Selector(response).xpath('//*[@class="parameter2 p-parameter-list"]/ul[2]/li[11]/text()').extract()
            print(product_typ)

            item['product_typ']=product_typ
            yield item

        # donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print("Sleep time start......")
        # time.sleep(300)
        # print("donetime is:", donetime)

        #
        # nextLink = selector.xpath('//*[@id="J_bottomPage"]/span[1]/a[10]/@href').extract()
        # if nextLink:
        #     nextLink = nextLink[0]
        #     # print(nextLink)
        #     yield Request('https://list.jd.com/'+nextLink,callback=self.parse)
