#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import jieba
import numpy as np
import jieba.posseg as pseg
import os
import sys
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import jieba.analyse
content= open("D:/luheng/mypython/mytry.txt")
corpus=[]
for line in content:
    wg = jieba.cut(line, cut_all=False)
    a=" ".join(wg)
    corpus.append(a)
vectorizer=CountVectorizer()
#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()
#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))
#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
w= vectorizer.fit_transform(corpus)
word=vectorizer.get_feature_names()
#获取词袋模型中的所有词语
weight=tfidf.toarray()
#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
a=weight[0]
b=weight[1]
c=weight[2]
print a*(b.T)
num = float(sum(a * b.T)) 
#若为行向量则 A * B.T
denom = np.linalg.norm(a) * np.linalg.norm(b)
cos = num / denom 
#余弦值
sim = 0.5 + 0.5 * cos 
#归一化
print sim
# for i in range(len(weight)):
# #打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
#     print u"-------这里输出第",i,u"类文本的词语tf-idf权重------"
#     for j in range(len(word)):
#         print word[j],weight[i][j]
