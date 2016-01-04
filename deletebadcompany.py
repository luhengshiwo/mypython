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
from sklearn import grid_search
import math
# from sklearn.externals.six import StringIO
# import pydot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
predictors = [ "sex","age", "exp", "marriage", "school_level", "degree_level",
              "degree", "salary1","job1","job2","simi","location"]                 
pickle_file = open("D:/luheng/mydata/truedata.pkl", "rb")
df = pickle.load(pickle_file)
# df = df[(df["status"]!=2)]
# df3=df[["position","expect_position"]]
# print df3
# df3.to_csv("D:/luheng/mypython/HRandpeople.txt",index=False,header=False)
pickle_file.close()
print u"读入pkl成功，进行下一步"
print len(df)
print len(df["com"].unique())
for company in df["com"].unique():
    mycom = df[(df["com"]==company)]
    passnum = mycom[(mycom["status"]==1)]
    failurenum =  mycom[(mycom["status"]==0)]
    notknownum =mycom[(mycom["status"]==2)]
    if len(mycom)<5:
        df.loc[df["com"]==company,"comstatus"]=1
    elif (len(passnum)/len(mycom)>0.9) or (len(failurenum)/len(mycom)>0.9) or (len(notknownum)/len(mycom)>0.9):
        df.loc[df["com"]==company,"comstatus"]=0
    else :
        df.loc[df["com"]==company,"comstatus"]=1 
df = df[(df["comstatus"]==1)] 
print len(df)
print len(df["com"].unique())        
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
print len(df)
df.loc[df["hrjob1"] == df["peoplejob1"], "job1"] = 1
df.loc[df["hrjob1"] != df["peoplejob1"], "job1"] = 0
df.loc[df["hrjob2"] == df["peoplejob2"], "job2"] = 1
df.loc[df["hrjob2"] != df["peoplejob2"], "job2"] = 0
change= ["sex", "age", "workexp_months", "job_exp", "marriage", "school_level", "degree_level",
              "job_degree_level", "salary_type", "latest_workexp_job_salary", "expect_salary", "location","job1","job2"]   
df[change] = df[change].astype(int)
df["simi"]=df["simi"].dropna()
print len(df)
# df = df[(df["hrjob1"]==u"计算机-互联网-通信-电子")]
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
# df = df[(df["expect_salary"]<20000)]
# df = df[(df["latest_workexp_job_salary"]<20000)]
# df = df[(df["salary_type"]<20000)]
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
print len(df)
print len(df["com"].unique())
df.to_csv("D:/luheng/mydata/findcomdelete.csv",index=False,header=True)
# # print df.describe()
# # df1=df[(df["status"]==1)]
# # print df1
# # df.to_csv("D:/luheng/mypython/mylook3.csv",index=False,header=True)
# # df1.to_csv("D:/luheng/mypython/mylook2.csv",index=False,header=True)
# x = df[predictors]
# x=(x-x.mean())/x.std()
# y = df["status"]
# # kbest=SelectKBest(f_classif, k=10).fit(x,y)
# # x=kbest.transform(x)
# # print  kbest.get_support()
# # print kbest.scores_
# x_train, x_test, y_train, y_test = cross_validation.train_test_split(
#     x, y, test_size=0.3, random_state=100)
# clf=ensemble.RandomForestClassifier(n_estimators=10)
# # param={"kernel":("rbf","linear","poly","sigmoid")}
# # clf = svm.SVC(cache_size=1000,class_weight="balanced",C=1)
# # clf=grid_search.GridSearchCV(clf,param)
# # clf=linear_model.LogisticRegression()
# # clf = tree.DecisionTreeClassifier(max_leaf_nodes=None)
# # print clf
# # clf = tree.ExtraTreeClassifier()
# # clf=naive_bayes.GaussianNB()
# # clf=ensemble.AdaBoostClassifier()
# # clf=ensemble.GradientBoostingClassifier()
# # scores = cross_validation.cross_val_score(clf,x,y,cv=10)
# # print scores
# clf.fit(x_train, y_train)
# print clf
# # print clf.best_params_
# a=0
# b=0
# for t in y_train:
#     if t == 0 :
#         a+=1
#     elif t ==1 :
#         b+=1	
# c=0   
# d=0
# for t2 in y_test:
#     if t2 == 0 :
#         c+=1
#     elif t2 ==1 :
#         d+=1    
# print u"训练集样本总数：%s,训练集得分：%.4fs" %(len(y_train),clf.score(x_train, y_train))
# # 准确率
# # accuracy_score和clf.score一样，f1是precision和recall的几何平均
# print u"测试集样本总数：%s,测试集得分：%.4fs" %(len(y_test),clf.score(x_test, y_test))
# pred = clf.predict(x_test)
# e=0
# f=0
# for t2 in pred:
#     if t2 == 0 :
#         e+=1
#     elif t2 ==1 :
#         f+=1 
# precision,recall,thresholds=metrics.precision_recall_curve(y_test,pred)
# # print precision
# # print recall
# # print e,f
# x1,x2,x3=precision
# y1,y2,y3=recall
# print u"测试集得分明细如下："
# print u"负样本个数：%s,预测为负样本的个数：%s,其中预测准确个数: %s" %(c,e,int(e-d+d*y2))
# print u"正样本个数：%s,预测为正样本的个数：%s,其中预测准确个数: %s" %(d,f,int(d*y2))  
# print u"准确率：%.4f,召回率: %.4f" %(x2,y2)
# tree.export_graphviz(clf,out_file = "D:/luheng/mypython/tree.dot")
# with open("D:/luheng/mypython/tree.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f) 
# train_sizes = np.linspace(0.1, 1.0, 20)
# train_sizes, train_scores, test_scores = learning_curve(
#     clf, x, y, train_sizes=train_sizes)
# train_scores_mean = np.mean(train_scores, axis=1)
# train_scores_std = np.std(train_scores, axis=1)
# test_scores_mean = np.mean(test_scores, axis=1)
# test_scores_std = np.std(test_scores, axis=1)
# plt.title("Learning Curve with Tree")
# plt.xlabel("Training examples")
# plt.ylabel("Score")
# plt.ylim(0.0, 1.1)
# plt.grid()
# plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
#                  train_scores_mean + train_scores_std, alpha=0.1,
#                  color="r")
# plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
#                  test_scores_mean + test_scores_std, alpha=0.1, color="g")
# plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
#          label="Training score")
# plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
#          label="Cross-validation score")
# plt.legend(loc="best")
# plt.show() 
#############################################################输出分类，合并df
# xy= x_test.join(y_test,how="outer")
# y_true = pd.DataFrame([pred]).T
# y_true = y_true.rename(columns={0:"predictors"})
# y_true.index= xy.index
# mydf= df.join(y_true,how="outer")
# mydf=mydf[(mydf["predictors"]>=0)]
# mydf=mydf[["predictors","status","sex","age", "exp", "marriage", "school_level", "degree_level",
#               "degree", "salary1","job1","job2","simi","location","status","workexp","projectexp","long_desc"]]
# mydf.to_csv("D:/luheng/mydata/job2distinguish.csv",index=False,header=True)
# df["hrjob1"].to_csv("D:/luheng/mydata/job.csv",index=False,header=True)
# print len(mydf)
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
