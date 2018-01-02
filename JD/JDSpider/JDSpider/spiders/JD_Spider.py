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
    name = "JDSpider"
    redis_key = "JDSpider:start_urls"
    start_urls = [
        # "https://list.jd.com/list.html?cat=737,738,751",##电风扇
        # "https://list.jd.com/list.html?cat=737,738,751&ev=exbrand_12380%7C%7C3085%7C%7C7420%7C%7C18136%7C%7C3659",
        # "https://list.jd.com//list.html?cat=737,738,751&page=4"
        ##风扇（品牌）
        # "https://list.jd.com/list.html?cat=737,738,1278",##冷风扇
        # "https://list.jd.com/list.html?cat=737,752,13116",##源汁机
        # "https://list.jd.com/list.html?cat=737,738,745",##吸尘器
        'https://search.jd.com/Search?keyword=195%2060r15&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1&ev=exbrand_%E7%B1%B3%E5%85%B6%E6%9E%97%EF%BC%88MICHELIN%EF%BC%89%7C%7C%E6%99%AE%E5%88%A9%E5%8F%B8%E9%80%9A%EF%BC%88Bridgestone%EF%BC%89%7C%7C%E9%A9%AC%E7%89%8C%EF%BC%88Continental%EF%BC%89%7C%7C%E9%82%93%E7%A6%84%E6%99%AE%EF%BC%88DUNLOP%EF%BC%89%7C%7C%E4%BD%B3%E9%80%9A%E8%BD%AE%E8%83%8E%EF%BC%88Giti%EF%BC%89%7C%7C%E5%9B%BA%E7%89%B9%E5%BC%82%EF%BC%88Goodyear%EF%BC%89%7C%7C%E5%80%8D%E8%80%90%E5%8A%9B%EF%BC%88Pirelli%EF%BC%89%7C%7C%E5%80%8D%E8%80%90%E5%8A%9B%EF%BC%88PEINEILI%EF%BC%89%7C%7C%E9%9F%A9%E6%B3%B0%E8%BD%AE%E8%83%8E%7C%7C%E9%9F%A9%E6%B3%B0%EF%BC%88Hankook%EF%BC%89%5E#J_searchWrap'
        ]


    def parse(self, response):
        item = JdspiderItem()
        selector = Selector(response)
        Products = selector.xpath('//*[@id="plist"]/ul/li')
        for each in Products:
            # p_Name = each.xpath('div/div[@class="p-name"]/a/em/text()').extract()
            p_Name = each.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()').extract()
            shop_name= each.xpath('div/div[@class="p-shop"]/@data-shop_name').extract()
            temphref = each.xpath('div/div[@class="p-img"]/a/@href').extract()
            temphref = str(temphref)
            ProductID = str(re.search('com/(.*?)\.html',temphref).group(1))
            # ProductID='1069555'
            ##获取价格
            json_url_p = 'http://p.3.cn/prices/mgets?skuIds=J_' + ProductID
            try:
                r = requests.get(json_url_p).text
                time.sleep(1)
                data = json.loads(r)[0]
                price = data['m']
                PreferentialPrice = data['p']
            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout')
                time.sleep(600)
                r = requests.get(json_url_p).text
                time.sleep(1)
                data = json.loads(r)[0]
                price = data['m']
                PreferentialPrice = data['p']

            ##获取评论总数
            json_url_connent= 'https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds=' + ProductID
            try:
                r = requests.get(json_url_connent).text
                time.sleep(1)
                data=json.loads(r)
                data = data['CommentsCount'][0]
                CommentCount=data['CommentCount']
                GoodRateShow=data['GoodRateShow']
                GoodCount = data['GoodCount']
                GeneralCount=data['GeneralCount']
                PoorCount=data['PoorCount']
            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout')
                time.sleep(600)
                r = requests.get(json_url_connent).text
                time.sleep(1)
                data=json.loads(r)
                data = data['CommentsCount'][0]
                CommentCount=data['CommentCount']
                GoodRateShow=data['GoodRateShow']
                GoodCount = data['GoodCount']
                GeneralCount=data['GeneralCount']
                PoorCount=data['PoorCount']

            json_url_keyword= 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0&productId=' + ProductID

            try:
                r = requests.get(json_url_keyword)
                html = r.content.decode('gb2312', 'ignore')
                keywords = re.findall(r',"name":"(.*?)",', html)
                keyword = ' '.join(keywords)

            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout')
                time.sleep(600)
                r = requests.get(json_url_keyword)
                html = r.content.decode('gb2312', 'ignore')
                keywords = re.findall(r',"name":"(.*?)",', html)
                keyword = ' '.join(keywords)

            ##获取商品参数
            product_typ_url="https://item.jd.com/"+ ProductID+".html"
            try:
                r = requests.get(product_typ_url)
                time.sleep(1)
                soup = BeautifulSoup(r.text, 'lxml')
                ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
                ips2 = soup.find_all('div', class_="detail-elevator-floor")
                ips = [ips1, ips2]
                try:
                    for i in ips:
                        type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
                        # control_mode = re.findall(r'<li title=".*?">控制方式：(.*?)<', str(ips))[0]
                        FBnumber = re.findall(r'<li title=".*?">扇叶片数：(.*?)<', str(ips))[0]
                        break
                except IndexError:
                    type = "没有对应数据"
                    print(type)
            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout')
                time.sleep(600)
                r = requests.get(product_typ_url)
                time.sleep(1)
                soup = BeautifulSoup(r.text, 'lxml')
                ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
                ips2 = soup.find_all('div', class_="detail-elevator-floor")
                ips = [ips1, ips2]
                try:
                    for i in ips:
                        type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
                        # control_mode = re.findall(r'<li title=".*?">控制方式：(.*?)<', str(ips))[0]
                        FBnumber = re.findall(r'<li title=".*?">扇叶片数：(.*?)<', str(ips))[0]
                        break
                except IndexError:
                    type = "没有对应数据"
                    print(type)

            # ##item
            item['p_Name'] = p_Name
            item['shop_name'] = shop_name
            item['ProductID'] = ProductID
            item['price'] = price
            item['PreferentialPrice'] = PreferentialPrice

            item['CommentCount']=CommentCount
            item['GoodRateShow']=GoodRateShow
            item['GoodCount']=GoodCount
            item['GeneralCount'] = GeneralCount
            item['PoorCount'] = PoorCount
            item['keyword'] = keyword

            item['type'] = type
            # item['control_mode'] = control_mode
            item['FBnumber'] = FBnumber
            yield item

        donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print("Sleep time start......")
        time.sleep(300)
        print("donetime is:", donetime)


        nextLink = selector.xpath('//*[@id="J_bottomPage"]/span[1]/a[10]/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            yield Request('https://list.jd.com/'+nextLink,callback=self.parse)

