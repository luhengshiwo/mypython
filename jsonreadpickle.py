#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
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
# from sklearn.externals.six import StringIO
# import pydot
begin = time.time()
predictors=["sex","age","workexp_months","job_exp","marriage","school_level","degree_level","job_degree_level","salary_type","latest_workexp_job_salary","expect_salary","location"]
pickle_file = open("D:/luheng/mypython/truedata.pkl","rb")
df = pickle.load(pickle_file)
pickle_file.close()
print u"读入pkl成功，进行下一步"
x=df[predictors].astype(float)
y=df["status"].astype(int)
kbest=SelectKBest(f_classif, k=4).fit(x,y)
x=kbest.transform(x)
print  kbest.get_support()
print kbest.scores_
x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=100)
# clf=ensemble.RandomForestClassifier(n_estimators=10)
# clf=svm.SVC(kernel="linear")
# clf=linear_model.LogisticRegression()
clf = tree.DecisionTreeClassifier()
print clf
# clf = tree.ExtraTreeClassifier()
# clf=naive_bayes.GaussianNB()
# clf=ensemble.AdaBoostClassifier()
# clf=ensemble.GradientBoostingClassifier()
# scores = cross_validation.cross_val_score(clf,x,y,cv=10)
# print scores
clf.fit(x_train,y_train)
print clf.feature_importances_
# print x_train
# print y_train
print u"训练集得分：%.4fs"%clf.score(x_train,y_train)
#准确率
'''accuracy_score和clf.score一样，f1是precision和recall的几何平均
'''
print u"测试集得分：%.4fs"%clf.score(x_test,y_test)
pred=clf.predict(x_test)
# m_f1=metrics.f1_score(y_test,pred)
m_precision = metrics.precision_score(y_test,pred);  
m_recall = metrics.recall_score(y_test,pred)
# print metrics.accuracy_score(y_test,pred)
# print m_f1
print u"准确率：%.4fs"%m_precision
print u"召回率：%.4fs"%m_recall
#画决策树图
# dot_data = StringIO()
# tree.export_graphviz(clf,out_file=dot_data)
# graph=pydot.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("D:/luheng/mypython/mytree.pdf")
# df["try"]=df["job_exp"]-df["workexp_months"].astype(int)
# print df
# for x in  df["try"].unique():
#     print x  
# print df.describe()
# df2=df[["latest_workexp_job_spec","latest_workexp_job_position","workexp","projectexp"]]
# df3=df[["industry","position"]]
# df3.to_csv("D:/luheng/mypython/HR.txt",index=False,header=False)
#画学习曲线图
# train_sizes=np.linspace(0.1, 1.0, 20)
# train_sizes,train_scores,test_scores=learning_curve(clf,x,y,train_sizes=train_sizes)
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


end = time.time()
print u"花费时间：%.2fs"%(end-begin)