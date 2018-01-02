# - * - coding: utf-8 - * -
##爬虫程序
from scrapy.spiders import CrawlSpider
from JDSpider.items import JdspiderItem
from scrapy.selector import Selector
from scrapy.http import Request
from bs4 import BeautifulSoup
import time
import requests
import re, json

class JdSpider(CrawlSpider):
    name = "JDSpider"
    redis_key = "JDSpider:start_urls"
    start_urls = [
        "https://list.jd.com/list.html?cat=737,738,751",##电风扇
        "https://list.jd.com//list.html?cat=737,738,751&page=32&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main",##风扇（品牌）
        # "https://list.jd.com/list.html?cat=737,738,1278",##冷风扇
        # "https://list.jd.com/list.html?cat=737,738,1278&ev=exbrand_18136%7C%7C7420%7C%7C12380%7C%7C3659%7C%7C3085"##冷风扇（品牌）
        # "https://list.jd.com/list.html?cat=737,752,13116",##源汁机
        # "https://list.jd.com/list.html?cat=737,752,13116&page=7&sort=sort_rank_asc&trans=1&JL=6_0_0"
        # "https://list.jd.com/list.html?cat=737,738,745",##吸尘器
        # "https://list.jd.com/list.html?cat=737,738,745&page=14&sort=sort_rank_asc&trans=1&JL=6_0_0"##吸尘器
        ]

    def parse(self, response):
        item = JdspiderItem()
        selector = Selector(response)
        Products = selector.xpath('//*[@id="plist"]/ul/li')
        for each in Products:
            p_Name = each.xpath('div/div[@class="p-name"]/a/em/text()').extract()[0]
            temphref = each.xpath('div/div[@class="p-img"]/a/@href').extract()
            temphref = str(temphref)
            ProductID = str(re.search('com/(.*?)\.html',temphref).group(1))
            # ProductID='1959718783'
            ##获取价格
            json_url_p = 'http://p.3.cn/prices/mgets?skuIds=J_' + ProductID
            try:
                data = requests.get(json_url_p,timeout = 1000).json()[0]
                price = data['m']
                PreferentialPrice = data['p']
            except requests.exceptions.ConnectionError:  #requests.exceptions.ReadTimeout
                print('Timeout ConnectionError1:json_url_p')
                time.sleep(600)
                try:
                    data = requests.get(json_url_p, timeout=1000).json()[0]
                    price = data['m']
                    PreferentialPrice = data['p']
                except requests.exceptions.ConnectionError:
                    print('Timeout ConnectionError2:json_url_p')
                    time.sleep(3600)
                    data = requests.get(json_url_p, timeout=1000).json()[0]
                    price = data['m']
                    PreferentialPrice = data['p']
                except requests.exceptions.ReadTimeout:
                    print('Timeout,ReadTimeout:',json_url_p)
            except requests.exceptions.ReadTimeout:
                print('Timeout,ReadTimeout:',json_url_p)



            ##获取评论总数
            json_url_connent= 'https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds=' + ProductID
            try:
                data = requests.get(json_url_connent,timeout = 1000).json()
                data = data['CommentsCount'][0]
                CommentCount=data['CommentCount']
                GoodRateShow=data['GoodRateShow']
                GoodCount = data['GoodCount']
                GeneralCount=data['GeneralCount']
                PoorCount=data['PoorCount']
            except requests.exceptions.ConnectionError:
                print('Timeout ConnectionError1:json_url_connent')
                time.sleep(600)
                try:
                    data = requests.get(json_url_connent,timeout = 1000).json()
                    data = data['CommentsCount'][0]
                    CommentCount = data['CommentCount']
                    GoodRateShow = data['GoodRateShow']
                    GoodCount = data['GoodCount']
                    GeneralCount = data['GeneralCount']
                    PoorCount = data['PoorCount']
                except requests.exceptions.ConnectionError:
                    print('Timeout ConnectionError2:json_url_connent')
                    time.sleep(3600)
                    data = requests.get(json_url_connent, timeout=1000).json()
                    data = data['CommentsCount'][0]
                    CommentCount = data['CommentCount']
                    GoodRateShow = data['GoodRateShow']
                    GoodCount = data['GoodCount']
                    GeneralCount = data['GeneralCount']
                    PoorCount = data['PoorCount']
                except requests.exceptions.ReadTimeout:
                    print('Timeout,ReadTimeout:',json_url_connent)
            except requests.exceptions.ReadTimeout:
                print('Timeout,ReadTimeout:',json_url_connent)

            ##获取商品评论关键字
            json_url_keyword= 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0&productId=' + ProductID
            # r = requests.get(json_url_keyword,timeout = 100)
            # time.sleep(2)
            # html = r.content.decode('gb2312', 'ignore')
            # keywords = re.findall(r',"name":"(.*?)",', html)
            # keyword = ' '.join(keywords)

            try:
                r = requests.get(json_url_keyword,timeout = 1000)
                html = r.content.decode('gb2312', 'ignore')
                keywords = re.findall(r',"name":"(.*?)",', html)
                keyword = ' '.join(keywords)
            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout ConnectionError1:json_url_keyword')
                time.sleep(600)
                try:
                    r = requests.get(json_url_keyword,timeout = 1000)
                    html = r.content.decode('gb2312', 'ignore')
                    keywords = re.findall(r',"name":"(.*?)",', html)
                    keyword = ' '.join(keywords)
                except requests.exceptions.ConnectionError:  # this is important
                    print('Timeout ConnectionError2:json_url_keyword')
                    time.sleep(3600)
                    r = requests.get(json_url_keyword,timeout = 1000)
                    html = r.content.decode('gb2312', 'ignore')
                    keywords = re.findall(r',"name":"(.*?)",', html)
                    keyword = ' '.join(keywords)
                except requests.exceptions.ReadTimeout:
                    print('Timeout,ReadTimeout:', json_url_keyword)
            except requests.exceptions.ReadTimeout:
                print('Timeout,ReadTimeout:', json_url_keyword)

            # ##获取商品参数 (冷风扇)
            # product_typ_url="https://item.jd.com/"+ ProductID+".html"
            # r = requests.get(product_typ_url,timeout = 100)
            # time.sleep(2)
            # soup = BeautifulSoup(r.text, 'lxml')
            # ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
            # ips2 = soup.find_all('div', class_="detail-elevator-floor")
            # ips = [ips1, ips2]
            # try:
            #     for i in ips:
            #         type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
            #         break
            # except IndexError:
            #     type = "没有对应数据"
            #     print(type)
            ##获取商品参数 (原汁)
            product_typ_url="https://item.jd.com/"+ ProductID+".html"
            try:
                r = requests.get(product_typ_url,timeout = 1000)
                soup = BeautifulSoup(r.text, 'lxml')
                try:
                    shop_name = re.findall(r'<a clstag=".*?" href=".*?" target="_blank" title="(.*?)">', str(soup))[0]
                except IndexError:
                    shop_name = "none"
                try:
                    brand = soup.find_all('ul', id="parameter-brand")
                    brand = re.findall(r'<li title="(.*?)"', str(brand))[0]
                except IndexError:
                    brand = "None"
                ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
                ips2 = soup.find_all('div', class_="detail-elevator-floor")
                ips = [ips1, ips2]
                for i in ips:
                    type= re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
                    try:
                        X_type = re.findall(r'<li title=".*?">.*?吸头：(.*?)<', str(ips))[0]
                    except IndexError:
                        X_type = "none"
                    try:
                        F_type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
                    except IndexError:
                        F_type= "none"
                    try:
                        Y_type = re.findall(r'<li title=".*?">类型：(.*?)<', str(ips))[0]
                    except IndexError:
                        Y_type= "none"
            except requests.exceptions.ConnectionError:  # this is important
                print('Timeout ConnectionError1:product_typ_url')
                time.sleep(600)
                try:
                    r = requests.get(product_typ_url,timeout = 1000)
                    soup = BeautifulSoup(r.text, 'lxml')
                    try:
                        shop_name = re.findall(r'<a clstag=".*?" href=".*?" target="_blank" title="(.*?)">', str(soup))[0]
                    except IndexError:
                        shop_name = "none"
                    try:
                        brand = soup.find_all('ul', id="parameter-brand")
                        brand = re.findall(r'<li title="(.*?)"', str(brand))[0]

                    except IndexError:
                        brand = "None"
                    ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
                    ips2 = soup.find_all('div', class_="detail-elevator-floor")
                    ips = [ips1, ips2]
                    for i in ips:
                        type = re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
                        try:
                            X_type = re.findall(r'<li title=".*?">.*?吸头：(.*?)<', str(ips))[0]
                        except IndexError:
                            X_type = "none"
                        try:
                            F_type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
                        except IndexError:
                            F_type = "none"
                        try:
                            Y_type = re.findall(r'<li title=".*?">类型：(.*?)<', str(ips))[0]
                        except IndexError:
                            Y_type = "none"
                except requests.exceptions.ConnectionError:  # this is important
                    print('Timeout ConnectionError2:product_typ_url')
                    time.sleep(3600)
                    r = requests.get(product_typ_url,timeout = 1000)
                    soup = BeautifulSoup(r.text, 'lxml')
                    try:
                        shop_name = re.findall(r'<a clstag=".*?" href=".*?" target="_blank" title="(.*?)">', str(soup))[
                            0]
                    except IndexError:
                        shop_name = "none"
                    try:
                        brand = soup.find_all('ul', id="parameter-brand")
                        brand = re.findall(r'<li title="(.*?)"', str(brand))[0]
                    except IndexError:
                        brand = "None"
                    ips1 = soup.find_all('ul', class_="parameter2 p-parameter-list")
                    ips2 = soup.find_all('div', class_="detail-elevator-floor")
                    ips = [ips1, ips2]
                    for i in ips:
                        type = re.findall(r'<li title=".*?">.*?：(.*?)<', str(ips))
                        try:
                            X_type = re.findall(r'<li title=".*?">.*?吸头：(.*?)<', str(ips))[0]
                        except IndexError:
                            X_type = "none"
                        try:
                            F_type = re.findall(r'<li title=".*?">类别：(.*?)<', str(ips))[0]
                        except IndexError:
                            F_type = "none"
                        try:
                            Y_type = re.findall(r'<li title=".*?">类型：(.*?)<', str(ips))[0]
                        except IndexError:
                            Y_type = "none"
                except requests.exceptions.ReadTimeout:
                    print('Timeout,ReadTimeout:', product_typ_url)
            except requests.exceptions.ReadTimeout:
                print('Timeout,ReadTimeout:', product_typ_url)

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

            item['brand'] = brand
            item['type'] = type
            item['X_type'] = X_type
            item['F_type'] = F_type
            item['Y_type'] = Y_type
            yield item

        # donetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # print("Sleep time start......")
        # time.sleep(5)
        # print("donetime is:", donetime)


        nextLink = selector.xpath('//*[@id="J_bottomPage"]/span[1]/a[10]/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            # print("start nextLink is "+nextLink)
            yield Request('https://list.jd.com/'+nextLink,callback=self.parse)
