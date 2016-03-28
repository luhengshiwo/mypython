#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
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
pickle_file = open("D:/luheng/mydata/data.pkl", "rb")
df = pickle.load(pickle_file)
pickle_file.close()
print u"读入pkl成功，进行下一步"
df["step1"] = (df["salary1"] - df["salary5"]) / (df['time5'] - 1)
df["step2"] = (df["salary1"] - df["salary5"]) / (df['numb'] - 1)
predictors = ['age', 'degree', 'gender', 'salary1', 'time1', 'size1', 'time2',
              'size2', 'salary3', 'time3', 'size3', 'step2', 'salary4', 'size4', 'numb', 'time5']
x = df[predictors].astype(float)
y = df['salary2'].astype(int)
clf = ensemble.RandomForestClassifier(n_estimators=50)
param_range = np.arange(10, 150, 10)
train_scores, test_scores = validation_curve(
    clf, x, y, "n_estimators", param_range=param_range)
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
print u"花费时间：%.2fs" % (end - begin)


errorNum, allNum, precision = ln.checkOneByOne(
    precision=10, X_test=X, y_test=y, model=model, j=j)
    print
    '''j:'errorNum',erroNum,
            'allNum',allNum
            'precision',precision'''


import numpy as np
import pandas as pd
import cPickle as pickle


class aoTest():

    def __init__(self):
        pass

    def load_data(self, path):
        data = pd.read_csv(path, dtype=np.str, header=None)
        data = np.array(data)
        # X = data[0:,:-1].astype(float)
        X = data[0:, :-1].astype(float)
        y = data[0:, -1].astype(float)
        y = np.ravel(y)
        return X, y

    def load_model(self, model):
        fr = open(model)
        return pickle.load(fr)

    def checkOneByOne(self, precision=5, X_test=None, y_test=None, model=None, j=None):
        erroNum = 0

        y_predict = model.predict(X_test)
        instance = ''
        for i in range(0, len(y_predict)):
            # instance+=str(y_test[i])+'  '+str(y_predict[i])+'\n'
            # print  y[i],y_predict[i]
            if abs(y_test[i] - y_predict[i]) > y_test[i] / 100 * precision:
                erroNum += 1

        # open('predict_price.csv','wb').write(instance)

        return erroNum, len(y_predict), (1 - 1. * erroNum / len(y_predict)) * 100

        # df=pd.read_csv("C:/danhua/predict_price_series1/predict_price_series_1_%s.csv"%j)
        # df["y_predict"]=y_predict
        # df.to_csv("C:/danhua/predict_price_series/predict_price_series_1_%s.csv"%j,index=False)


if __name__ == '__main__':

num, errorNum, allNum, precision = [], [], [], []
    for j in range(1, 2489):
        try:
            ln = aoTest()
            X, y = ln.load_data(
                'C:/danhua/predict_price_feature/fea_da_car_series_1_%s.csv' % j)
            model = ln.load_model(
                'C:/danhua/da_carset_model/da_carset_model/da_car_series_%s.model' % j)
            errormum, allnum, precision = ln.checkOneByOne(
                precision=10, X_test=X, y_test=y, model=model, j=j)
            y_predict = model.predict(X_test)
            print j
            print 'errorNum', erroNum,
            print 'allNum', len(y_predict)
            print 'precision:', (1 - 1. * erroNum / len(y_predict)) * 100
            num.append(j)
            errorNum.append(erroNum)
            allNum.append(len(y_predict))
            precision.append((1 - 1. * erroNum / len(y_predict)) * 100)
        except:
            (AttributeError, ValueError, IOError)
    df = pd.DataFrame([num, errorNum, allNum, precision]).T
    df = df.rename(columns={0: "j", 1: "errorNum",
                            2: "allNum", 3: "precision"})
    df.to_csv()