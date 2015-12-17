#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import numpy as np
import jieba
import nltk
import time
from nltk import *
import matplotlib.pyplot as plt
# import sys 
# reload(sys) 
# sys.setdefaultencoding("utf-8")
begin = time.time()
#注意下面的.read(),要是没有的话就出错了
content = open("D:/luheng/mypython/mynltktext.txt").read()
wg = jieba.cut(content, cut_all=False)
text = " ".join(wg)
# print text.similar("1")
tokens = nltk.word_tokenize(text)
text = nltk.Text(tokens)
# a =text.count(u"软件")
# print a
# print text.index(u"系统")
# print text[90]*2
# fr = FreqDist(text)
# voca = fr.keys()[:10]
# fr.plot(50,cumulative=True)
v=set(text)
long_words =[w for w in v if len(w)>2]
text = sorted(long_words)
for word in text:
	print word
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
