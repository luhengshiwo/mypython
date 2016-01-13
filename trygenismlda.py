#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import jieba
import pandas as pd
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
from gensim import corpora,models,similarities
content= open("D:/luheng/mydata/mytry.txt")
corpus=[]
for line in content:
    wg = jieba.cut(line, cut_all=False)
    a=" ".join(wg)
    corpus.append(a)
text=[[word for word in corpus.split()] for corpus in corpus]   
textdict = corpora.Dictionary(text)
textcorpus = [textdict.doc2bow(i) for i in text]
model = models.ldamodel.LdaModel(
	textcorpus,num_topics=3,id2word = textdict)    
for i in range(3):
    print model.print_topic(i)   