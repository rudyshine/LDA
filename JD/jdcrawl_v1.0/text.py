# -*-utf8-*-
import requests
import time
import random
import re
import numpy as np
import pandas as pd
import pymongo
import codecs
from bs4 import BeautifulSoup
from urllib import request

#设置请求中头文件的信息
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.jd.com/'}

cookie={
'_jda':'122270672.2082744608.1490836927.1491443901.1491447607.20',
'__jdb':'122270672.6.2082744608|20.1491447607',
'__jdc':'122270672',
'__jdu':'2082744608',
'__jdv':'122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d0494d40ca3242e2b57611255d334b6d|1491447607413',
'ipLoc-djd':'1-72-2799-0',
'ipLocation':'%u5317%u4EAC',
'unpl':'V2_ZzNtbRdWRh1wXUNVKUleBmIARl4RU0USdQhFUH9MXgdiUBUIclRCFXMUR1FnGFwUZwMZXUpcRxNFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3oQXwNiBhVcS2dzEkU4dlB%2fEVoMZDMTbUNnAUEpAEdUcxFbSGQCG15EUkYSdAF2VUsa',
'user-key':'c4a237ca-dae8-403e-9cec-ad4d0c1470da'}

# url="https://sale.jd.com/act/GrZjoT7UQWCn.html"
# url2 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId="
# url3="&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0"
# url4="&score=0&sortType=5&pageSize=10&isShadowSku=0&page="

# def getproductId():



def getmaxpage(url0):
    r=requests.get(url=url0,headers=headers,cookies=cookie)
    html0=r.content.decode('gb2312','ignore')
    html0=str(html0)
    file = codecs.open(productId+"page.txt", "w")
    file.write(html0)
    file.close()
    html0 = codecs.open(productId+'page.txt', 'r').read()
    maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html0)
    # referenceId=re.findall(r',"isTop".*?,"referenceId":(.*?),', html0)
    if maxpage==['0']:
        print("这个产品没有用户进行评论")
        return 0
    else:
        sumpage = maxpage.pop()
        return sumpage

def crawlpage(ran_num,url1):
    r = requests.get(url=url1, headers=headers, cookies=cookie)
    html = r.content.decode('gb2312', 'ignore')
    for i in ran_num:
        i = str(i)
        url = url1 + i
        r = requests.get(url=url, headers=headers, cookies=cookie)
        html2 = r.content.decode('gb2312', 'ignore')
        html = html + html2
        time.sleep(5)
        print("当前抓取页面:", url, "状态:", r)
    html = str(html)
    # 写入文件
    html = str(html)
    file = codecs.open(productId+"page.txt", "w")
    file.write(html)
    file.close()

    html = codecs.open(productId+"page.txt", 'r').read()
    userClient = re.findall(r',"referenceImage".*?,"userClientShow":(.*?),', html)
    userLevel = re.findall(r'"referenceImage".*?,"userLevelName":(.*?),', html)
    productColor = re.findall(r'"creationTime".*?,"productColor":(.*?),', html)
    recommend = re.findall(r'"creationTime".*?,"recommend":(.*?),', html)
    nickname = re.findall(r'"creationTime".*?,"nickname":(.*?),', html)
    userProvince = re.findall(r'"referenceImage".*?,"userProvince":(.*?),', html)
    usefulVoteCount = re.findall(r'"referenceImage".*?,"usefulVoteCount":(.*?),', html)
    days = re.findall(r'"usefulVoteCount".*?,"days":(.*?)}', html)
    score = re.findall(r'"referenceImage".*?,"score":(.*?),', html)
    isMobile = re.findall(r'"usefulVoteCount".*?,"isMobile":(.*?),', html)
    mobile = []
    for m in isMobile:
        n = m.replace('}', '')  # 替换掉最后的}
        mobile.append(n)
    productSize = re.findall(r'"creationTime".*?,"productSize":(.*?),', html)
    creationTime1 = re.findall(r'"creationTime":(.*?),"referenceName', html)
    creationTime = []
    for d in creationTime1:
        date = d[1:20]
        creationTime.append(date)
    hour = []
    for h in creationTime:
        date = h[10:13]
        hour.append(date)
    content = re.findall(r'"guid".*?,"content":(.*?)","creationTime"', html)
    content_1 = []
    for i in content:
        if not "img" in i:
            content_1.append(i)

    # 将前面提取的各字段信息汇总为table数据表，以便后面分析
    table = pd.DataFrame({'creationTime': creationTime,'hour': hour, 'nickname': nickname,
                          'productColor': productColor, 'productSize': productSize,
                          'recommend': recommend, 'mobile': mobile, 'userClient': userClient,
                          'userLevel': userLevel, 'userProvince': userProvince,
                          'usefulVoteCount': usefulVoteCount, 'content_1': content_1,
                          'days': days, 'score': score})
    table['creationTime'] = pd.to_datetime(table['creationTime'])
    table = table.set_index('creationTime')
    table['days'] = table['days'].astype(np.str)
    table.head()
    print("存入csv....")
    # table.to_csv('jd_table_textmaxpage.csv')
    table.to_csv(productId+'jd_table.csv', mode='a', header=False)
    print("存完....")

    # 数据存入momgodb
    print("开始连接数据库：")
    client = pymongo.MongoClient('localhost', 27017)
    rent_info = client['jd_table']  # 给数据库命名
    sheet_table = rent_info[productId+'jd_table']  # 创建表单
    sheet_table.insert({'creationTime': creationTime,'hour': hour, 'nickname': nickname,
                        'productColor': productColor, 'productSize': productSize,
                        'recommend': recommend, 'mobile': mobile, 'userClient': userClient,
                        'userLevel': userLevel, 'userProvince': userProvince,
                        'usefulVoteCount': usefulVoteCount, 'content_1': content_1,
                        'days': days, 'score': score})
    print("done......")

