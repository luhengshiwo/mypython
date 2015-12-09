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
from sklearn.covariance import EllipticEnvelope
from sklearn import svm
from sklearn import ensemble
from sklearn.learning_curve import learning_curve
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn import cross_validation
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
# df.loc[df["salary"]<=2000,"salary"]=0
# df.loc[(df["salary"]<=4000)&(df["salary"]>2000),"salary"]=1
# df.loc[(df["salary"]<=6000)&(df["salary"]>4000),"salary"]=2
# df.loc[(df["salary"]<=8000)&(df["salary"]>6000),"salary"]=3
# df.loc[(df["salary"]<=10000)&(df["salary"]>8000),"salary"]=4
# df.loc[(df["salary"]<=20000)&(df["salary"]>10000),"salary"]=5
# df.loc[df["salary"]>20000,"salary"]=6
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
#去除重复数据
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
x1=df[predictors].astype(float)
y1=df["salary"].astype(int)
# print df[["salaryold","salary"]]

#作图来表现支持度
plt.scatter(df["salaryold"],df["salary"])
plt.xlim(0,30000)
plt.ylim(0,30000)
plt.xlabel("salaryold")
plt.ylabel("salary")
plt.title( "salaryold and salary" )
plt.show()
#离群点检测
# clf=EllipticEnvelope()
# clf=svm.OneClassSVM(kernel="linear")
# clf.fit(x1)
# a =clf.predict(x1)
# d=0
# for x in a:
#     if x==1:
#         d+=1
# print len(a),d     
#以下是两个dataframe合并的方法，在书本的191页有详细说明   
# df2=pd.DataFrame([a]).T
# df2=df2.rename(columns ={0:"outlier"})
# index=np.arange(688)
# df = df.set_index(index)
# df3=pd.merge(df,df2,left_index=True,right_index=True)
# df3=df3[(df3["outlier"]==1)]
# predictors=["school","experience","degree","gender","age","jobtitle","salaryold"]
# x=df3[predictors].astype(float)
# y=df3["salary"].astype(int)    
end = time.time()
print u"花费时间：%.2fs"%(end-begin)