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
from scipy.stats import gaussian_kde
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
hrjob1,hrjob2,peoplejob1,peoplejob2=[],[],[],[]
predictors = [ "sex","age", "workexp_months", "exp", "marriage", "school_level", "degree_level",
              "degree", "salary_type", "latest_workexp_job_salary", "salary1","salary2","job1","job2","simi","location"]   
pickle_file = open("D:/luheng/mydata/truedata.pkl", "rb")
df = pickle.load(pickle_file)
# df = df[(df["status"]!=2)]
# df3=df[["position","expect_position"]]
# print df3
# df3.to_csv("D:/luheng/mypython/HRandpeople.txt",index=False,header=False)
pickle_file.close()
print u"读入pkl成功，进行下一步"
# thre = 0.9
# df["position"]=df["position"].fillna(-1)
# df=df[(df["position"]!=-1)]
# for company in df["com"].unique():
#     mycom = df[(df["com"]==company)]
#     for position in mycom["position"].unique():
#     	mypos = df[(df["position"]==position)&(df["com"]==company)]
#     	df.loc[df["position"]==position,"positionlen"]=1.0/len(mypos)
#     passnum = mycom[(mycom["status"]==1)]
#     failurenum =  mycom[(mycom["status"]==0)]
#     if len(mycom)<5:
#         df.loc[df["com"]==company,"comstatus"]=1
#     else:
#         if float(len(passnum))/len(mycom)>thre or float(len(failurenum))/len(mycom)>thre:
#             df.loc[df["com"]==company,"comstatus"]=0
#         else :
#             df.loc[df["com"]==company,"comstatus"]=1
#     df.loc[df["com"]==company,"comstatus2"]=max(float(len(passnum))/len(mycom),float(len(failurenum))/len(mycom))           
# df = df[(df["comstatus"]==1)]   
# print df["positionlen"]
# print df
# df.to_csv("D:/luheng/mypython/HRpeople.csv",index=False)
# df["my"]=2.718281828459 
# dfwanghui=df[["workexp","projectexp","my","long_desc"]]
# print dfwanghui
# dfwanghui.to_csv("D:/luheng/mypython/towanghui.txt",index=False,header=False)
# print u"给王会的文件写入成功！"
# dfchenge=df[["industry","position","long_desc"]]
# print dfchenge
# dfchenge.to_csv("D:/luheng/mypython/dfchenge.txt",index=False,header=False)
# dfchenge=df[["expect_industry","expect_position","expect_spec","workexp","projectexp"]]
# print dfchenge
# dfchenge.to_csv("D:/luheng/mypython/dfchenge22.txt",index=False,header=False)
# print u"给陈戈的文件写入成功！"
df = df[(df["peoplejob2"]!="dosomething")]
df = df[(df["hrjob2"]!="dosomething")]
df=df[(df["simi"]!=-1)]
# df = df[(df["hrjob1"]=="计算机-互联网-通信-电子")]
# df.to_csv("D:/luheng/mypython/HRpeople.csv",index=False)
df.loc[df["hrjob1"] == df["peoplejob1"], "job1"] = 1
df.loc[df["hrjob1"] != df["peoplejob1"], "job1"] = 0
df.loc[df["hrjob2"] == df["peoplejob2"], "job2"] = 1
df.loc[df["hrjob2"] != df["peoplejob2"], "job2"] = 0
change= ["sex", "age", "workexp_months", "job_exp", "marriage", "school_level", "degree_level",
              "job_degree_level", "salary_type", "latest_workexp_job_salary", "expect_salary", "location","job1","job2","simi","status"]   
