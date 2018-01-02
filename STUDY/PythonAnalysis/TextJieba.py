#-*- coding:utf-8 -*-
'''
一、特点
1、支持三种分词模式：
　　(1)精确模式：试图将句子最精确的切开，适合文本分析。
　　(2)全模式：把句子中所有可以成词的词语都扫描出来，速度非常快，但是不能解决歧义。
　　(3)搜索引擎模式：在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
2、支持繁体分词
3、支持自定义词典

二、实现
结巴分词的实现原理主要有一下三点：
(1)基于Trie树结构实现高效的词图扫描，生成句子中汉字所有可能成词情况所构成的有向无环图（DAG)。
(2)采用了动态规划查找最大概率路径, 找出基于词频的最大切分组合。
(3)对于未登录词，采用了基于汉字成词能力的HMM模型，使用了Viterbi算法。
'''
#
import jieba
#
# ##jieba分词
# '''cut方法有两个参数
# 1)第一个参数是我们想分词的字符串
# 2)第二个参数cut_all是用来控制是否采用全模式'''
#
# #全模式
word_list = jieba.cut("今天天气真好。亲爱的，我们去远足吧！",cut_all=True)
print("全模式：","|".join(word_list))
# #精确模式 , 默认就是精确模式
# word_list = jieba.cut("今天天气真好。亲爱的，我们去远足吧！",cut_all=False)
# print("精确模式：","|".join(word_list))
# #搜索引擎模式
# word_list = jieba.cut_for_search("今天天气真好。亲爱的，我们去远足吧！")
# print("搜索引擎：","|".join(word_list))
#
# ##添加自定义词典
# import jieba
#
# jieba.load_userdict("./cu.txt")
# word_list = jieba.cut("小红今天我们还去以前经常去的地方远足吗？要不咱们换个地方吧！园小园怎么样?没问题小豆芽")
# print("|".join(word_list))

##关键字提取
# import jieba.analyse
# jieba.analyse.extract_tags(sentence, topK = 20, withWeight = False, allowPOS = ())
## sentence:待提取的文本。
## topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
## withWeight:是否一并返回关键词权重值，默认值为False。
## allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。
## jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件。

# optparse模块OptionParser学习
# optparse是专门在命令行添加选项的一个模块。