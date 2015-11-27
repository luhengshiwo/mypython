#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import pandas as pd
import pickle
import time
begin = time.time()
pickle_file = open("D:/luheng/mypython/data.pkl","rb")
df = pickle.load(pickle_file)
predictors = ['age','gender','degree','salary']
df[predictors]=df[predictors].astype(float)
df['size']=df['size'].astype(int)
print df.describe()
print df.columns
print df["degree"].mean
end = time.time()
print u"花费时间：%.2fs"%(end-begin)