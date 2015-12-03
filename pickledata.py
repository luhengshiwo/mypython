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
age,degree,gender,salary1,time1,size1,position1,salary2,time2,size2,position2,salary3,time3,size3,position3,salary4,size4,salary5,time5,numb,tag=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
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
    mytag=0
    salary5.append(data[u"workExperienceList"][-1][u"salary"])
    firststartdate = data[u"workExperienceList"][-1][u"start_date"]
    finalenddate=data[u"workExperienceList"][0][u"end_date"]
    if finalenddate==u'至今'or finalenddate==u'今' or finalenddate == u'Present':
        finalenddate = "2015-10"   
    finalend=time.strptime(finalenddate,"%Y-%m")
    if  firststartdate == None:
        firststartdate = "2015-1"
    firststart = time.strptime(firststartdate,"%Y-%m") 
    time5.append((finalend[0]-firststart[0])*12 + (finalend[1]-firststart[1]))   
    for workexp in data[u"workExperienceList"]:
    	num +=1
        if num ==1:
            salary1.append(workexp[u"salary"])
            size1.append(workexp[u"size"])
            position1.append(workexp[u"position_name"])
            enddate=workexp[u'end_date']
            startdate = workexp[u'start_date']
            if enddate==u'至今'or enddate==u'今' or enddate == u'Present':
                enddate = "2015-10"   
            end=time.strptime(enddate,"%Y-%m")
            start = time.strptime(startdate,"%Y-%m")
            month = (end[0]-start[0])*12 + (end[1]-start[1])
            time1.append(month)    
        elif num==2:
            salary2.append(workexp[u"salary"])
            size2.append(workexp[u"size"])
            position2.append(workexp[u"position_name"])
            enddate=workexp[u'end_date']
            startdate = workexp[u'start_date']
            if enddate==u'至今'or enddate==u'今' or enddate == u'Present':
                enddate = "2015-10"  
                mytag=1      
            end=time.strptime(enddate,"%Y-%m")
            start = time.strptime(startdate,"%Y-%m")
            month = (end[0]-start[0])*12 + (end[1]-start[1])
            time2.append(month)               
        elif num==3:
            salary3.append(workexp[u"salary"])
            size3.append(workexp[u"size"])
            position3.append(workexp[u"position_name"])
            enddate=workexp[u'end_date']
            startdate = workexp[u'start_date']
            if enddate==u'至今'or enddate==u'今' or enddate == u'Present'or  enddate == None:
                enddate = "2015-10"
                mytag=1
            if  startdate == None:
                startdate = "2015-1"
                mytag=1   
            end=time.strptime(enddate,"%Y-%m")
            start = time.strptime(startdate,"%Y-%m")
            month = (end[0]-start[0])*12 + (end[1]-start[1])
            time3.append(month) 
        if num >1:       
    	    salaryavg +=workexp[u"salary"]
    	    sizeavg +=workexp[u"size"]
    numb.append(num)    
    salaryavg = salaryavg/num
    sizeavg = sizeavg/num
    salary4.append(salaryavg)
    size4.append(sizeavg)	
    tag.append(mytag)
myfile.close()    
df = pd.DataFrame([age,degree,gender,salary1,time1,size1,position1,salary2,time2,size2,position2,salary3,time3,size3,position3,salary4,size4,numb,tag,salary5,time5]).T
df=df.rename(columns = {0:'age',1:'degree',2:'gender',3:'salary1',4:'time1',5:'size1',6:'position1',7:'salary2',8:'time2',9:'size2',10:'position2',11:'salary3',12:'time3',13:'size3',14:'position3',15:'salary4',16:'size4',17:'numb',18:'tag',19:'salary5',20:'time5'})
df.loc[df["gender"]==u"男","gender"]=0
df.loc[df["gender"]==u"Male","gender"]=0
df.loc[df["gender"]==u"女","gender"]=1
df.loc[df["gender"]==u"Female","gender"]=1
df["gender"]=df["gender"].fillna(0)
predictors = ['age','gender','degree','salary1','time1','size1','salary2','time2','size2','salary3','time3','size3','salary4','size4','numb','tag','salary5','time5']
df[predictors]=df[predictors].astype(float)
df[["age","time1","time2","time3"]]=df[["age","time1","time2","time3"]].astype(int)
df = df[(df["tag"]==0)&(df["age"]>17)&(df["time1"]>0)&(df["time2"]>0)&(df["time3"]>0)]
output = open("D:/luheng/mypython/data.pkl",'wb')
pickle.dump(df,output)
output.close()
print u"成功写入pkl"
end = time.time()
print u"花费时间：%.2fs"%(end-begin)