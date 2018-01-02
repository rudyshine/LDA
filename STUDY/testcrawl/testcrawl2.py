#导入requests库(请求和页面抓取)
import requests
#导入time库(设置抓取Sleep时间)
import time
#导入random库(生成乱序随机数)
import random
#导入正则库(从页面代码中提取信息)
import re
#导入数值计算库(常规计算)
import numpy as np
#导入科学计算库(拼表及各种分析汇总)
import pandas as pd
#导入绘制图表库(数据可视化)
import matplotlib.pyplot as plt
#导入结巴分词库(分词)
import jieba as jb
#导入结巴分词(关键词提取)
import jieba.analyse
import codecs

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


#获取总页数
url0="https://club.jd.com/comment/productPageComments.action?callback=" \
     "fetchJSON_comment98vv79456&productId=1993092&score=0&sortType=5&" \
     "pageSize=10&isShadowSku=0&page=0"
r=requests.get(url=url0,headers=headers,cookies=cookie)
html0=r.content.decode('gb2312','ignore')
html0=str(html0)
file = codecs.open("page2.txt", "w")
file.write(html0)
file.close()
html0 = codecs.open('page2.txt', 'r').read()
#获取总页数
maxpage=re.findall(r',"jwotestProduct".*?,"maxPage":(.*?),',html0)
print("maxpage:",maxpage)

print("开始执行抓取......")
url1="https://club.jd.com/comment/productPageComments.action?callback=" \
     "fetchJSON_comment98vv79456&productId=3082122&score=0&sortType=5&" \
     "pageSize=10&isShadowSku=0&page="

ran_num=random.sample(range(1800,1820), 5)
# r=requests.get(url=url1,headers=headers,cookies=cookie)
# html=r.content.decode('gb2312','ignore')
for i in ran_num:
      i=str(i)
      url=url1+i
      r=requests.get(url=url,headers=headers,cookies=cookie)
      html2=r.content.decode('gb2312','ignore')
      # html = html + html2
      html =html2
      time.sleep(5)
      print("当前抓取页面:",url,"状态:",r)

# print(type(html))
html=str(html)
file = codecs.open("page2.txt", "w",encoding="GBK")
file.write(html)
file.close()
html = codecs.open('page2.txt', 'r',encoding="GBK").read()

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
content=re.findall(r'"guid".*?,"content":(.*?),',html)
# 对提取的评论信息进行去重
content_1=[]
for i in content:
  if not "img" in i:
   content_1.append(i)


#将前面提取的各字段信息汇总为table数据表，以便后面分析
table=pd.DataFrame({'creationTime':creationTime,'hour':hour,'nickname':nickname,'productColor':productColor,'productSize':productSize,'recommend':recommend,'mobile':mobile,'userClient':userClient,'userLevel':userLevel,'userProvince':userProvince,'usefulVoteCount':usefulVoteCount,'content_1':content_1,'days':days,'score':score})
#将creationTime字段更改为时间格式
table['creationTime']=pd.to_datetime(table['creationTime'])
#设置creationTime字段为索引列
table = table.set_index('creationTime')
#设置days字段为数值格式
table['days']=table['days'].astype(np.str)
#查看整理完的数据表
table.head()

#保存table数据表
table.to_csv('jd_table22.csv',encoding="gbk")

#对数据表按月进行汇总并生成新的月度汇总数据表
# table_month=table.resample('M')
# month=table_month['nickname']
# print(month)
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

#在table表中筛选使用移动设备的条目并创建新表
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
plt.ylabel('移动设备评论数量')
plt.title('PC与移动设备评论数量变化趋势')
plt.subplot(2, 1, 2)
plt.plot(mobile_n,'go',mobile_n,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
plt.xlabel('月份')
plt.ylabel('PC评论数量')
plt.show()

#按24小时分别对table表中的nickname进行计数


# hour_group=table.groupby('hour')['nickname'].agg(len)
#汇总24小时评论数量变化趋势图
# plt.rc('font', family='STXihei', size=9)
# a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
# plt.bar([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],hour_group,color='#99CC01',alpha=0.8,align='center',edgecolor='white')
# plt.xlabel('24小时')
# plt.ylabel('评论数量')
# plt.title('24小时评论数量变化趋势')
# plt.legend(['评论数量'], loc='upper right')
# plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='y',alpha=0.4)
# plt.xticks(a,('0','1','2','3','4','5','6','7','8','9','10','11','12''13','14','15','16','17','18','19','20','21','22','23'))
# plt.show()

