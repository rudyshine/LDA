import requests
import time
import random
import re
import numpy as np
import pandas as pd
import pymongo
import codecs
from scrapy.spiders import CrawlSpider
class jdcrawl(CrawlSpider):
    name ='jdgree'
    allowed_domains=['jd.com']
    def __init__(self,productId, *args, **kwargs):
        super(jdcrawl, self).__init__(*args, **kwargs)
        self.productId=productId
        print(self.productId)
        url1="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456"
        url2="&productId="+self.productId
        url3="&score=0&sortType=5&pageSize=10&isShadowSku=0&page="
        self.start_urls=url1+url2+url3
        # print("=========",self.start_urls)
        ran_num = random.sample(range(0, 5), 5)
        r = requests.get(url=self.start_urls)
        html = r.content

        for i in ran_num:
            i = str(i)
            url = self.start_urls + i
            r = requests.get(url=url)
            html2 = r.content
            html = html + html2
            time.sleep(5)
            print("当前抓取页面:", url, "状态:", r)

        html = str(html, encoding="GBK")

        file = codecs.open("page.txt", "w")
        file.write(html)
        file.close()
        #
        # html = codecs.open('page.txt', 'r').read()



    def getinfor(self):
        print("===============11111111")
        html = codecs.open('page.txt', 'r').read()
        #获取总页数
        maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html)
        # print("maxpage:",maxpage)

        ##提取userClient字段信息
        userClient=re.findall(r',"usefulVoteCount".*?,"userClientShow":(.*?),',html)

        ##提取userLevel字段信息
        userLevel=re.findall(r'"referenceImage".*?,"userLevelName":(.*?),',html)

        #提取productColor字段信息
        productColor=re.findall(r'"creationTime".*?,"productColor":(.*?),',html)

        #提取recommend字段信息
        recommend=re.findall(r'"creationTime".*?,"recommend":(.*?),',html)

        #提取nickname字段信息
        nickname=re.findall(r'"creationTime".*?,"nickname":(.*?),',html)

        #提取userProvince字段信息
        userProvince=re.findall(r'"referenceImage".*?,"userProvince":(.*?),',html)

        #提取usefulVoteCount字段信息
        usefulVoteCount=re.findall(r'"referenceImage".*?,"usefulVoteCount":(.*?),',html)

        ##提取days字段信息
        days=re.findall(r'"usefulVoteCount".*?,"days":(.*?)}',html)

        ##提取score字段信息
        score=re.findall(r'"referenceImage".*?,"score":(.*?),',html)

        ##提取isMobile字段信息
        isMobile=re.findall(r'"usefulVoteCount".*?,"isMobile":(.*?),',html)
        mobile=[]
        for m in isMobile:
            n=m.replace('}','') #替换掉最后的}
            mobile.append(n)

        #提取productSize字段信息
        productSize=re.findall(r'"creationTime".*?,"productSize":(.*?),',html)
        # size=[]
        # for s in productSize:
        #   s1=s[3]
        #   size.append(s1)
        # print(productSize)

        #提取时间字段信息
        creationTime1=re.findall(r'"creationTime":(.*?),"referenceName',html)
        creationTime=[]
        for d in creationTime1:
          date=d[1:20]
          creationTime.append(date)
        print(creationTime)

        hour=[]
        for h in creationTime:
          date=h[10:13]
          hour.append(date)

        #提取评论信息
        content=re.findall(r'"guid".*?,"content":(.*?)","creationTime"',html)
        # 对提取的评论信息进行去重
        content_1=[]
        for i in content:
          if not "img" in i:
              content_1.append(i)