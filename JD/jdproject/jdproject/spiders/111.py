
import requests
import time
import random
import re
import numpy as np
import pandas as pd
import pymongo
import codecs

def gethtml(self):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Connection': 'close',
        'Referer': 'https://www.jd.com/'
    }

    cookie = {
        '_jda': '122270672.2082744608.1490836927.1491443901.1491447607.20',
        '__jdb': '122270672.6.2082744608|20.1491447607',
        '__jdc': '122270672',
        '__jdu': '2082744608',
        '__jdv': '122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d0494d40ca3242e2b57611255d334b6d|1491447607413',
        'ipLoc-djd': '1-72-2799-0',
        'ipLocation': '%u5317%u4EAC',
        'unpl': 'V2_ZzNtbRdWRh1wXUNVKUleBmIARl4RU0USdQhFUH9MXgdiUBUIclRCFXMUR1FnGFwUZwMZXUpcRxNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3oQXwNiBhVcS2dzEkU4dlB%2fEVoMZDMTbUNnAUEpAEdUcxFbSGQCG15EUkYSdAF2VUsa',
        'user-key': 'c4a237ca-dae8-403e-9cec-ad4d0c1470da'}

    url1 = self.start_urls
    ran_num = random.sample(range(0, 200), 200)
    r = requests.get(url=url1, headers=headers, cookies=cookie)
    html = r.content

    for i in ran_num:
        i = str(i)
        url = url1 + i
        r = requests.get(url=url, headers=headers, cookies=cookie)
        html2 = r.content
        html = html + html2
        time.sleep(5)
        print("当前抓取页面:", url, "状态:", r)

    html = str(html, encoding="GBK")

    file = codecs.open("page.txt", "w")
    file.write(html)
    file.close()

    html = codecs.open('page.txt', 'r').read()
    return html



    def getinfor(self):
        print("===============11111111")
        # html = codecs.open('page.txt', 'r').read()
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

if __name__ == '__main__':
    print("gethtml")
    gethtml(self)


