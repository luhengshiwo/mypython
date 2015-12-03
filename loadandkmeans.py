#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import pandas as pd
import pickle
import time
import matplotlib.pyplot as plt
begin = time.time()
pickle_file = open("D:/luheng/mypython/data.pkl","rb")
df = pickle.load(pickle_file)
pickle_file.close()
print u"读入pkl成功，进行下一步"
print df["numb"].min()
print df["numb"].max()
# plt.scatter(df["time2"],df["salary2"])
# plt.show()
end = time.time()
print u"花费时间：%.2fs"%(end-begin)