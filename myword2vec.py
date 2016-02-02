#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import jieba
from gensim import corpora,models,similarities
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
content= open("D:/luheng/mydata/mytry.txt")
corpus=[]
for line in content:
    wg = jieba.cut(line, cut_all=False)
    a=" ".join(wg)
    corpus.append(a)
text=[[word for word in corpus.split()] for corpus in corpus]   
#此时text有初始语料的行数
#dictionary 建立了词典
#mycorpus 建立了语料库
dictionary = corpora.Dictionary(text)
# print dictionary
# print dictionary.token2id
mycorpus = [dictionary.doc2bow(mytext) for mytext in text]
lda = models.ldamodel.LdaModel(mycorpus,num_topics=3,id2word=dictionary)
for i in range(3):
	print lda.print_topic(i)


# tfidf = models.TfidfModel(mycorpus)
# corpus_tfidf = tfidf[mycorpus]
# for doc in corpus_tfidf:
# 	print doc
# lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=1)
# print lsi.print_topics(2)	
# corpus_lsi = lsi[corpus_tfidf]
# for doc in corpus_lsi:
# 	print doc