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
begin = time.time()
age,degree,gender,salary1,size1,salary2,size2,salary3,size3,salary4,size4,numb=[],[],[],[],[],[],[],[],[],[],[],[]
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
        print u"有异常"
    	age.append(30)           
    degree.append(data[u"degree"])
    gender.append(data[u"gender"])
    salaryavg = 0
    num = 0
    sizeavg = 0 
    for workexp in data[u"workExperienceList"]:
    	num +=1
        if num ==1:
            salary1.append(workexp[u"salary"])
            size1.append(workexp[u"size"])
        elif num==2:
            salary2.append(workexp[u"salary"])
            size2.append(workexp[u"size"])   
        elif num==3:
            salary3.append(workexp[u"salary"])
            size3.append(workexp[u"size"])
        if num >1:       
    	    salaryavg +=workexp[u"salary"]
    	    sizeavg +=workexp[u"size"]
    numb.append(num)    
    salaryavg = salaryavg/num
    sizeavg = sizeavg/num
    salary4.append(salaryavg)
    size4.append(sizeavg)	
myfile.close()    
df = pd.DataFrame([age,degree,gender,salary1,size1,salary2,size2,salary3,size3,salary4,size4,numb]).T
df=df.rename(columns = {0:'age',1:'degree',2:'gender',3:'salary1',4:'size1',5:'salary2',6:'size2',7:'salary3',8:'size3',9:'salary4',10:'size4',11:'numb'})
df.loc[df["gender"]==u"男","gender"]=0
df.loc[df["gender"]==u"Male","gender"]=0
df.loc[df["gender"]==u"女","gender"]=1
df.loc[df["gender"]==u"Female","gender"]=1
df["gender"]=df["gender"].fillna(0)
predictors = ['age','gender','degree','salary1','size1','salary2','size2','salary3','size3','salary4','size4','numb']
df[predictors]=df[predictors].astype(float)
print df
output = open("D:/luheng/mypython/data.pkl",'wb')
pickle.dump(df,output)
output.close()
print u"成功写入pkl"
end = time.time()
print u"花费时间：%.2fs"%(end-begin)