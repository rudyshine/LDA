import scrapy
from bs4 import BeautifulSoup
import requests
import re
import json
from jdtest.items import JdtestItem
import time

class jdspider(scrapy.Spider):
    name="jdtest"
    allowed_domains=["jd.com"]
    start_urls=[
        "https://list.jd.com/list.html?cat=737,794,870&ev=1554_584893&JL=3_%E7%A9%BA%E8%B0%83%E7%B1%BB%E5%88%AB_%E5%A3%81%E6%8C%82%E5%BC%8F%E7%A9%BA%E8%B0%83#J_crumbsBar"   #壁挂式空调
    ]

    def parse(self, response):
        sel=scrapy.Selector(response)
        goods_info=sel.xpath(".//div[@id='plist']/ul/li")
        for goods in goods_info:
            ProductID=goods.xpath(".//div[@class='gl-i-wrap j-sku-item']/@data-sku").extract()[0]       #商品编号
            if len(ProductID)!=0:
                goods_web="https://item.jd.com/"+str(ProductID)+".html"         #商品链接   包含商品型号,店铺名称,类别,品牌,型号等
                item=JdtestItem(ProductID=ProductID)
                request=scrapy.Request(url=goods_web,callback=self.goods,meta={'item':item},dont_filter=True)
                yield request
            else:
                print("parse中ProductID为空  没有读到")

        #翻页功能
        next_page=sel.xpath(".//div[@class='p-wrap']/span[@class='p-num']/a[@class='pn-next']/@href").extract()
        if next_page:
            next="https://list.jd.com/"+next_page[0]
            yield scrapy.Request(next,callback=self.parse)

    def goods(self,response):
        item=response.meta['item']
        sel=scrapy.Selector(response)
        ProductID=item['ProductID']
        PreferentialPrice="0"
        if len(ProductID)!=0:
            try:
                shop_name=sel.xpath(".//div[@class='name']/a/text()").extract()[0]       #店铺名称
            except:
                shop_name="京东自营"

            try:
                p_Name=sel.xpath(".//div[@class='sku-name']/text()").extract()[0].strip('\"').strip('\n').strip().replace('\t','')    #商品名称
                if len(p_Name)==0:
                    p_Name = sel.xpath(".//div[@class='item ellipsis']/@title").extract()[0].replace('\t','')
            except:
                try:
                    p_Name=sel.xpath(".//div[@class='item ellipsis']/@title").extract()[0].replace('\t','')
                except:
                    p_Name=None

            detail_info = sel.xpath(".//div[@class='p-parameter']")  # 包含商品详情内容
            detail = detail_info.xpath(".//li/@title").extract()
            product_detail = ' '.join(detail).replace('\t', '')

            try:
                brand=detail_info.xpath(".//ul[@id='parameter-brand']/li/a/text()").extract()[0].strip()    #商品品牌
            except:
                try:
                    brand=sel.xpath(".//div[@class='inner border']/div[@class='head']/a/text()").extract()[0].strip()
                except:
                    brand=None

            if ("（" and "）") in brand:
                dd=re.findall("（.*?）",brand)[0]
                brand=brand.replace(dd,'').replace(' ','')

            if brand=="Panasonic":
                brand="松下"
            if brand=="CHEBLO":
                brand="樱花"
            if brand=="MBO":
                brand="美博"
            if brand=="YAIR":
                brand="扬子"
            if brand=="PHLGCO":
                brand="飞歌"
            if brand=="FZM":
                brand="方米"
            if brand=="inyan":
                brand="迎燕"
            if brand=="JENSANY":
                brand="金三洋"

            detail_1=detail_info.extract()
            try:
                name_info=re.findall(">商品名称：.*?<",detail_1[0])      #商品名称
                X_name=name_info[0][6:-1].strip().replace('\t','')
                if len(X_name)==0:
                    X_name=p_Name
                if p_Name==None:
                    p_Name=X_name
            except:
                X_name=p_Name
            try:
                type_info = re.findall('>变频/定频：.*?<', detail_1[0])  # 类别（定变频）
                X_type = type_info[0][7:-1].strip()
            except:
                X_type=None

            try:
                capacity_info = re.findall('>商品匹数：.*?<', detail_1[0])  # 商品容量（匹数）
                capacity = capacity_info[0][6:-1].strip()
            except:
                try:
                    capacity_sel=sel.xpath(".//div[@class='Ptable']/div[2]/dl/dd[2]/text()").extract()[0]
                    if (len(capacity_sel)>5):
                        capacity_sel=sel.xpath(".//div[@class='Ptable']/div[2]/dl/dd[3]/text()").extract()[0]
                    if "匹" in str(capacity_sel):
                        capacity=capacity_sel
                    else:
                        capacity=None
                except:
                    capacity=None

            # 商品评价链接   json格式
            comment_web = "https://sclub.jd.com/comment/productPageComments.action?productId=" + str(ProductID) + "&score=0&sortType=5&page=0&pageSize=10"
            # comment_web="https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds="+str(ProductID)
            try:
                comment_webs = requests.get(comment_web,timeout=1000).text
                urls = json.loads(comment_webs)
                try:
                    comment = urls['hotCommentTagStatistics']
                    keyword_list = []
                    for i in range(len(comment)):
                        keyword_list.append(comment[i]['name'])
                    if len(keyword_list)==0:
                        keyword=None
                    else:
                        keyword = ' '.join(keyword_list)                 #关键词
                except IndexError:
                    keyword=None

                rate = urls['productCommentSummary']
                try:
                    CommentCount = rate['commentCount']  # 评论总数
                except IndexError:
                    CommentCount=None
                    print("评价总数",CommentCount)
                try:
                    GoodRateShow = rate['goodRateShow']  # 好评率
                except IndexError:
                    GoodRateShow=None
                    print("好评率:",GoodRateShow)
                try:
                    GoodCount = rate['goodCount']  # 好评数
                except IndexError:
                    GoodCount=None
                    print("好评数:",GoodCount)
                try:
                    GeneralCount = rate['generalCount']  # 中评数
                except IndexError:
                    GeneralCount =None
                    print("中评数:",GeneralCount)
                try:
                    PoorCount = rate['poorCount']  # 差评数
                except IndexError:
                    PoorCount=None
                    print("差评数:",PoorCount)
            except:
                time.sleep(600)
                try:
                    comment_webs = requests.get(comment_web, timeout=1000).text
                    urls = json.loads(comment_webs)
                    try:
                        comment = urls['hotCommentTagStatistics']
                        keyword_list = []
                        for i in range(len(comment)):
                            keyword_list.append(comment[i]['name'])
                        keyword = ' '.join(keyword_list)  # 关键词
                    except:
                        keyword = None

                    rate = urls['productCommentSummary']
                    try:
                        CommentCount = rate['commentCount']  # 评论总数
                    except:
                        print("评论:",comment_web)
                        CommentCount = None
                    try:
                        GoodRateShow = rate['goodRateShow']  # 好评率
                    except:
                        GoodRateShow = None
                        print("except中好评率：",GoodRateShow)
                    try:
                        GoodCount = rate['goodCount']  # 好评数
                    except:
                        GoodCount =None
                    try:
                        GeneralCount = rate['generalCount']  # 中评数
                    except:
                        GeneralCount = None
                    try:
                        PoorCount = rate['poorCount']  # 差评数
                    except:
                        PoorCount =None
                except:
                    time.sleep(1800)
                    try:
                        comment_webs = requests.get(comment_web, timeout=3000).text
                        urls = json.loads(comment_webs)
                        try:
                            comment = urls['hotCommentTagStatistics']
                            keyword_list = []
                            for i in range(len(comment)):
                                keyword_list.append(comment[i]['name'])
                            keyword = ' '.join(keyword_list)  # 关键词
                        except:
                            keyword = None

                        rate = urls['productCommentSummary']
                        try:
                            CommentCount = rate['commentCount']  # 评论总数
                        except:
                            print("评论:", comment_web)
                            CommentCount = None
                        try:
                            GoodRateShow = rate['goodRateShow']  # 好评率
                        except:
                            GoodRateShow = None
                            print("except中好评率：", GoodRateShow)
                        try:
                            GoodCount = rate['goodCount']  # 好评数
                        except:
                            GoodCount = None
                        try:
                            GeneralCount = rate['generalCount']  # 中评数
                        except:
                            GeneralCount = None
                        try:
                            PoorCount = rate['poorCount']  # 差评数
                        except:
                            PoorCount = None
                    except:
                        print("连接失败：",comment_web)


            # price_web="https://p.3.cn/prices/mgets?pduid=1508741337887922929012&skuIds=J_"+str(ProductID)
            price_web="https://p.3.cn/prices/mgets?ext=11000000&pin=&type=1&area=1_72_4137_0&skuIds=J_"+str(ProductID)+"&pdbp=0&pdtk=vJSo%2BcN%2B1Ot1ULpZg6kb4jfma6jcULJ1G2ulutvvlxgL3fj5JLFWweQbLYhUVX2E&pdpin=&pduid=1508741337887922929012&source=list_pc_front&_=1510210566056"
            try:
                price_webs = requests.get(price_web,timeout=1000).text
                price_json = json.loads(price_webs)[0]
                try:
                   price = price_json['m']
                except:
                   price_info = re.findall('\"p\":\".*?\"', str(price_webs))
                   price = price_info[0][5:-1]
                try:
                   PreferentialPrice = price_json['p']
                except:
                    PreferentialPrice=price             #商品价格
            except:
                time.sleep(600)
                try:
                    price_webs = requests.get(price_web,timeout=1000).text
                    price_json = json.loads(price_webs)[0]
                    try:
                        PreferentialPrice = price_json['p']
                    except:
                        try:
                            PreferentialPrice_info = re.findall('\"p\":\".*?\"', str(price_webs))
                            PreferentialPrice = PreferentialPrice_info[0][5:-1]
                        except:
                            PreferentialPrice=None
                    try:
                        price = price_json['m']
                    except:
                        try:
                           price_info = re.findall('\"m\":\".*?\"', str(price_webs))
                           price = price_info[0][5:-1]
                        except:
                            price=PreferentialPrice
                except:
                    time.sleep(1800)
                    try:
                        price_webs = requests.get(price_web,timeout=3000).text
                        price_json = json.loads(price_webs)[0]
                        try:
                            PreferentialPrice = price_json['p']
                        except:
                            try:
                                PreferentialPrice_info = re.findall('\"p\":\".*?\"', str(price_webs))
                                PreferentialPrice = PreferentialPrice_info[0][5:-1]
                            except:
                                PreferentialPrice=None
                        try:
                            price = price_json['m']
                        except:
                            try:
                               price_info = re.findall('\"m\":\".*?\"', str(price_webs))
                               price = price_info[0][5:-1]
                            except:
                                price=PreferentialPrice
                    except:
                        print("连接失败：",price_web)

            if PreferentialPrice==None:
                item = JdtestItem()
                item['ProductID']=ProductID
                item['p_Name']=p_Name
                item['shop_name']=shop_name
                item['price']=price
                item['PreferentialPrice']=PreferentialPrice
                item['CommentCount']=CommentCount
                item['GoodRateShow']=GoodRateShow
                item['GoodCount']=GoodCount
                item['GeneralCount']=GeneralCount
                item['PoorCount']=PoorCount
                item['keyword']=keyword
                item['type']=product_detail
                item['brand']=brand
                item['X_type']=X_type
                item['X_name']=X_name
                item['capacity']=capacity
                item['source']="京东"
                yield item

            elif float(PreferentialPrice)>300.00:
                item = JdtestItem()
                item['ProductID']=ProductID
                item['p_Name']=p_Name
                item['shop_name']=shop_name
                item['price']=price
                item['PreferentialPrice']=PreferentialPrice
                item['CommentCount']=CommentCount
                item['GoodRateShow']=GoodRateShow
                item['GoodCount']=GoodCount
                item['GeneralCount']=GeneralCount
                item['PoorCount']=PoorCount
                item['keyword']=keyword
                item['type']=product_detail
                item['brand']=brand
                item['X_type']=X_type
                item['X_name']=X_name
                item['capacity']=capacity
                item['source']="京东"
                yield item
            else:
                print("广告及无效页面:","https://item.jd.com/"+str(ProductID)+".html")
        else:
            print ("goods中ProductID未找到  没有传进去")

