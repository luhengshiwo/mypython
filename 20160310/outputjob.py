#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import json
import numpy as np
import re
import time
import pandas as pd
import pickle
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient(host='192.168.1.48', port=27017)
db = client.training.jobs
begin = time.time()
print db.find().count()
position, salary, exp, degree = [], [], [], []
i=0
for line in db.find():
    job = line["job"]
    position_categ = job["position_categ"]
    if position_categ != u"计算机/互联网/通信/电子":
        continue
    salary_start =  job["salary_start"]   
    salary_end = job["salary_end"]
    if salary_start ==0:
        salarymid =  salary_end
    else: 
        salarymid = salary_start    
    job_exp = job["job_exp"]
    try:
        jobexp = re.findall(r'(\w*[0-9]+)\w*', job_exp)[0]
        jobexp = (int(jobexp)) * 12
    except:
        jobexp = 0
    job_degree_level = job["job_degree_level"]
    if job_degree_level == u"不限" or job_degree_level == u"其他":
        degree_level = 0
    elif job_degree_level == u"中专" or job_degree_level == u"高中" or job_degree_level == u"初中" or job_degree_level == u"中技":
        degree_level = 1
    elif job_degree_level == u"大专":
        degree_level = 2
    elif job_degree_level == u"本科":
        degree_level = 3
    elif job_degree_level == u"本科":
        degree_level = 4
    elif job_degree_level == u"硕士":
        degree_level = 5
    elif job_degree_level == u"博士":
        degree_level = 6
    position_category= job["position_category"]   
    position.append(position_category)
    salary.append(salarymid)
    exp.append(jobexp)
    degree.append(degree_level)
    print i
    i=i+1
df = pd.DataFrame([salary, exp, degree,position]).T
print df
output = open("D:/luheng/20160310/data.pkl", 'wb')
pickle.dump(df, output)
output.close()
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
