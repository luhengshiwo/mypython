#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import json
import numpy as np
import re
import time
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
begin = time.time()
df = pd.read_csv("D:/luheng/20160310/readresumewithposition.csv", index_col=0)
print df
df.loc[df["salary_last"] == " ", "salary_last"] = 0
df.loc[df["gender"] == u"男", "gender"] = 0
df.loc[df["gender"] == u"女", "gender"] = 1
df.loc[df["gender"] == "", "gender"] = 0
df.loc[df["marriage"] == u"未婚", "marriage"] = 0
df.loc[df["marriage"] == u"已婚未育", "marriage"] = 1
df.loc[df["marriage"] == u"已婚已育", "marriage"] = 2
df.loc[df["marriage"] == u"其他", "marriage"] = 3
df.loc[df["marriage"] == u"保密", "marriage"] = 3
df["salary_last"].fillna(0)
print len(df)
#{0:"salary_last",1:"degree",2:"workmonth",3:"gender",4:"marriage",5:"age",6:"salary_exp"}
df = df[df["salary_last"] >= 0]
df = df[df["salary_exp"] >= 0]
df = df[df["degree"] >= 0]
df = df[df["workmonth"] >= 0]
df = df[df["gender"] >= 0]
df = df[df["age"] >= 0]
print len(df)
df[["salary_last", "degree", "workmonth", "gender", "marriage", "age", "salary_exp","work"]] = df[
    ["salary_last", "degree", "workmonth", "gender", "marriage", "age", "salary_exp","work"]].astype(int)
# print df.describe()
df.to_csv("D:/luheng/20160310/resumeposition.csv",
          index=True, header=True, index_label="id")