def getnum(sumpage,url1):
    n=100
    # b=getmaxpage
    if int(sumpage)>=n:
        m=int(sumpage)//n
        ran_num = range(int(sumpage))
        for i in range(m):
            s = set(ran_num)
            ran1 = random.sample(ran_num, n)
            s1 = set(ran1)
            crawlpage(ran1,url1)
            print("sleep time start...")
            time.sleep(240)
            print("sleep time done...")
            s2 = s - s1
            ran_num = list(s2)
        ran_num = random.sample(ran_num,len(ran_num))
        crawlpage(ran_num,url1)
    else:
        ran_num0 =random.sample(range(0,int(sumpage)), int(sumpage))
        crawlpage(ran_num0,url1)



# if __name__=='__main__':
#     startime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print("startime is:", startime)
#     url = "https://sale.jd.com/act/GrZjoT7UQWCn.html"
#     url2 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId="
#     url3 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0"
#     url4 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page="
#     html = request.urlopen(url).read()
#     soup = BeautifulSoup(html, "lxml")
# 
#     for skuid in soup.find_all('li'):
#         Id = skuid.get('skuid')
#         if Id != None:
#             Id = str.split(Id)
#             productId = ''.join(Id)
#             for i in range(0, len(Id)):
#                 productId = ''.join(Id)
#                 url0 = url2 + productId + url3
#                 print("url0:", url0)
#                 url1 = url2 + productId + url4
#                 print("url1:", url1)
#                 time.sleep(60)
# 
#                 n=getmaxpage(url0)
#                 if n!=0:
#                     getnum(n,url1)
#                 endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#                 print("endtime is:",endtime)
#                 time.sleep(1800)

if __name__ == '__main__':
    startime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("startime is:", startime)
    url = "https://sale.jd.com/act/GrZjoT7UQWCn.html"
    url2 = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId="
    url3 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page=0"
    url4 = "&score=0&sortType=5&pageSize=10&isShadowSku=0&page="
    productId =str(1993089)
    print(productId)
    url0 = url2 + productId + url3
    print("url0:", url0)
    url1 = url2 + productId + url4
    print("url1:", url1)
    n = getmaxpage(url0)
    if n != 0:
        getnum(n, url1)
    endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("endtime is:", endtime)
    time.sleep(1800)
    #