#导入requests库(请求和页面抓取)
import requests
#导入time库(设置抓取Sleep时间)
import time
#导入random库(生成乱序随机数)
import random
#导入正则库(从页面代码中提取信息)
import re
#导入数值计算库(常规计算)
import pymongo
import numpy as np
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入绘制图表库(数据可视化)
import matplotlib.pyplot as plt
#导入结巴分词库(分词)
import jieba as jb
#导入结巴分词(关键词提取)
import jieba.analyse
#中文转码
import codecs

startime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("startime is:",startime)

#设置请求中头文件的信息
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Connection':'close',
'Referer':'https://www.jd.com/'
}

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

#设置URL的第一部分
#url1='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv79456&productId=3312037&score=0&sortType=5&pageSize=10&isShadowSku=0&page='
url1="https://club.jd.com/comment/productPageComments.action?callback=" \
     "fetchJSON_comment98vv79456&productId=1993092&score=0&sortType=5&" \
     "pageSize=10&isShadowSku=0&page="

##首页等于0



ran_num=random.sample(range(200,201),1)
r=requests.get(url=url1,headers=headers,cookies=cookie)
html=r.content

for i in ran_num:
      i=str(i)
      url=url1+i
      r=requests.get(url=url,headers=headers,cookies=cookie)
      html2=r.content
      html = html + html2
      time.sleep(5)
      print("当前抓取页面:",url,"状态:",r)

#对抓取的页面进行编码
html=str(html,encoding = "GBK")

#将编码后的页面输出为txt文本存储
# file = open("page1.txt", "w")
file = codecs.open("page.txt", "w")
file.write(html)
file.close()


#读取存储的txt文本文件
# html = open('page1.txt', 'r').read()
html = codecs.open('page.txt', 'r').read()

# print("done")




#获取总页数
maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html)
# print("maxpage:",maxpage)

# # #使用正则提取userClient字段信息
userClient=re.findall(r',"usefulVoteCount".*?,"userClientShow":(.*?),',html)

# # #使用正则提取userLevel字段信息
userLevel=re.findall(r'"referenceImage".*?,"userLevelName":(.*?),',html)

# # #使用正则提取productColor字段信息
productColor=re.findall(r'"creationTime".*?,"productColor":(.*?),',html)

# # #使用正则提取recommend字段信息
recommend=re.findall(r'"creationTime".*?,"recommend":(.*?),',html)

# # #使用正则提取nickname字段信息
nickname=re.findall(r'"creationTime".*?,"nickname":(.*?),',html)

# # #使用正则提取userProvince字段信息
userProvince=re.findall(r'"referenceImage".*?,"userProvince":(.*?),',html)

# # #使用正则提取usefulVoteCount字段信息
usefulVoteCount=re.findall(r'"referenceImage".*?,"usefulVoteCount":(.*?),',html)

# #使用正则提取days字段信息
days=re.findall(r'"usefulVoteCount".*?,"days":(.*?)}',html)

# #使用正则提取score字段信息
score=re.findall(r'"referenceImage".*?,"score":(.*?),',html)

# #使用正则提取isMobile字段信息
isMobile=re.findall(r'"usefulVoteCount".*?,"isMobile":(.*?),',html)
mobile=[]
for m in isMobile:
 n=m.replace('}','') #替换掉最后的}
 mobile.append(n)

#使用正则提取productSize字段信息
productSize=re.findall(r'"creationTime".*?,"productSize":(.*?),',html)
# size=[]
# for s in productSize:
#   s1=s[3]
#   size.append(s1)
# print(productSize)

#使用正则提取时间字段信息
creationTime1=re.findall(r'"creationTime":(.*?),"referenceName',html)
#提取日期和时间
creationTime=[]
for d in creationTime1:
  date=d[1:20]
  creationTime.append(date)
# print(creationTime)
#提取小时信息
hour=[]
for h in creationTime:
  date=h[10:13]
  hour.append(date)
  # print(hour)

#使用正则提取评论信息
content=re.findall(r'"guid".*?,"content":(.*?)","creationTime"',html)
# 对提取的评论信息进行去重
# print("content:",content)
content_1=[]
for i in content:
    if not "img" in i:
        print("i:",i)
        content_1.append(i)
# print("content_1:",len(content_1))
# print("content_1:",content_1)

#数据保存成csv格式
#将前面提取的各字段信息汇总为table数据表
table=pd.DataFrame({'creationTime':creationTime,'hour':hour,'nickname':nickname,
                    'productColor':productColor,'productSize':productSize,
                    'recommend':recommend,'mobile':mobile,'userClient':userClient,
                    'userLevel':userLevel,'userProvince':userProvince,
                    'usefulVoteCount':usefulVoteCount,'content_1':content_1,
                    'days':days,'score':score})
#将creationTime字段更改为时间格式
table['creationTime']=pd.to_datetime(table['creationTime'])
#设置creationTime字段为索引列
table = table.set_index('creationTime')
#设置days字段为数值格式
table['days']=table['days'].astype(np.str)
#查看整理完的数据表
table.head()
##保存table数据表
# table.to_csv('jd_table1.csv')
##追加保存table数据表
table.to_csv('jd_table1.csv',mode='a',header=False)


#数据存入momgodb
print("开始连接数据库：")
client = pymongo.MongoClient('localhost', 27017)
rent_info = client['jd_table1']  # 给数据库命名
sheet_table = rent_info['jd_table1']  # 创建表单
sheet_table.insert({'creationTime':creationTime,'hour':hour,'nickname':nickname,
                    'productColor':productColor,'productSize':productSize,
                    'recommend':recommend,'mobile':mobile,'userClient':userClient,
                    'userLevel':userLevel,'userProvince':userProvince,
                    'usefulVoteCount':usefulVoteCount,'content_1':content_1,
                    'days':days,'score':score})
print("done......")


endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("endtime is:",endtime)