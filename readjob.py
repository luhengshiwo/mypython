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
hrjob1,hrjob2,peoplejob1,peoplejob2=[],[],[],[]
myfilehr = open("D:/luheng/mypython/myhr.txt",'r') 
for line in myfilehr:
	index1 = line.find("\t")
	job1=line[2:index1-1]
	hrjob1.append(job1.decode("utf-8"))
	index2 = line.find("\t",index1+1)
	job2=line[index1+2:index2-1]
	hrjob2.append(job2.decode("utf-8"))
myfilehr.close()
myfilepeople = open("D:/luheng/mypython/mypeople.txt",'r') 
for line in myfilepeople:
	index1 = line.find("\t")
	job1=line[2:index1-1]
	peoplejob1.append(job1.decode("utf-8"))
	index2 = line.find("\t",index1+1)
	job2=line[index1+2:index2-1]
	peoplejob2.append(job2.decode("utf-8"))
myfilehr.close()
df=pd.DataFrame([hrjob1,hrjob2,peoplejob1,peoplejob2]).T
for x in df[2].unique():
	print x
end = time.time()
print u"花费时间：%.2fs" % (end - begin)