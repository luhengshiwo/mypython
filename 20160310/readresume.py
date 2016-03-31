#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import json
import numpy as np
import re
import time
import csv
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
begin = time.time()
df = pd.read_csv("D:/luheng/20160310/resumeposition.csv", index_col=0)
print len(df)
df = df[df["salary_last"] < 20000]
df = df[df["salary_exp"] < 20000]
df = df[df["workmonth"] < 1000]
df = df[df["age"] < 75]
df = df[df["salary_last"] > 2000]
df = df[df["salary_exp"] > 2000]
print len(df)
df = df[df["salary_exp"]>df["salary_last"]]
print len(df)
df.to_csv("D:/luheng/20160310/resume_p.csv",index_col=0)

jobtitle = pd.read_csv("D:/luheng/20160310/jobTitleDic.csv",
                       header=None, encoding="gbk")


def fit_position(word):
    position = jobtitle[jobtitle[0] == word][1]
    if len(position == 1):
        level = int(position)
    else:
        level = 6
    return level

def find_position(position): 
    words = re.split(';|,|、', position)
    allposition = []
    for word in words:
        level = fit_position(word)
        if level > 0:
            allposition.append(level)
    if len(allposition) > 0:
        positionlevel = min(allposition)
    else:
        positionlevel = 0 
    return positionlevel
filename = open("D:/luheng/20160310/resume_p.csv","rb")
i=0
position2 =[] 
for line in csv.reader(filename):
    if  i>0 :
        position2.append(find_position(line[8]))
    i=i+1         
df["position"] = position2
print df["position"]
# print df["position"] 

# # str1 = "a;bbc,:d、aa"
# # d = re.split(';|,|:|、', str1)
# # print d
# # print df
# # print df.describe()
df.to_csv("D:/luheng/20160310/resume_p2.csv",index_col=0)

df = pd.read_csv("D:/luheng/20160310/resume_p2.csv", index_col=0)
print len(df)
df = df[df["position"] < 6]

df.to_csv("D:/luheng/20160310/resume_p2final.csv",index_col=0)

end = time.time()
print u"花费时间：%.2fs" % (end - begin)
