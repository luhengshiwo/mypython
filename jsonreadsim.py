#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import pickle
import numpy as np
import scipy as sp
import pandas as pd
from pandas.io.json import json_normalize
import json
import time
import re
import os
from os.path import join
import sys
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.externals.six import StringIO
# import pydot
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
source = "D:/luheng/mypython/parsedata2"
corpus = []
for root, dirs, files in os.walk(source):
    for OneFileName in files:
        if OneFileName.find('.txt') == -1:
            continue
        OneFullFileName = join(root, OneFileName)
        myfile = open(OneFullFileName)
        for line in myfile:
            data = json.loads(line)
            for key in data:
                try :
                    wg1 = jieba.cut(myproject, cut_all=False)
                    a1 = " ".join(wg1)
                    corpus.append(a1)
                except:
                    corpus.append(u"细节 略") 
                try:       
                    wg2 = jieba.cut(data[key]["long_desc"], cut_all=False)
                    a2 = " ".join(wg2)
                    corpus.append(a2)
                except :
                    corpus.append(u"细节 略")                
        myfile.close()