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
from sklearn.learning_curve import validation_curve
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
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
# kbest=SelectKBest(f_classif, k=11).fit(x,y)
# x=kbest.transform(x)
# print  kbest.get_support()
# print kbest.scores_
#PCA
pca = PCA(n_components=15)
x=pca.fit_transform(x)
x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=10)
clf=ensemble.RandomForestClassifier(n_estimators=50)
#clf=naive_bayes.GaussianNB()
#clf=ensemble.AdaBoostClassifier()
# clf=svm.SVC(kernel="linear")
#clf=linear_model.LogisticRegression()
# clf.fit(x,y)
# print clf.score(x,y)
clf.fit(x_train,y_train)
print clf.score(x_test,y_test)  
# train_scores,valid_scores=validation_curve(clf,x,y,"n_estimators",np.arange(10,150,10))
# print train_scores
# print valid_scores
end = time.time()
print u"花费时间：%.2fs"%(end-begin)