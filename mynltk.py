#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import jieba
import nltk
import time
begin = time.time()
content= open("D:/luheng/mypython/mynltktext.txt").read() 
corpus=[]
wg = jieba.cut(content, cut_all=False)
a=" ".join(wg)
corpus.append(a)
text = corpus[0]
print text
print len(text)
end = time.time()
print u"花费时间：%.2fs" % (end - begin)


   
