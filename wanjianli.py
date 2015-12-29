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
# from sklearn.externals.six import StringIO
# import pydot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
hrjob1,hrjob2,peoplejob1,peoplejob2=[],[],[],[]
predictors = [ "sex","age", "workexp_months", "exp", "marriage", "school_level", "degree_level",
              "degree", "salary_type", "latest_workexp_job_salary", "salary1","salary2","job1","job2","simi","location"]   
pickle_file = open("D:/luheng/mypython/truedata.pkl", "rb")
df = pickle.load(pickle_file)
# df = df[(df["status"]!=2)]
# df3=df[["position","expect_position"]]
# print df3
# df3.to_csv("D:/luheng/mypython/HRandpeople.txt",index=False,header=False)
pickle_file.close()
print u"读入pkl成功，进行下一步"
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
              "job_degree_level", "salary_type", "latest_workexp_job_salary", "expect_salary", "location","job1","job2","status"]   
df[change] = df[change].astype(int)
df = df[(df["workexp_months"]<300)]
df = df[(df["expect_salary"]<20000)]
df = df[(df["latest_workexp_job_salary"]<20000)]
df = df[(df["salary_type"]<20000)]
df = df[(df["expect_salary"]>1000)]
# df2 = df[(df["job2"]==0)&(df["status"]==1)&(df["job1"]==1)]
# df3 = df[(df["job2"]==0)&(df["status"]==0)&(df["job1"]==1)]
# df4 = df[(df["job2"]==1)&(df["status"]==0)]
# df5 = df[(df["job2"]==1)&(df["status"]==1)]
# print len(df)
# print len(df2)
# print len(df3)
# print len(df4)
# print len(df5)
df.loc[df["job_exp"] == 0, "job_exp"] = 1
df["exp"] = (df["workexp_months"]-df["job_exp"])
df["degree"]=df["degree_level"]-df["job_degree_level"]
# print df[["salary_type","latest_workexp_job_salary","expect_salary"]] #haha
# print df["latest_workexp_job_salary"].describe()
# for salary in df["latest_workexp_job_salary"].unique():
#     print salary

df.loc[df["salary_type"] == 0, "salary_type"] = 5500
df.loc[df["latest_workexp_job_salary"] == 0, "latest_workexp_job_salary"] = 1356
df.loc[df["expect_salary"] == 0, "expect_salary"] = 5500
df["salary1"]=df["salary_type"]-df["expect_salary"]
df["salary2"]=df["latest_workexp_job_salary"]-df["expect_salary"]
print len(df)
# # print df.describe()
# # df1=df[(df["status"]==1)]
# # print df1
# # df.to_csv("D:/luheng/mypython/mylook3.csv",index=False,header=True)
# # df1.to_csv("D:/luheng/mypython/mylook2.csv",index=False,header=True)
x = df[predictors]
x=(x-x.mean())/x.std()
y = df["status"]
kbest=SelectKBest(f_classif, k=12).fit(x,y)
x=kbest.transform(x)
print  kbest.get_support()
print kbest.scores_
x_train, x_test, y_train, y_test = cross_validation.train_test_split(
    x, y, test_size=0.3, random_state=100)
clf=ensemble.RandomForestClassifier(n_estimators=10)
# clf = svm.SVC()
# clf=linear_model.LogisticRegression()
# clf = tree.DecisionTreeClassifier(max_leaf_nodes=None)
# print clf
# clf = tree.ExtraTreeClassifier()
# clf=naive_bayes.GaussianNB()
# clf=ensemble.AdaBoostClassifier()
# clf=ensemble.GradientBoostingClassifier()
# scores = cross_validation.cross_val_score(clf,x,y,cv=10)
# print scores
clf.fit(x_train, y_train)
a=0
b=0
for t in y_train:
    if t == 0 :
        a+=1
    elif t ==1 :
        b+=1	
c=0   
d=0
for t2 in y_test:
    if t2 == 0 :
        c+=1
    elif t2 ==1 :
        d+=1    
print u"训练集样本总数：%s,训练集得分：%.4fs" %(len(y_train),clf.score(x_train, y_train))
# 准确率
# accuracy_score和clf.score一样，f1是precision和recall的几何平均
print u"测试集样本总数：%s,测试集得分：%.4fs" %(len(y_test),clf.score(x_test, y_test))
pred = clf.predict(x_test)
e=0
f=0
for t2 in pred:
    if t2 == 0 :
        e+=1
    elif t2 ==1 :
        f+=1 
precision,recall,thresholds=metrics.precision_recall_curve(y_test,pred)
x1,x2,x3=precision
y1,y2,y3=recall
print u"测试集得分明细如下："
print u"负样本个数：%s,预测为负样本的个数：%s,其中预测准确个数: %s" %(c,e,int(e-d+d*y2))
print u"正样本个数：%s,预测为正样本的个数：%s,其中预测准确个数: %s" %(d,f,int(d*y2))  
print u"准确率：%.4f,召回率: %.4f" %(x2,y2)
# tree.export_graphviz(clf,out_file = "D:/luheng/mypython/tree.dot")
# with open("D:/luheng/mypython/tree.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)  
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
