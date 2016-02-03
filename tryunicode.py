#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import jieba
import pandas as pd
import os
import codecs
import sys
import jieba.posseg as pseg 
import time  
from gensim import corpora,models,similarities
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
t1=time.time() 
stop = open('D:/luheng/mydata/stopword.txt')
f= open("D:/luheng/mydata/mytry.txt","r") #读取文本  
stopwords = {}.fromkeys([line.rstrip() for line in stop ])
txtlist=f.read() #f.read().decode('utf-8') 
words=jieba.cut(txtlist)  
result=" "
for w in words: 
    try:
        seg=str(w.encode('gbk'))
    except:
        seg=str(w)    
    if seg not in stopwords:
        result += w +" "  #去停用词              
stop.close()   
f.close()  
t2=time.time() 
print(u"分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果
model = models.ldamodel.LdaModel(result,num_topics=10,id2word = result.id2word) 
topics=[model[c] for c in result]
print topics[0]