#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import numpy as np
import scipy as sp
import jieba
import pandas as pd
import os
import codecs
from gensim import corpora, models, similarities
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
# level=logging.INFO)#输出日志
stop = open('D:/luheng/mydata/stopword.txt')
content = open("D:/luheng/mydata/mytry2.txt")  # 读取文本
text = []
stopwords = {}.fromkeys([line.rstrip() for line in stop])
# 打开两个文件，一个是要处理的文本，还有一个是停用词
# 需要注意的是停用词里面是str，而jieba分词里面分出来的是unicode
for line in content:
    result = []
    wg = jieba.cut(line, cut_all=False)
    for w in wg:
        try:
            seg = str(w.encode('gbk'))  # 中文编码转化
        except:
            seg = str(w)  # 非中文编码转化
        if seg not in stopwords:
            result.append(w)
        a = " ".join(result)
    text.append(a)
corpus = [[word for word in line.split()] for line in text]
# 最终corpus里面就是准备好的语料了
stop.close()
content.close()
# textdict里面是词典
# textcorpus就是分开的一篇篇文章，也叫做语料库
textdict = corpora.Dictionary(corpus)  # 词到数字｛"数据挖掘"：0,"篮球":1,｝


# 通过词典，将语料中的文字转化为数字(编号)
# 最终形如[[(0,1),(1,4),(2,2)],[(1,3),(2,2)],[(3,1),(4,1),(5,1)]]
# 小括号第一个是词的编号，第二个是个数
textcorpus = [textdict.doc2bow(i) for i in corpus]
# model = models.ldamodel.LdaModel(
# 	textcorpus,num_topics=3,id2word = textdict)
# topics = [model[c] for c in textcorpus]
# print topics
# for i in range(3):
# 	print model.print_topic(i)

# tfidf模型
tfidf = models.TfidfModel(textcorpus)
corpus_tfidf = tfidf[textcorpus]


# lsa模型
lsi = models.LsiModel(corpus_tfidf, id2word=textdict, num_topics=2)
corpus_lsi = lsi[textcorpus]
# print lsi.print_topics(2)
print corpus_lsi
index = similarities.MatrixSimilarity(lsi[textcorpus])
sims = index[corpus_lsi]
print list(enumerate(sims))
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print sims
