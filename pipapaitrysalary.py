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
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import ensemble
from sklearn import svm
from sklearn import naive_bayes
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.learning_curve import learning_curve
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn.decomposition import PCA
begin = time.time()
salary,school,experience,degree,gender,age,name,jobtitle,salaryold,test=[],[],[],[],[],[],[],[],[],[]
data = pd.read_csv("D:/luheng/mypython/school.txt",header=None)
schooldata = data[[1,9]]
schooldata = schooldata.rename(columns={1:"school",9:"degree"})
myfile = open("D:/luheng/mypython/out.json",'r') 
for eachline in myfile:
    line = "".join([eachline.rsplit("}" , 1)[0] , "}"]) 
    data = json.loads(line)
    try:
        salarynum = re.findall(r'(\w*[0-9]+)\w*',data[u"jobexp"][u"salary"])
        salary.append((int(salarynum[0])+int(salarynum[1]))/2)
    except:
        salary.append(int(salarynum[0]))  
    school.append(data[u"highest_school_name"])
    salaryoldtmp=0
    index=0
    if data[u"workexp"]==[]:
        salaryold.append(0)
    for work in data[u"workexp"]:
        index+=1
        if work[u"job_salary"]!="":
            salaryoldnum=re.findall(r'(\w*[0-9]+)\w*',work[u"job_salary"])
            if len(salaryoldnum) ==2:
                salaryoldtmp = (int(salaryoldnum[0])+int(salaryoldnum[1]))/2
                salaryold.append(salaryoldtmp)
            elif len(salaryoldnum) ==1:
                salaryoldtmp = int(salaryoldnum[0])
                salaryold.append(salaryoldtmp) 
            break
        elif work[u"job_salary"]=="":
            salaryoldtmp=0
            if index == len(data[u"workexp"]) :
                salaryold.append(salaryoldtmp)                 
    exp=data[u"latest_exp"]
    yearindex = exp.find(u"年")
    monthindex = exp.find(u"个月")
    if yearindex >0 and monthindex ==-1:
        expnum=re.findall(r'(\w*[0-9]+)\w*',exp)
        month = int(expnum[0])*12
    elif yearindex ==-1 and monthindex >0:
        expnum=re.findall(r'(\w*[0-9]+)\w*',exp)
        month = int(expnum[0])
    elif yearindex >0 and  monthindex >0:
        expnum=re.findall(r'(\w*[0-9]+)\w*',exp)
        month = int(expnum[0])*12+int(expnum[1]) 
    else :
        month =0           
    experience.append(month)
    degree.append(data[u"highest_degree_level"])
    gender.append(data[u"sex"])
    if data[u"age"]=="":
        age.append(30) 
    else:
        age.append(int(data[u"age"]))
    name.append(data[u"name"])  
myfile.close() 
myfile2 = open("D:/luheng/mypython/jobtitle.txt",'r') 
for line in myfile2:
    index = line.find("|")
    if index>0:
        job=line[1:index]
        jobtitle.append(job.decode("utf-8"))
    else :
        jobtitle.append("")    
