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
from sklearn import svm
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import ensemble
from sklearn import svm
from sklearn import naive_bayes
begin = time.time()
salary,school,experience,degree,gender,age,name,jobtitle,salaryold=[],[],[],[],[],[],[],[],[]
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
    # print data[u"latest_job_salary"]
    # salaryold.append(data[u"jobexp"][u"salary"])
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
df = pd.DataFrame([salary,school,experience,degree,gender,age,name,jobtitle]).T
df=df.rename(columns ={0:"salary",1:"school",2:"experience",3:"degree",4:"gender",5:"age",6:"name",7:"jobtitle"}) 
df.loc[df["salary"]<=2000,"salary"]=1
df.loc[(df["salary"]<=4000)&(df["salary"]>2000),"salary"]=1
df.loc[(df["salary"]<=6000)&(df["salary"]>4000),"salary"]=2
df.loc[(df["salary"]<=8000)&(df["salary"]>6000),"salary"]=3
df.loc[(df["salary"]<=10000)&(df["salary"]>8000),"salary"]=4
df.loc[(df["salary"]<=20000)&(df["salary"]>10000),"salary"]=5
df.loc[df["salary"]>20000,"salary"]=6
df.loc[df["gender"]==u"男","gender"]=0
df.loc[df["gender"]==u"女","gender"]=1
df.loc[df["gender"]=="","gender"]=0
df = df[(df["degree"]!="")&(df["school"]!="")&(df["jobtitle"]!="")]
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
predictors=["school","experience","degree","gender","age","jobtitle"]
x=df[predictors].astype(float)
y=df["salary"].astype(int)
# print df[["salary","school","experience","degree","gender","age"]]
# for x in df["degree"].unique():
# 	print x	
x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=10)
clf=ensemble.RandomForestClassifier(n_estimators=100)
# clf=naive_bayes.GaussianNB()
# clf=ensemble.AdaBoostClassifier()
# clf=svm.SVC(kernel="linear")
# clf=linear_model.LogisticRegression()
clf.fit(x_train,y_train)
print clf.score(x,y)
predictions=clf.predict(x_test)
scores=0.0
scores2=0.0
scores3=0.0
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
    if abs(predictions[i]-ysalary[i] )>1:
        scores2+=1     
    else :
        scores3+=1
print scores/len(predictions)  
print scores,scores2,scores3 
end = time.time()
print u"花费时间：%.2fs"%(end-begin)