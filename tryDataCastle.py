#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import scipy as sp
import pandas as pd
from pandas.io.json import json_normalize
import json
import time
import re
from sklearn import ensemble
import time
begin = time.time()
age,degree,gender,salary,size=[],[],[],[],[]
myfile = open("D:/luheng/mypython/practice.json",'r') 
a=0
for eachline in myfile:
    line = "".join([eachline.rsplit("}" , 1)[0] , "}"]) 
    data = json.loads(line)
    a+=1
    try:
        agenum = re.findall(r'(\w*[0-9]+)\w*',data[u"age"])
        age.append(agenum[0])
    except:
    	age.append(30)           
    degree.append(data[u"degree"])
    gender.append(data[u"gender"])
    salaryavg = 0
    num = 0
    sizeavg = 0
    for workexp in data[u"workExperienceList"]:
    	num +=1
    	salaryavg +=workexp[u"salary"]
    	sizeavg +=workexp[u"size"]
    salaryavg = salaryavg/num
    sizeavg = sizeavg/num
    salary.append(salaryavg)
    size.append(sizeavg)	
myfile.close()    
df = pd.DataFrame([age,degree,gender,salary,size]).T
df=df.rename(columns = {0:'age',1:'degree',2:'gender',3:'salary',4:'size'})
df.loc[df["gender"]==u"男","gender"]=0
df.loc[df["gender"]==u"Male","gender"]=0
df.loc[df["gender"]==u"女","gender"]=1
df.loc[df["gender"]==u"Female","gender"]=1
df["gender"]=df["gender"].fillna(0)
predictors = ['age','gender','degree','size']
x=df[predictors].astype(float)
y=df['salary'].astype(int)
clf=ensemble.RandomForestClassifier(n_estimators=10)
clf.fit(x,y)
score=clf.score(x,y)
print score
end = time.time()
print u"花费时间：%.2fs"%(end-begin)