myfile2.close()
df = pd.DataFrame([salary,school,experience,degree,gender,age,name,jobtitle,salaryold]).T
df=df.rename(columns ={0:"salary",1:"school",2:"experience",3:"degree",4:"gender",5:"age",6:"name",7:"jobtitle",8:"salaryold"}) 
df.loc[df["salary"]<=2000,"salary"]=0
df.loc[(df["salary"]<=4000)&(df["salary"]>2000),"salary"]=1
df.loc[(df["salary"]<=6000)&(df["salary"]>4000),"salary"]=2
df.loc[(df["salary"]<=8000)&(df["salary"]>6000),"salary"]=3
df.loc[(df["salary"]<=10000)&(df["salary"]>8000),"salary"]=4
df.loc[(df["salary"]<=20000)&(df["salary"]>10000),"salary"]=5
df.loc[df["salary"]>20000,"salary"]=6
# df.loc[df["salaryold"]<=2000,"salaryold"]=0
# df.loc[(df["salaryold"]<=4000)&(df["salaryold"]>2000),"salaryold"]=1
# df.loc[(df["salaryold"]<=6000)&(df["salaryold"]>4000),"salaryold"]=2
# df.loc[(df["salaryold"]<=8000)&(df["salaryold"]>6000),"salaryold"]=3
# df.loc[(df["salaryold"]<=10000)&(df["salaryold"]>8000),"salaryold"]=4
# df.loc[(df["salaryold"]<=20000)&(df["salaryold"]>10000),"salaryold"]=5
# df.loc[df["salaryold"]>20000,"salaryold"]=6
df.loc[df["gender"]==u"男","gender"]=0
df.loc[df["gender"]==u"女","gender"]=1
df.loc[df["gender"]=="","gender"]=0
df = df[(df["degree"]!="")&(df["school"]!="")&(df["jobtitle"]!="")&(df["salaryold"]!=0)]
df = df.drop_duplicates()
df.loc[df["degree"]==u"大专","degree"]=0	
df.loc[df["degree"]==u"中专/技校","degree"]=0
df.loc[df["degree"]==u"中专","degree"]=0
df.loc[df["degree"]==u"高中","degree"]=0
df.loc[df["degree"]==u"本科","degree"]=1
df.loc[df["degree"]==u"硕士","degree"]=2
df.loc[df["degree"]==u"博士","degree"]=2
df.loc[df["degree"]==u"MBA","degree"]=2
for x in df["school"].unique():
    if len(schooldata[(schooldata["school"]==x.encode("utf-8"))])==1:
        degree=schooldata[(schooldata["school"]==x.encode("utf-8"))]["degree"].max()
        df["school"]=df["school"].replace(x,degree)
    else :
        df["school"]=df["school"].replace(x,0)    
df.loc[df["jobtitle"]==u"-计算机-互联网-通信-电子","jobtitle"]=0   
df.loc[df["jobtitle"]==u"-人事-行政-高级管理","jobtitle"]=1  
df.loc[df["jobtitle"]==u"-销售-客服-技术支持","jobtitle"]=2   
df.loc[df["jobtitle"]==u"-建筑-房地产","jobtitle"]=3
df.loc[df["jobtitle"]==u"-广告-市场-媒体-艺术","jobtitle"]=4 
df.loc[df["jobtitle"]==u"-生产-营运-采购-物流","jobtitle"]=5 
df.loc[df["jobtitle"]==u"-会计-金融-银行-保险","jobtitle"]=6    
df.loc[df["jobtitle"]==u"-咨询-法律-教育-科研","jobtitle"]=7    
df.loc[df["jobtitle"]==u"-生物-制药-医疗-护理","jobtitle"]=8    
df.loc[df["jobtitle"]==u"-公务员-翻译-其他","jobtitle"]=9    
df.loc[df["jobtitle"]==u"-服务业","jobtitle"]=10 
predictors=["school","experience","degree","gender","age","jobtitle","salaryold"]
x=df[predictors].astype(float)
y=df["salary"].astype(int)
#######用最适合算法的几个属性
# lrf = ensemble.RandomForestClassifier(n_estimators=20).fit(x, y)
# model = SelectFromModel(lrf, threshold=None, prefit=True)
# x = model.transform(x)
# print model.get_support()
#用对标签贡献最大的k个属性
# kbest=SelectKBest(chi2, k=7).fit(x,y)
# x=kbest.transform(x)
# print  kbest.get_support()
# print kbest.scores_
# ##数据预处理
# x = preprocessing.scale(x) 
#PCA
pca = PCA(n_components=3)
x=pca.fit_transform(x)
print pca.explained_variance_ratio_
x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=100)
# clf=ensemble.RandomForestClassifier(n_estimators=20)
# clf=ensemble.ExtraTreesClassifier(n_estimators=20)
# clf=naive_bayes.GaussianNB()
clf=ensemble.AdaBoostClassifier()
# clf=ensemble.GradientBoostingClassifier()
# clf=linear_model.SGDClassifier()
# clf=svm.SVC(kernel="linear")
# clf=linear_model.LogisticRegression()
# clf=QuadraticDiscriminantAnalysis(store_covariances=True)
# clf=LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
# clf = NearestCentroid()
clf.fit(x_train,y_train)
print clf.score(x_train,y_train)
print clf.score(x_test,y_test)
#画学习曲线图
train_sizes=np.linspace(0.1, 1.0, 20)
train_sizes,train_scores,test_scores=learning_curve(clf,x,y,train_sizes=train_sizes)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
plt.title("Learning Curve with LR")
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