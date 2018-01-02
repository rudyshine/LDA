import numpy as np
import pandas as pd
import time
import re
import codecs
import matplotlib.pyplot as plt

startime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
html = codecs.open('3889758page.txt', 'r').read()

#产品名称
referenceName=re.findall(r',"guid".*?,"referenceName":(.*?),',html)
print("lenuserClient:",len(referenceName))
print("referenceName:",referenceName)

#下单时间referenceTime
referenceTime1=re.findall(r',"referenceName".*?,"referenceTime":(.*?),',html)
referenceTime=[]
for d in referenceTime1:
  date=d[1:20]
  referenceTime.append(date)
print("lenuserClient:",len(referenceTime))
print("referenceTime:",referenceTime)

##提取userClient（用户客户端信息）字段信息
userClient=re.findall(r',"referenceName".*?,"userClientShow":(.*?),',html)
print("lenuserClient:",len(userClient))
print("userClient:",userClient)

# ##提取userLevel（用户等级）字段信息
userLevel=re.findall(r'"productSize".*?,"userLevelName":(.*?),',html)
print("lenuserLevel:",len(userLevel))
print("userLevel",userLevel)
# #提取productColor字段信息
# productColor=re.findall(r'"referenceName".*?,"productColor":(.*?),',html)
# print("productColor",productColor)
# print("lenuserLevel:",len(productColor))
# # #提取recommend(推荐)字段信息
# recommend=re.findall(r'"creationTime".*?,"recommend":(.*?),',html)
# print("lenuserLevel:",len(recommend))
# print("recommend",recommend)
# #提取nickname字段信息
nickname=re.findall(r'"userImageUrl".*?,"nickname":(.*?),',html)
print("lenuserLevel:",len(nickname))
print("nickname",nickname)

# #提取userProvince(省份)字段信息
userProvince=re.findall(r'"userImageUrl".*?,"userProvince":(.*?),',html)
print("lenuserLevel:",len(userProvince))
print("userProvince",userProvince)

# # #提取usefulVoteCount（被标记的有用评论数）字段信息
# usefulVoteCount=re.findall(r'"referenceImage".*?,"usefulVoteCount":(.*?),',html)
# print("lenuserLevel:",len(usefulVoteCount))
# print("usefulVoteCount:",usefulVoteCount)

#提取days字段信息
days=re.findall(r'"referenceName".*?,"days":(.*?),',html)
print("lendays:",len(days))
print("days:",days)

# #追加评论
# afterDays=re.findall(r'"referenceName".*?,"afterDays":(.*?)}',html)
# print("lenafterDays:",len(afterDays))
# print("afterDays:",afterDays)

##提取score字段信息
score=re.findall(r'"referenceName".*?,"score":(.*?),',html)
print("lenscore:",len(score))
print("score:",score)
##提取isMobile字段信息
isMobile=re.findall(r'"productSize".*?,"isMobile":(.*?),',html)
print("lenscore:",len(isMobile))
print("isMobile:",isMobile,"\n")
# mobile=[]
# for m in isMobile:
#     n=m.replace('}','') #替换掉最后的}
#     mobile.append(n)
# print("lenscore:",len(mobile))
# print("mobile:",mobile)
# ##提取productSize字段信息
productSize=re.findall(r'"creationTime".*?,"productSize":(.*?),',html)
print("lenscore:",len(productSize))
print("productSize:",productSize)

##提取时间字段信息
creationTime1=re.findall(r'"creationTime":(.*?),"referenceName',html)
creationTime=[]
for d in creationTime1:
  date=d[1:20]
  creationTime.append(date)
print("lenscore:",len(creationTime))
print("creationTime:",creationTime)
# hour=[]
# for h in creationTime:
#   date=h[10:13]
#   hour.append(date)
# print("lenscore:",len(hour))
# print("hour:",hour)
##提取评论信息
content=re.findall(r'"guid".*?,"content":(.*?)","creationTime"',html)
print("content:",len(content))
# 对提取的评论信息进行去重
content_1=[]
for i in content:
  if not "img" in i:
      content_1.append(i)
print("lencontent_1:",len(content_1))
print("content_1:",content_1)
table = pd.DataFrame({'creationTime': creationTime,"referenceTime":referenceTime,
                      "referenceName":referenceName,'nickname': nickname,
                       'productSize': productSize,
                       'isMobile': isMobile, 'userClient': userClient,
                      'userLevel': userLevel, 'userProvince': userProvince,
                       'content_1': content_1,
                      'days': days, 'score': score})
# table = pd.DataFrame({'userClient': userClient, 'days': days,'score': score})
table['creationTime'] = pd.to_datetime(table['creationTime'])
table['referenceTime'] = pd.to_datetime(table['referenceTime'])
table = table.set_index('creationTime')
table.head()
print("存入csv....")
# table.to_csv('jd_table_textmaxpage.csv')
table.to_csv( 'jd_table2222====.csv', mode='a')
print("存完....")
endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("endtime is:",endtime)

# # print(df)
# mobile_t=table.loc[table["mobile"] == "true"]
# #在table中筛选没有使用移动设备的条目并创建新表
# mobile_f=table.loc[table["mobile"] == "false"]
# #按月汇总使用移动设备的数据
# mobile_t_m=mobile_t.resample('M',how=len)
# #按月汇总不使用移动设备的数据
# mobile_f_m=mobile_f.resample('M',how=len)
# #提取使用移动设备的按月汇总nickname
# mobile_y=mobile_t_m['nickname']
# #提取没有使用移动设备的按月汇总nickname
# mobile_n=mobile_f_m['nickname']
#
# plt.subplot(2, 1, 1)
# plt.plot(mobile_y,'go',mobile_y,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
# plt.ylabel('移动设备评论数量')
# plt.title('PC&mobile')
# plt.subplot(2, 1, 2)
# plt.plot(mobile_n,'go',mobile_n,'g-',color='#99CC01',linewidth=3,markeredgewidth=3,markeredgecolor='#99CC01',alpha=0.8)
# plt.xlabel('month')
# plt.ylabel('PC')
# plt.show()