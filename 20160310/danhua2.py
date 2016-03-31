import heapq
import numpy as np
import pandas as pd
import time
import cPickle as pickle
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn import svm
from sklearn import cross_validation
import datetime
import random
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.learning_curve import validation_curve

class Learn():
 
    def __init__(self):
        pass

    def load_data(self,path):
        start = time.clock()
        data=pd.read_csv(path, dtype=np.str)
        start = time.clock()
        data=np.array(data)
        X = data[0:, :-1].astype(np.float)
        start = time.clock()

        y = data[0:, -1].astype(np.float)#*data[0:, -1].astype(np.float)
        y = np.ravel(y)
        return X,y

    def checkOneByOne(self,precision=5,X_test=None,y_test=None,model=None):
        errorNum=0
        y_predict=model.predict(X_test)
        for i in range(0,len(y_predict)):
            print y_test[i],y_predict[i]
            if abs(y_test[i]-y_predict[i])>y_test[i]/100*precision:
                errorNum+=1
        print 
        print 'errorNum:',errorNum,
        print 'allNum:',len(y_predict),
        print 'precision:',(1-1.*errorNum/len(y_predict))*100
        print
    def sampleInstance(self,X,y,sampleRate):
        indexs=[i for i in range(len(y))]
        trainIndexs=random.sample(indexs,int(sampleRate*len(y)))
        testIndexs=[]
        for i in range(len(y)):
            if i not in trainIndexs:
                testIndexs.append(i)

        X_train=X[trainIndexs,:]
        y_train=y[trainIndexs]

        X_test=X[testIndexs,:]
        y_test=y[testIndexs]

        return X_train,y_train,X_test,y_test


    def train(self,path=None, model_path=None, X=None,y=None,clf=None,algorithm='LogisticRegression'):
        # print 'train...'
        # print 'load data'
        if X is None:
            X,y = self.load_data(path)

        print 'instance num:',len(X)

        print 'training...'
        sampleRate = 0.8
        X_train,y_train,X_test,y_test = self.sampleInstance(X,y,sampleRate)

        est = GradientBoostingRegressor(n_estimators=1000,\
            learning_rate=0.005,\
            max_depth=3,\
            random_state=1,\
            loss='huber').fit(X_train, y_train)

        self.dump_model(est,model_path)

        print 'check result:'

    def plt22(self):
        param_range=np.arange(10,150,10)
        X,y=self.load_data("这里面改成你的路径")
        train_scores,test_scores=validation_curve(est,X,y,"n_estimators",param_range=param_range)
        train_scores_mean = np.mean(train_scores, axis=1)
        train_scores_std = np.std(train_scores, axis=1)
        test_scores_mean = np.mean(test_scores, axis=1)
        test_scores_std = np.std(test_scores, axis=1)
        plt.title("Validation Curve with GBR")
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

a=Learn()
a.plt22()