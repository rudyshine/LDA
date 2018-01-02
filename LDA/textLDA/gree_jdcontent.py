#-*- coding: utf-8 -*-
import pandas as pd
import jieba
from gensim import corpora, models
import re

##评论内容提取
inputfile = '1993089jd_table.csv' #评论汇总文件
outputfile = '1993089jd_table.txt' #评论提取后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8')
# data = data[['content_1']][data['productSize'] == 'referenceName']
data = data[['content_1']]
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')

##原始数据去重
inputfile = outputfile#评论文件
outputfile = '1993089jd_table_process_1.txt' #评论处理后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8', header = None)
l1 = len(data)
data = pd.DataFrame(data[0].unique())
l2 = len(data)
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')
print(u'删除了%s条评论。' %(l1 - l2))  ##删除了199条评论。

##分词代码
outputfile1='1993089jd_table_cut.txt'
data1 = pd.read_csv(outputfile, encoding = 'utf-8', header = None) #读入数据
mycut = lambda s: ' '.join(jieba.cut(s)) #自定义简单分词函数
data1 = data1[0].apply(mycut) #通过“广播”形式分词，加快速度。
data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果

##LDA代码ss
posfile=outputfile1
stoplist='stoplist.txt'
pos = pd.read_csv(posfile, header = None)
stop = pd.read_csv(stoplist,  header = None, sep = 'tipdm')
#sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
#所以解决办法是手动设置一个不存在的分割词，如tipdm。
stop = [' ', ''] + list(stop[0]) #Pandas自动过滤了空格符，这里手动添加
pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stoplist])

#主题分析
pos_dict = corpora.Dictionary(pos[2])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
for i in range(3):
    print(pos_lda.print_topic(i)) #输出每个主题