df[change] = df[change].astype(float)
df.loc[(df["hrjob1"]==u"计算机-互联网-通信-电子"),"job"]=0
df.loc[(df["hrjob1"]==u"人事-行政-高级管理"),"job"]=1
df.loc[(df["hrjob1"]==u"会计-金融-银行-保险"),"job"]=2
df.loc[(df["hrjob1"]==u"销售-客服-技术支持"),"job"]=3
df.loc[(df["hrjob1"]==u"广告-市场-媒体-艺术"),"job"]=4
df.loc[(df["hrjob1"]==u"建筑-房地产"),"job"]=5
df.loc[(df["hrjob1"]==u"服务业"),"job"]=6
df.loc[(df["hrjob1"]==u"公务员-翻译-其他"),"job"]=7
df.loc[(df["hrjob1"]==u"生物-制药-医疗-护理"),"job"]=8
df.loc[(df["hrjob1"]==u"咨询-法律-教育-科研"),"job"]=9
df.loc[(df["hrjob1"]==u"生产-营运-采购-物流"),"job"]=10
# df = df[(df["job"]==0)]
#计算机-互联网-通信-电子 人事-行政-高级管理  会计-金融-银行-保险 销售-客服-技术支持   广告-市场-媒体-艺术   建筑-房地产  服务业 公务员-翻译-其他 生物-制药-医疗-护理  咨询-法律-教育-科研 生产-营运-采购-物流
# df = df[(df["workexp_months"]<300)]
# df = df[(df["expect_salary"]<20000)]
# df = df[(df["latest_workexp_job_salary"]<20000)]
# df = df[(df["salary_type"]<20000)]
# df = df[(df["workexp_months"]>0)]
# df = df[(df["expect_salary"]>1000)]
# df2 = df[(df["job2"]==0)&(df["status"]==1)&(df["job1"]==1)]
# df3 = df[(df["job2"]==0)&(df["status"]==0)&(df["job1"]==1)]
# df4 = df[(df["job2"]==1)&(df["status"]==0)]
# df5 = df[(df["job2"]==1)&(df["status"]==1)]
# print len(df)
# print len(df2)
# print len(df3)
# print len(df4)
# print len(df5)
df.loc[(df["job_exp"] == 0)&(df["workexp_months"] <= 0), "exp"] = 1
df.loc[(df["job_exp"] == 0)&(df["workexp_months"] > 0), "exp"] = 1/df["workexp_months"]
df.loc[(df["job_exp"] > 0)&(df["workexp_months"] <= 0), "exp"] = 1/df["job_exp"]
df.loc[(df["job_exp"] > 0)&(df["workexp_months"] > 0)&(df["workexp_months"]>=df["job_exp"] ), "exp"] = 1
df.loc[(df["job_exp"] > 0)&(df["workexp_months"] > 0)&(df["workexp_months"]<df["job_exp"] ), "exp"] = df["workexp_months"]/df["job_exp"]
df.loc[(df["job_degree_level"]==0)&(df["degree_level"]==0),"degree"]=1
df.loc[(df["job_degree_level"]==0)&(df["degree_level"]>0),"degree"]=0
df.loc[(df["job_degree_level"]==1)&((df["degree_level"]==1)|(df["degree_level"]==2)),"degree"]=1
df.loc[(df["job_degree_level"]==1)&((df["degree_level"]!=1)&(df["degree_level"]!=2)),"degree"]=0
df.loc[(df["job_degree_level"]==2)&((df["degree_level"]==2)|(df["degree_level"]==3)),"degree"]=1
df.loc[(df["job_degree_level"]==2)&((df["degree_level"]!=2)&(df["degree_level"]!=3)),"degree"]=0
df.loc[(df["job_degree_level"]==3)&((df["degree_level"]==3)|(df["degree_level"]==4)),"degree"]=1
df.loc[(df["job_degree_level"]==3)&((df["degree_level"]!=3)&(df["degree_level"]!=4)),"degree"]=0
df.loc[(df["job_degree_level"]==4)&((df["degree_level"]==4)),"degree"]=1
df.loc[(df["job_degree_level"]==4)&((df["degree_level"]!=4)),"degree"]=0
df.loc[(df["salary_type"]==0)|(df["expect_salary"]==0),"salary1"]=1
df.loc[(df["salary_type"]!=0)&(df["expect_salary"]!=0)&(df["salary_type"]>=df["expect_salary"]),"salary1"]=df["expect_salary"]/df["salary_type"]
df.loc[(df["salary_type"]!=0)&(df["expect_salary"]!=0)&(df["salary_type"]<df["expect_salary"]),"salary1"]=df["salary_type"]/df["expect_salary"]
# df["degree"]=df["degree_level"]-df["job_degree_level"]

# print df[["salary_type","latest_workexp_job_salary","expect_salary"]] #haha
# print df["latest_workexp_job_salary"].describe()
# for salary in df["latest_workexp_job_salary"].unique():
#     print salary

df.loc[df["salary_type"] == 0, "salary_type"] = 5500  
df.loc[df["latest_workexp_job_salary"] == 0, "latest_workexp_job_salary"] = 1356
df.loc[df["expect_salary"] == 0, "expect_salary"] = 5500
# df["salary1"]=df["salary_type"]-df["expect_salary"]
df["salary2"]=df["latest_workexp_job_salary"]-df["expect_salary"]
predictors = [ "sex","age", "exp", "marriage", "school_level", "degree_level",
              "degree", "salary1","job1","job2","simi","location"]            
df =df[(df["workexp_months"]<1000)]
# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数

# plt.subplot2grid((2,3),(0,0))
# status_0 = df.sex[df.status == 0].value_counts()
# status_1 = df.sex[df.status == 1].value_counts()
# dfsex=pd.DataFrame({u'推荐':status_1, u'未推荐':status_0})
# dfsex.plot(kind='bar', stacked=True)
# plt.title(u"各性别的推荐情况")
# plt.xlabel(u"性别") 
# plt.ylabel(u"人数") 

# statu = df.marriage[df.status == 0].value_counts()
# statu = df.marriage[df.status == 1].value_counts()
# dfmar=pd.DataFrame({u'推荐':statu, u'未推荐':statu})
# dfmar.plot(kind='bar', stacked=True)
# plt.title(u"婚姻状况的推荐情况")
# plt.xlabel(u"婚姻状况") 
# plt.ylabel(u"人数") 



#人数分布
plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
df.status.value_counts().plot(kind='bar')# 柱状图 
plt.title(u"推荐情况 (1为推荐)") # 标题
plt.ylabel(u"人数") 

#求职者分布
plt.subplot2grid((2,3),(0,1))
df.degree_level.value_counts().plot(kind="bar")
plt.ylabel(u"人数") 
plt.title(u"求职者学历分布")

#年龄分布
plt.subplot2grid((2,3),(0,2))
plt.scatter(df.status, df.age)
plt.ylabel(u"年龄")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title(u"按年龄看推荐分布 (1为推荐)")

#工作经验分布
plt.subplot2grid((2,3),(1,0))
plt.scatter(df.status, df.workexp_months)
plt.ylabel(u"工作经验")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title(u"按工作经验看推荐分布 (1为推荐)")

#相似度密度分布
plt.subplot2grid((2,3),(1,1), colspan=2)
df.simi[df.status == 0].plot(kind='kde')   
df.simi[df.status == 1].plot(kind='kde')
plt.xlabel(u"相似度")# plots an axis lable
plt.ylabel(u"密度") 
plt.title(u"推荐情况的相似度分布")
plt.legend((u'不推荐', u'推荐'),loc='best')

#工资匹配度分布
plt.subplot2grid((3,3),(0,2))
plt.scatter(df.status, df.salary1)
plt.ylabel(u"工资匹配度")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title(u"按工资匹配度看推荐分布 (1为推荐)")



plt.show()
end = time.time()
print u"花费时间：%.2fs" % (end - begin)