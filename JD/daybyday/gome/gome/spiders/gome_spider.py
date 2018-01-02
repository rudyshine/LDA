import scrapy
import re
import requests
from gome.items import GomeItem
import logging

log_filename="gome_log.txt"

class gome_spider(scrapy.Spider):
    name="gome"
    allowed_domains=["gome.com.cn"]
    start_urls=[
        "http://list.gome.com.cn/cat10000198.html"
    ]


    def parse(self, response):
        sel=scrapy.Selector(response)
        paper =sel.xpath(".//span[@id='min-pager-number']/text()").extract()[0]
        # print(paper)
        paper_start = paper.find('/') + 1
        page = int(paper[paper_start:])  #获取最大页数
        # print (page)
        print ("一共有"+str(page)+"页")
        for i in range(1,page):
            urls="http://list.gome.com.cn/cat10000198.html?&page="+str(i)
            request=scrapy.Request(url=urls,callback=self.update)
            yield request


    def update(self,response):        #每一页内容
        for url in response.xpath(".//li[@class='product-item']"):
            goods_info=url.xpath(".//div[@class='item-tab-warp']/p[@class='item-name']/a/@href").extract()[0]      #商品链接
            preid_start=goods_info.rfind('/')+1
            preid_end=goods_info.rfind('.html')
            preid=goods_info[preid_start:preid_end]
            #print(preid)
            preid_1=preid.split('-')[0]
            preid_2=preid.split('-')[1]

            p_Name=url.xpath(".//div[@class='item-tab-warp']/p[@class='item-name']/a/text()").extract()[0]      #商品名称

            try:         #店铺名称
                shop_name=url.xpath(".//div[@class='item-tab-warp']/p[@class='item-shop']/span[@class='nnamezy']/text()").extract()[0]
                if len(shop_name)==2:
                    shop_name="国美自营"
            except:
                shop_name=url.xpath(".//div[@class='item-tab-warp']/p[@class='item-shop']/a/text()").extract()[0]

            goods_web="http://"+goods_info
            item=GomeItem(p_Name=p_Name,shop_name=shop_name,preid_1=preid_1,preid_2=preid_2)
            request=scrapy.Request(url=goods_web,callback=self.goods,meta={'item':item},dont_filter=True)
            yield request


    def goods(self,response):       #每个商品的内容
        item=response.meta['item']
        preid_1=item['preid_1']
        preid_2=item['preid_2']
        p_Name=item['p_Name']
        shop_name=item['shop_name']
        sel=scrapy.Selector(response)

        info_1=sel.xpath(".//div[@class='prd-firstscreen-left']")   #包含商品编号
        info_2=sel.xpath(".//div[@class='sliderleft']")      #包含商品详情
        info_3=sel.xpath(".//div[@class='product-comment clearfix']")              #包含评价链接

        try:
            product_number_info=info_1.xpath(".//div[@class='toolbar ']/span[@class='product-number']/text()").extract()[0]
            #print (product_number_info)
            product_number=product_number_info.split('：')[-1]            #商品编号
           # print (product_number)
        except:
            product_number="0"

        try:
            product_detail_info=info_2.xpath(".//div[@class='guigecanshu_wrap']/div/text()").extract()
            #print(product_detail_info)
            product_detail_1=[]
            for i in range(len(product_detail_info)):
                product_detail_start=product_detail_info[i].find('：')+1
                product_detail_1.append(product_detail_info[i][product_detail_start:])
            product_detail=' '.join(product_detail_1)           #商品详情
           # print (product_detail)
        except:
            product_detail="none"

        try:
            capacity_info=re.findall("容量：.*<",info_2.extract()[0])[-1]
            capacity_start=capacity_info.find('：')+1
            capacity_end=capacity_info.rfind('<')
            capacity=capacity_info[capacity_start:capacity_end]         #商品容量
            #print (capacity)
        except:
            capacity="none"

        try:
            X_name_info=re.findall(">商品名称：.*<",info_2.extract()[0])[0]
            X_name_start=X_name_info.find('：')+1
            X_name_end=X_name_info.rfind('<')
            X_name=X_name_info[X_name_start:X_name_end]         #商品名称
            #print (capacity)
        except:
            X_name=p_Name

        try:
            type_info=re.findall(">类别：.*<",info_2.extract()[0])[0]
            type_start=type_info.find('：')+1
            type_end=type_info.rfind('<')
            type=type_info[type_start:type_end]         #商品类别
            #print(type)
        except:
            type="none"
        try:
            brand_info=re.findall(">品牌：.*<",info_2.extract()[0])[0]
            brand_start=brand_info.find('：')+1
            brand_end=brand_info.rfind('<')
            brand=brand_info[brand_start:brand_end]         #商品品牌
            #print(brand)
        except:
            brand="none"

        try:
            productid_info=re.findall(">型号：.*<",info_2.extract()[0])[0]
            productid_start=productid_info.find('：')+1
            productid_end=productid_info.rfind('<')
            productid=productid_info[productid_start:productid_end]         #商品型号
            #print(productid)
        except:
            productid="none"

        #comment_url="http://review.gome.com.cn/"+str(preid_1)+"-0-1.html"     #商品评价链接
        comment_urls=info_3.xpath(".//div[@class='clearfix']/a/@href").extract()[0]      #商品评价链接
        comment_url="http:"+comment_urls
        item = GomeItem(p_Name=p_Name, shop_name=shop_name, preid_1=preid_1, preid_2=preid_2, \
                               product_number=product_number, product_detail=product_detail, \
                               capacity=capacity, type=type, brand=brand, productid=productid,X_name=X_name)
        request = scrapy.Request(url=comment_url, callback=self.goods_comment_price, meta={'item': item}, dont_filter=True)
        yield request

    def goods_comment_price(self,response):
        item=response.meta['item']
        p_Name=item['p_Name']
        shop_name=item['shop_name']
        preid_1=item['preid_1']
        preid_2=item['preid_2']
        product_number=item['product_number']
        product_detail=item['product_detail']
        capacity=item['capacity']
        type=item['type']
        brand=item['brand']
        productid=item['productid']
        X_name=item['X_name']
        comment_web=response.xpath(".//div[@class='adv-main']")
        try:
            comment_num=comment_web.xpath(".//div[@class='adv-tlayer']/span[@class='adv-prdcount']/strong/text()").extract()[0]
            if int(comment_num)==0:          #好评率
                GoodRateShow="none"
            else:
                GoodRateShow=comment_web.xpath(".//div[@class='adv-goods']/div[@class='adv-gdsper']/span/text()").extract()[0]
        except:
            GoodRateShow="None"

        try:         #评论关键词
            comment_info=comment_web.xpath(".//div[@class='adv-recommend']/div[@class='w-recommend']/span/text()").extract()
            keyword=' '.join(comment_info)
        except:
            keyword="none"


        commentcount_url="http://ss.gome.com.cn/item/v1/prdevajsonp/appraiseNew/"+str(preid_1)+"/1/all/0/10/flag/appraise"  #商品评论数链接
        price_url="http://ss.gome.com.cn/item/v1/d/m/store/unite/"+str(preid_1)+"/"+str(preid_2)+"/N/31180100/311801001/1/null/flag/item"   #商品价格链接

        commentcount_web=requests.get(commentcount_url).text
        try:
            bad_info=re.findall('"bad":\d+',commentcount_web)[0]
            PoorCount=bad_info.split(':')[-1]           #差评数
        except:
            PoorCount="0"
        try:
            good_info=re.findall('"good":\d+',commentcount_web)[0]
            GoodCount=good_info.split(':')[-1]          #好评数
        except:
            GoodCount="0"
        try:
            mid_info=re.findall('"mid":\d+',commentcount_web)[0]
            GeneralCount=mid_info.split(':')[-1]        #中评数
        except:
            GeneralCount="0"
        try:
            total_info=re.findall('"totalCount":\d+',commentcount_web)[0]
            CommentCount=total_info.split(':')[-1]     #评论总数
        except:
            CommentCount="0"

        price_web = requests.get(price_url).text
        price_info = re.findall('"salePrice":".*?"', price_web)[0]
        price_1 = price_info.split(':')[-1]
        price_start = price_1.find('\"') + 1
        price_end = price_1.rfind('\"')
        price = price_1[price_start:price_end]         #价格
        PreferentialPrice=price[:]

        X_type="none"

        item = GomeItem(p_Name=p_Name, shop_name=shop_name, preid_1=preid_1, preid_2=preid_2, \
                        ProductID=product_number, X_name=X_name, \
                        capacity=capacity, type=product_detail, brand=brand, productid=productid, \
                        GoodRateShow=GoodRateShow,keyword=keyword,PoorCount=PoorCount,\
                        GoodCount=GoodCount,GeneralCount=GeneralCount,CommentCount=CommentCount,\
                        price=price,PreferentialPrice=PreferentialPrice,X_type=X_type)
        yield item










