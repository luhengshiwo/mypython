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
from sklearn.learning_curve import learning_curve
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
clf=naive_bayes.GaussianNB()
clf.fit(x,y)
print clf.score(x,y)
train_sizes=np.linspace(0.1, 1.0, 5)
train_sizes,train_scores,test_scores=learning_curve(clf,x,y,train_sizes=train_sizes)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
plt.title("Validation Curve with GB")
plt.xlabel("Training examples")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
plt.grid()
plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                 train_scores_mean + train_scores_std, alpha=0.1,
                 color="r")
plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                 test_scores_mean + test_scores_std, alpha=0.1, color="g")
plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
         label="Training score")
plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
         label="Cross-validation score")
plt.legend(loc="best")
plt.show()
end = time.time()
print u"花费时间：%.2fs"%(end-begin)