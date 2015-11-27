#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import jieba
import nltk
content= open("D:/luheng/mypython/1234.txt").read() 
wg = jieba.cut(content, cut_all=False)
text=[word for word in wg]
a = nltk.FreqDist(text)
print a


   
