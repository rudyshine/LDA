#-*- coding:utf-8 -*-

import jieba.analyse
import numpy as np
import pandas as pd
import time
import re
import codecs
import jieba
import matplotlib.pyplot as plt

startime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
html = codecs.open('4521778page.txt', 'r').read()
productId='4521778'

#    # 产品名称
referenceName = re.findall(r',"guid".*?,"referenceName":(.*?),', html)
print("lenuserClient:", len(referenceName))
print("referenceName:", referenceName)

# 下单时间referenceTime
referenceTime1 = re.findall(r',"referenceName".*?,"referenceTime":(.*?),', html)
referenceTime = []
for d in referenceTime1:
    date = d[1:20]
    referenceTime.append(date)
print("lenuserClient:", len(referenceTime))
print("referenceTime:", referenceTime)

##提取userClient（用户客户端信息）字段信息
userClient = re.findall(r',"referenceName".*?,"userClientShow":(.*?),', html)
# ##提取userLevel（用户等级）字段信息
userLevel = re.findall(r'"productSize".*?,"userLevelName":(.*?),', html)
# #提取nickname字段信息
nickname = re.findall(r'"userImageUrl".*?,"nickname":(.*?),', html)
# #提取userProvince(省份)字段信息
userProvince = re.findall(r'"userImageUrl".*?,"userProvince":(.*?),', html)
# 提取days字段信息
days = re.findall(r'"referenceName".*?,"days":(.*?),', html)
##提取score字段信息
score = re.findall(r'"referenceName".*?,"score":(.*?),', html)
##提取isMobile字段信息
isMobile = re.findall(r'"productSize".*?,"isMobile":(.*?),', html)
# ##提取productSize字段信息
productSize = re.findall(r'"creationTime".*?,"productSize":(.*?),', html)
##提取时间字段信息
creationTime1 = re.findall(r'"creationTime":(.*?),"referenceName', html)
creationTime = []
for d in creationTime1:
    date = d[1:20]#取时间
    creationTime.append(date)
##提取评论信息
content = re.findall(r'"guid".*?,"content":(.*?)","creationTime"', html)
print("content:", len(content))
# 对提取的评论信息进行去重
content_1 = []
for i in content:
    if not "img" in i:
        content_1.append(i)
# 将前面提取的各字段信息汇总为table数据表，以便后面分析
table = pd.DataFrame({'creationTime': creationTime,"referenceTime":referenceTime,
                   'referenceName':referenceName,'nickname': nickname,
                   'productSize': productSize,'isMobile': isMobile,
                   'userClient': userClient,'userLevel': userLevel,
                   'userProvince': userProvince,'content_1': content_1,
                   'days': days, 'score': score})
table['creationTime'] = pd.to_datetime(table['creationTime'])
table = table.set_index('creationTime')
table.head()
print("存入csv....")
# table.to_csv('jd_table_textmaxpage.csv')
table.to_csv(productId+'jd_table.csv', mode='a', header=False)
print("存完....")
endtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print("endtime is:",endtime)
#

##商品评论关键词分析
#文本数据格式转换
word_str = ''.join(content_1)
#提取文字关键词
'''jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
sentence:待提取的文本。
topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
withWeight:是否一并返回关键词权重值，默认值为False。
allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件。
'''
word_rank=jieba.analyse.extract_tags(word_str, topK=20, withWeight=True, allowPOS=())
#转化为数据表
word_rank = pd.DataFrame(word_rank,columns=['word','rank'])
#查看关键词及权重
word_rank.sort_values(word_rank.columns[1],ascending=False)
print(word_rank.columns[1])
print(word_rank)

#
# #筛选包含'XX'关键字的评论
# content_2=[]
# for i in content_1:
#       if "董"in i or "格力"in i:
#             content_2.append(i)
# print(content_2)
# ###计算为了“董”或“格力”而购买商品的比例
# print(len(content_2)/len(content_1)*100)
#
#
# # ##计数统计，example：统计userClient
# df=pd.read_csv('4521778jd_table.csv')
# count = df['userClient'].value_counts()
# print(count)



df=pd.read_csv('4521778jd_table.csv')
s=jieba.cut(df,cut_all=True)
print(",".join(s))