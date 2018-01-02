# -*- coding:utf-8 -*-
import pandas as pd
import jieba
import numpy
import codecs
from numpy import array
from sklearn import tree
from sklearn.svm import SVC
import time

startime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print('startime:',startime)

f_stop = open('stoplist.txt')
stop_word = [line.strip() for line in open('stoplist.txt').read()]

f=codecs.open('凉之静 (复件).txt','r',encoding='utf-8')
f=f.read()
texts=jieba.cut(f,cut_all=False,HMM=True)
text1='/'.join(texts)
text2=text1.replace('\n','/')
text_word=list(set(text1.split('/'))-set(stop_word))


##构造主题的稀疏矩阵eig_matrix，作为训练的输入
f_themes=text1.split('\n')
f_rows=[]
for line in f_themes:
    f_rows.append(line.split('/'))
eig_matrix=numpy.zeros([len(f_rows),len(text_word)])
for i in range(len(f_themes)):
    for j in range(len(eig_matrix[i])):
        if text_word[j] in f_rows[i]:
            eig_matrix[i][j]=1.0

#构造训练的输出y，即各类别，第1/2/3类邮件分别有48好、20中、29差
y=numpy.zeros([98,1])
y1=numpy.ones([20,1])
y2=numpy.ones([29,1])+numpy.ones([29,1])
y[49:69]=y1
y[69:]=y2

# #分类算法四：DT
def dT(x,y,newx):
    dt = tree.DecisionTreeClassifier(criterion=str('entropy'))
    dt.fit(x, y)
    return dt.predict([newx])


# #新来邮件获得分类结果函数
def topicClassify(topic):
    #新邮件分词
    email_seg = list(set(('/'.join(jieba.cut(topic,HMM=True))).split('/')))
    #构造稀疏向量
    eig_vector = numpy.zeros(len(text_word))
    for k in range(len(text_word)):
        if text_word[k] in email_seg:
            eig_vector[k] = 1.0
    return dT(eig_matrix,y,eig_vector)


while True:
    topic = input(u'新主题：')
    if topic=='q' or topic=='Q':
        break#跳出程序
    else:
        result = topicClassify(topic)
        print(result)
        endtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('endtime:', endtime)
