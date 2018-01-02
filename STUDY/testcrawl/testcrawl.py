import requests
import time
import random
import re
import numpy as np
import pandas as pd
import pymongo
import codecs
import matplotlib.pyplot as plt

startime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("startime is:",startime)

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
#获取总页数
#获取总页数maxPage":6861
#page=
#page
# list=[]
# ran_num=random.sample(list,10)
url0="https://club.jd.com/comment/productPageComments.action?callback=" \
     "fetchJSON_comment98vv79456&productId=1993092&score=0&sortType=5&" \
     "pageSize=10&isShadowSku=0&page=0"
r=requests.get(url=url0,headers=headers,cookies=cookie)
html0=r.content.decode('gb2312','ignore')
html0=str(html0)
file = codecs.open("page0.txt", "w")
file.write(html0)
file.close()
html0 = codecs.open('page0.txt', 'r').read()
#获取总页数
maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html0)
page=maxpage.pop()

print("开始执行抓取......")
url1="https://club.jd.com/comment/productPageComments.action?callback=" \
     "fetchJSON_comment98vv79456&productId=1993089&score=0&sortType=5&" \
     "pageSize=10&isShadowSku=0&page="
ran_num=range(0,int(page))
r=requests.get(url=url1,headers=headers,cookies=cookie)
html=r.content.decode('gb2312','ignore')
for i in ran_num:
      i=str(i)
      url=url1+i
      r=requests.get(url=url,headers=headers,cookies=cookie)
      html2=r.content.decode('gb2312','ignore')
      html = html + html2
      time.sleep(1)
      print("当前抓取页面:",url,"状态:",r)

#写入文件
html=str(html)#, encoding = "GBK")
file = codecs.open("page.txt", "w")
file.write(html)
file.close()


html = codecs.open('page.txt', 'r').read()
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
# print(creationTime)
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


#将前面提取的各字段信息汇总为table数据表，以便后面分析
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

#保存table数据表


# 新建/追加保存table数据表
print("存入csv....")
table.to_csv('jd_table_11111.csv',mode='a')
# table.to_csv('jd_table.csv',mode='a',header=False)
print("存完....")

#数据存入momgodb
print("开始连接数据库：")
client = pymongo.MongoClient('localhost', 27017)
rent_info = client['jd_table']  # 给数据库命名
sheet_table = rent_info['jd_table_1234']  # 创建表单
sheet_table.insert({'creationTime':creationTime,'hour':hour,'nickname':nickname,
                    'productColor':productColor,'productSize':productSize,
                    'recommend':recommend,'mobile':mobile,'userClient':userClient,
                    'userLevel':userLevel,'userProvince':userProvince,
                    'usefulVoteCount':usefulVoteCount,'content_1':content_1,
                    'days':days,'score':score})
print("done......")

#在table表中筛选使用移动设备的条目并创建新表
table_month=table.resample('M')
month=table_month['nickname']
# print(month)
mobile_t=table.loc[table["mobile"] == "true"]
#在table中筛选没有使用移动设备的条目并创建新表
mobile_f=table.loc[table["mobile"] == "false"]
#按月汇总使用移动设备的数据
mobile_t_m=mobile_t.resample('M',how=len)
#按月汇总不使用移动设备的数据
mobile_f_m=mobile_f.resample('M',how=len)
#提取使用移动设备的按月汇总nickname
mobile_y=mobile_t_m['nickname']
#提取没有使用移动设备的按月汇总nickname
mobile_n=mobile_f_m['nickname']
#绘制PC与移动设备评论数量变化趋势图
plt.subplot(2, 1, 1)
plt.plot(mobile_y,'go',mobile_y,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
plt.ylabel('mobile content')
plt.title('PC&mobile')
plt.subplot(2, 1, 2)
plt.plot(mobile_n,'go',mobile_n,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
plt.xlabel('month')
plt.ylabel('PC content')
plt.show()


# #绘制分月评论数量变化趋势图
# plt.rc('font', family='STXihei', size=9)
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
# plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13],month,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
# plt.xlabel('月份')
# plt.ylabel('评论数量')
# plt.title('分月评论数量变化趋势')
# plt.legend(['评论数量'], loc='upper right')
# plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
# plt.xticks(a,('15-11','12','16-01','02','03','04','05','06','07','08','09','10','11'))
# plt.show()


#在table表中按userClient对数据进行汇总
userClient_group=table.groupby('userClient')['nickname'].agg(len)
#汇总用户客户端分布情况
plt.rc('font', family='STXihei', size=9)
a=np.array([1,2,3,4,5])
plt.bar([1,2,3,4,5],userClient_group,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
plt.xlabel('客户端分布')
plt.ylabel('评论数量')
plt.title('用户客户端分布情况')
plt.legend(['评论数量'], loc='upper right')
plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
plt.ylim(0,300)
plt.xticks(a,('PC','Android','iPad','iPhone','微信购物'))
plt.show()