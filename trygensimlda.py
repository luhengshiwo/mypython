#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import jieba
import pandas as pd
import os
import codecs
from gensim import corpora,models,similarities
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
stop = open('D:/luheng/mydata/stopword.txt')
content= open("D:/luheng/mydata/mytry2.txt")#读取文本 
text=[]
stopwords = {}.fromkeys([ line.rstrip() for line in stop ])	
# 打开两个文件，一个是要处理的文本，还有一个是停用词
# 需要注意的是停用词里面是str，而jieba分词里面分出来的是unicode
for line in content:
    result=[]
    wg = jieba.cut(line, cut_all=False)
    for w in wg: 
        try:
            seg=str(w.encode('gbk'))#中文编码转化
        except:
            seg=str(w)    #非中文编码转化
        if seg not in stopwords:
            result.append(w)                    
        a=" ".join(result)
    text.append(a)
corpus=[[word for word in line.split()] for line in text]
#最终corpus里面就是准备好的语料了
stop.close()   
content.close()      
#textdict里面是词典
#textcorpus就是分开的一篇篇文章，也叫做语料库  
textdict = corpora.Dictionary(corpus)
# for key in textdict.token2id:
# 	print key,textdict.token2id[key]
textcorpus = [textdict.doc2bow(i) for i in corpus]
print textcorpus
model = models.ldamodel.LdaModel(
	textcorpus,num_topics=2,id2word = textdict)    
topics = [model[c] for c in textcorpus]
# print topics
# for i in range(2):
# 	print model.print_topic(i)