#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import jieba
import gensim.models.word2vec as word2vec
content= open("D:/luheng/mypython/1234.txt").read() 
wg = jieba.cut(content, cut_all=False)