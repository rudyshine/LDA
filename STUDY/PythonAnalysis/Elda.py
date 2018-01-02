# -*- coding: utf-8 -*-
import os
import codecs
import logging

import jieba
from lxml import etree
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''
Sogou新闻语料预处理
@chenbingjin 2016-07-01
'''

train = []
# huge_tree=True, 防止文件过大时出错 XMLSyntaxError: internal error: Huge input lookup
parser = etree.XMLParser(encoding='utf8',huge_tree=True)

def load_data(dirname):
    global train
    files = os.listdir(dirname)
    for fi in files:
        logging.info("deal with "+fi)
        text = codecs.open(dirname+fi, 'r', encoding='utf8').read()
        # xml自身问题，存在&符号容易报错, 用&amp;代替
        text = text.replace('&', '&amp;')
        # 解析xml，提取新闻标题及内容
        root = etree.fromstring(text, parser=parser)
        docs = root.findall('doc')
        for doc in docs:
            tmp = ""
            for chi in doc.getchildren():
                if chi.tag == "contenttitle" or chi.tag == "content":
                    if chi.text != None and chi.text != "":
                        tmp += chi.text
            if tmp != "":
                train.append(tmp)


from gensim.corpora import Dictionary
from gensim.models import LdaModel

stopwords = codecs.open('4521778jd_table.csv','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
train_set = []
for line in train:
    line = list(jieba.cut(line))
    train_set.append([ w for w in line if w not in stopwords ])

# 构建训练语料
dictionary = Dictionary(train_set)
corpus = [ dictionary.doc2bow(text) for text in train_set]

# lda模型训练
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
lda.print_topics(20)