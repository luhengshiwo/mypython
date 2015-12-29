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
from sklearn import ensemble
from sklearn import cross_validation
from sklearn import linear_model
from sklearn import naive_bayes
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn import svm
from sklearn import tree
from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import neighbors
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
wanghuifile = open("D:/luheng/mypython/wanghui.txt",'r') 
for line in wanghuifile:
	if line.find(u"数据")!=-1:
		print "ok"
	else :
	    print line	
end = time.time()
print u"花费时间：%.2fs" % (end - begin)