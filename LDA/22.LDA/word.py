##-*- coding: utf-8 -*-
import codecs
import jieba
import pandas as pd
import re
from gensim import corpora
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
    # print("text:",text)

    return text


def get_cut():
    docs = df['content_1']
    docs = docs.apply(lambda s: clean_email_text(s)) ##apply方法写出格式
    # docs.head(1).values ##取出值变成数组
    doclist = docs.values ##取出所有内容
    output = open('cut.txt', 'w')
    for line in doclist:
        texts = ' '.join((jieba.cut(line)))
        print(texts)
        output.write(texts+'\n')


    return True


if __name__ == '__main__':

    df = pd.read_csv("格力凉之静.csv")
    df = df[['nickname', 'content_1']].dropna()# 原邮件数据中有很多Nan的值，直接扔了。
    s=get_cut()
