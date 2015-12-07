#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import ensemble
from sklearn import svm
from sklearn import naive_bayes
from sklearn.learning_curve import validation_curve
import time
begin = time.time()
pickle_file = open("D:/luheng/mypython/data.pkl","rb")
df = pickle.load(pickle_file)
pickle_file.close()
print u"读入pkl成功，进行下一步" 
df["step1"]=(df["salary1"]-df["salary5"])/(df['time5']-1)  
df["step2"]=(df["salary1"]-df["salary5"])/(df['numb']-1) 
predictors = ['age','degree','gender','salary1','time1','size1','time2','size2','salary3','time3','size3','step2','salary4','size4','numb','time5']
x=df[predictors].astype(float)
y=df['salary2'].astype(int)
clf=ensemble.RandomForestClassifier(n_estimators=50)
param_range=np.arange(10,150,10)
train_scores,test_scores=validation_curve(clf,x,y,"n_estimators",param_range=param_range)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
plt.title("Validation Curve with RF")
plt.xlabel("$n_estimators$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
plt.semilogx(param_range, train_scores_mean, label="Training score", color="r")
plt.fill_between(param_range, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.2, color="r")
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score",
             color="g")
plt.fill_between(param_range, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.2, color="g")
plt.legend(loc="best")
plt.show()
end = time.time()
print u"花费时间：%.2fs"%(end-begin)