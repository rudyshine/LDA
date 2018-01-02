# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim import models,corpora
import time
import jieba
import pandas as pd
import re
import gensim


##文本预处理
def clean_email_text(text):
    text = text.replace('\n'," ") #新行，我们是不需要的
    text = re.sub(r"-", " ", text) #把 "-" 的两个单词，分开。（比如：july-edu ==> july edu）
    text = re.sub(r"\d+/\d+/\d+", "", text) #日期，对主体模型没什么意义
    text = re.sub(r"[0-2]?[0-9]:[0-6][0-9]", "", text) #时间，没意义
    text = re.sub(r"[\w]+@[\.\w]+", "", text) #邮件地址，没意义
    text = re.sub(r" ", "", text)  # 邮件地址，没意义
    text = re.sub(r"/[a-zA-Z]*[:\//\]*[A-Za-z0-9\-_]+\.+[A-Za-z0-9\.\/%&=\?\-_]+/i", "", text) #网址，没意义
    pure_text = ''
    # 以防还有其他特殊字符（数字）等等，我们直接把他们loop一遍，过滤掉
    for letter in text:
        # 只留下字母和空格
        if letter.isalpha() or letter==' ':
            pure_text += letter
    # 再把那些去除特殊字符后落单的单词，直接排除。
    # 我们就只剩下有意义的单词了。
    text = ' '.join(word for word in pure_text.split() if len(word)>1)
    return text


def get_cut():
    docs = df['content_1']
    docs = docs.apply(lambda s: clean_email_text(s)) ##apply方法写出格式
    doclist = docs.values ##取出所有内容
    output = open('cut.txt', 'w')
    for line in doclist:
        texts = ' '.join((jieba.cut(line)))
        output.write(texts+'\n')
    output.closed
    return True


def load_stopword():
    f_stop = open('stoplist.txt')
    sw = [line.strip() for line in f_stop]
    f_stop.close()
    return sw


if __name__ == '__main__':
    df = pd.read_csv("凉之静 (复件).csv")
    df = df[['content_1']].dropna()# 原邮件数据中有很多Nan的值，直接扔了。
    s=get_cut()

    print('初始化停止词列表 --')
    t_start = time.time()
    stop_words = load_stopword()

    print('开始读入语料数据 -- ')
    f = open('cut.txt')    #切词后的文件
    texts = [[word for word in line.strip().lower().split() if word not in stop_words] for line in f]
    print('读入语料数据完成，用时%.3f秒' % (time.time() - t_start))
    f.close()
    M = len(texts)
    print('文本数目：%d个' % M)

    print('正在建立词典 --')
    dictionary = corpora.Dictionary(texts)
    V = len(dictionary)
    print('词库个数：',V)
    print('正在计算文本向量 --')
    corpus = [dictionary.doc2bow(text) for text in texts]
    print('正在计算文档TF-IDF --')
    t_start = time.time()
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    print('建立文档TF-IDF完成，用时%.3f秒' % (time.time() - t_start))
    print('LDA模型拟合推断 --')
    num_topics = 5
    t_start = time.time()
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                            alpha=0.01, eta=0.01, minimum_probability=0.001,
                            update_every = 1, chunksize = 100, passes = 1)
    # lda.update(corpus_tfidf)##模型更新数据
    print('LDA模型完成，训练时间为\t%.3f秒' % (time.time() - t_start))
    lda.save('datasets.pkl')  # 保存到文件datasets.pkl中
    model = gensim.models.ldamodel.LdaModel.load('datasets.pkl')  # 从文件datasets.pkl中读出结果数据

    # 所有文档的主题   # 所有文档的主题
    # doc_topic = lda.get_document_topics(corpus_tfidf)
    # print('Document-Topic:\n',doc_topic)
    #

    # 随机打印某10个文档的主题
    num_show_topic = 50 # 每个文档显示前几个主题
    print('5个文档的主题分布：')
    doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
    ##采用有放回的做采样
    idx = np.arange(M) ##生成0到M-1的数组
    np.random.shuffle(idx)##对数组做个shuffle的排序
    idx = idx[:50]#取出前十个
    for i in idx:
        topic = np.array(doc_topics[i])
        topic_distribute = np.array(topic[:, 1]) ##主题分布
        topic_idx = topic_distribute.argsort()[:-num_show_topic-1:-1]##主题分布的词排序
        print(topic_distribute[topic_idx])

    #
    num_show_term =3  # 每个主题显示几个词
    print('每个主题的词分布：')
    for topic_id in range(num_topics):
        print('主题:',topic_id)
        term_distribute_all = lda.get_topic_terms(topicid=topic_id)
        term_distribute = term_distribute_all[:num_show_term]
        term_distribute = np.array(term_distribute)
        term_id = term_distribute[:, 0].astype(np.int)
        print('主题词：')
        for t in term_id:
            print(dictionary.id2token[t])
        print('概率：', term_distribute[:, 1])
