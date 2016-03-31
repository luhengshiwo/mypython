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
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient(host='192.168.1.48', port=27017)
db = client.training.resumes
begin = time.time()
i = 0
salary1, degree, workmonth, gender, marry, agenow, salary2, work, project, skill1, hisid, position = [
], [], [], [], [], [], [], [], [], [], [], []
for resume in db.find({"latest_job_industry_category": u"计算机/互联网/通信/电子行业"}):  # 858920/4827926
    latest_workexp_job_salary = resume["latest_workexp_job_salary"]
    degree_level_notnum = resume["highest_degree_level"]
    if degree_level_notnum == "中技" or degree_level_notnum == "中专" or degree_level_notnum == "初中" or degree_level_notnum == "初中及以下" or degree_level_notnum == "高中":
        degree_level = 0
    elif degree_level_notnum == "大专" or degree_level_notnum == "":
        degree_level = 1
    elif degree_level_notnum == "本科":
        degree_level = 2
    elif degree_level_notnum == "硕士":
        degree_level = 3
    elif degree_level_notnum == "博士" or degree_level_notnum == "MBA":
        degree_level = 3
    elif degree_level_notnum == "博士后":
        degree_level = 4
    else:
        degree_level = 2
    workexp_month = resume["workexp_month"]
    sex = resume["sex"]
    marriage = resume["marriage"]
    age = resume["age"]
    try:
        expect_salary_notnum = resume["jobexp"]["salary"]
    except:
        expect_salary_notnum = 0
    expsalarygap = 0
    expect_salary = 0
    if expect_salary_notnum == u"面议":
        expect_salary = 0
    if expect_salary_notnum != None:
        try:
            salary = re.findall(r'(\w*[0-9]+)\w*', expect_salary_notnum)
            if len(salary) == 2:
                expect_salary = (int(salary[0]) + int(salary[1])) / 2
                expsalarygap = expect_salary - int(salary[0])
            elif len(salary) == 1:
                expect_salary = int(salary[0])
        except:
            expect_salary = 0
    try:
        position_notnum = resume["jobexp"]["position"]
    except:
        position_notnum = u"未知"
    workexp = resume["workexp"]
    projectinfo = resume["projectinfo"]
    skill = resume["skill"]
    hisidnum = resume["_id"]
    if latest_workexp_job_salary == 0:
        latest_workexp_job_salary = expect_salary * 0.8
    salary1.append(latest_workexp_job_salary)
    degree.append(degree_level)
    workmonth.append(workexp_month)
    gender.append(sex)
    marry.append(marriage)
    agenow.append(age)
    salary2.append(expect_salary)
    hisid.append(hisidnum)
    position.append(position_notnum)
    workexplen=len(workexp)
    i = i + 1
    print i,workexplen
    work.append(workexplen)
    # project.append(projectinfo)
    # skill1.append(skill)
print u"读取完毕"
df = pd.DataFrame([salary1, degree, workmonth, gender,
                   marry, agenow, salary2, position,work]).T
df = df.rename(columns={0: "salary_last", 1: "degree", 2: "workmonth",
                        3: "gender", 4: "marriage", 5: "age", 6: "salary_exp", 7: "position_exp",8:"work"})
df.index = hisid
df.to_csv("D:/luheng/20160310/readresumewithposition.csv",
          index=True, header=True, index_label="id")
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
