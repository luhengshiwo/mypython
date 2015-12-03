#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import pandas as pd
import pickle
from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import ensemble
from sklearn import svm
from sklearn import naive_bayes
import time
begin = time.time()
pickle_file = open("D:/luheng/mypython/data.pkl","rb")
df = pickle.load(pickle_file)
pickle_file.close()
print u"读入pkl成功，进行下一步"
# a=df["position1"].unique()
# print len(a)
# for x in a:
# 	try:
# 	    print x
# 	except:
# 	    print u"error"  
df["step1"]=(df["salary1"]-df["salary5"])/(df['time5']-1)  
df["step2"]=(df["salary1"]-df["salary5"])/(df['numb']-1) 
predictors = ['age','degree','gender','salary1','time1','size1','time2','size2','salary3','time3','size3','step2','salary4','size4','numb','time5']
x=df[predictors].astype(float)
y=df['salary2'].astype(int)
x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=10)
clf=ensemble.RandomForestClassifier(n_estimators=150)
#clf=naive_bayes.GaussianNB()
#clf=ensemble.AdaBoostClassifier()
# clf=svm.SVC(kernel="linear")
#clf=linear_model.LogisticRegression()
clf.fit(x_train,y_train)
print clf.score(x,y)
predictions=clf.predict(x_test)
scores=0.0
#随机猜测的准确率
# a=[ x for x in x_test['salary2']]
# b=[ y for y in y_test]
# for i in range(len(a)):
#     if (a[i]+1)==b[i]:
#         scores+=1
ysalary = [ y for y in y_test]
for i in range(len(predictions)):
    if predictions[i]==ysalary[i]:
        scores+=1	
print scores/len(predictions)   
end = time.time()
print u"花费时间：%.2fs"%(end-begin)