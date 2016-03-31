#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import json
import numpy as np
import re
import time
import csv
import pandas as pd
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
pickle_file = open("D:/luheng/20160310/data.pkl","rb")
df = pickle.load(pickle_file)
pickle_file.close()
print len(df)
df=df.rename(columns={0:"salary",1:"workmonth",2:"degree",3:"position"})
df[["salary","workmonth","degree"]]=df[["salary","workmonth","degree"]].astype(int)
df=df[df["workmonth"]<150]
df=df[df["salary"]<20000]
df=df[df["salary"]>1000]
print len(df)
print df["salary"]
# for i in range(len(df)):
#     print df.iloc[i]
                    

df.to_csv("D:/luheng/20160310/jobdata.csv",index=False)

# model_id,prov_id=[],[]
# for line in result:
#     model_id.append(line[0])
#     prov_id.append(line[1])
# df = pd.DataFrame([model_id,prov_id ]).T
# df = df.rename(columns={0:"model_id" ,1:"prov_id"}
# import pandas.io.sql as sql
# sql.read_frame("")



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
    words = re.split(';|,|:|、', position)
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
filename = open("D:/luheng/20160310/jobdata.csv","rb")
i=0
position2 =[] 
for line in csv.reader(filename):
    if  i>0 :
        position2.append(find_position(line[3]))
    i=i+1         
df["position"] = position2
print df["position"]
# print df["position"] 

# # str1 = "a;bbc,:d、aa"
# # d = re.split(';|,|:|、', str1)
# # print d
# # print df
# # print df.describe()
df.to_csv("D:/luheng/20160310/jobdata_p2.csv",index=False)






df = pd.read_csv("D:/luheng/20160310/jobdata_p2.csv")
print len(df)
df = df[df["position"] < 6]

df.to_csv("D:/luheng/20160310/jobdata_p2final.csv",index=False)