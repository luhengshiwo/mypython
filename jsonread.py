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
import os
from os.path import join
import sys
from sklearn import ensemble
from sklearn import cross_validation
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import f_classif
from sklearn import svm
from sklearn import tree
# from sklearn.externals.six import StringIO
# import pydot
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
source = "D:/luheng/mypython/parsedata2"
status_id,status_title,name,sex,age,workexp_months,marriage,school_name,school_level,major_name,degree_level,expect_jobtype,expect_location,expect_salary,expect_industry,expect_position,expect_spec,latest_workexp_job_salary,latest_workexp_job_industry,latest_workexp_job_spec,latest_workexp_job_position,skill,workexp,projectexp,state,city,industry,position,salary_type,job_degree_level,job_skill,job_exp,long_desc,employment_type,location=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for root, dirs, files in os.walk( source ):
    for OneFileName in files :
        if OneFileName.find( '.txt' ) == -1 :
            continue
        OneFullFileName = join( root, OneFileName )
        myfile = open(OneFullFileName)
        for line in myfile:
            data = json.loads(line)
            for key in data:
				status_id.append(data[key]["status_id"])
				status_title.append(data[key]["status_title"])
				name.append(data[key]["name"])
				sex.append(data[key]["sex"])
				birth = data[key]["dateofbirth"]
				try:
				    age.append(2015-time.strptime(birth, "%Y-%m-%d")[0])
				except:
				    age.append(0) 
				workexp_months.append(data[key]["workexp_months"])
				marriage.append(data[key]["marriage"])
				school_name.append(data[key]["school_name"])
				school_level.append(data[key]["school_level"])
				major_name.append(data[key]["major_name"])
				degree_level.append(data[key]["degree_level"])
				expect_jobtype.append(data[key]["expect_jobtype"])
				matchcity=""
				if data[key]["expect_location"] !="":
				    expect_location.append(data[key]["expect_location"]["city"])
				    matchcity+=data[key]["expect_location"]["city"]
				else :
				    expect_location.append("")   
				if matchcity=="":
				    location.append(1)
				elif city==  data[key]["city"]:
				    location.append(1)
				else:
				    location.append(0)  
				nextsalary = 0
				if data[key]["expect_salary"]==u"面议" or data[key]["expect_salary"]=="":
				    nextsalary =0
				else:
				    salary =re.findall(r'(\w*[0-9]+)\w*',data[key]["expect_salary"])
				    if len(salary)==2:
				    	nextsalary = (int(salary[0])+int(salary[1]))/2
				    elif len(salary)==1:
				        nextsalary=int(salary[0])	
				expect_salary.append(nextsalary)
				expect_industry.append(data[key]["expect_industry"])
				expect_position.append(data[key]["expect_position"])
				expect_spec.append(data[key]["expect_spec"])
				latest_workexp_job_salary.append(data[key]["latest_workexp_job_salary"])
				latest_workexp_job_industry.append(data[key]["latest_workexp_job_industry"])
				latest_workexp_job_spec.append(data[key]["latest_workexp_job_spec"])
				latest_workexp_job_position.append(data[key]["latest_workexp_job_position"])
				skill.append(data[key]["skill"])
				myworkexp=data[key]["workexp"]
				mywork=""
				if myworkexp!=None:
					for key1 in myworkexp:
					    mywork +=  myworkexp[key1]["job_text"]  
					mywork="".join(mywork.split())	    	
					workexp.append(mywork)
				myprojectexp=data[key]["projectexp"]
				myproject=""
				if myprojectexp!=None:
				    for key2 in myprojectexp:
				    	myproject+= myprojectexp[key2]["project_desc"]
				    myproject="".join(myproject.split())	
				    projectexp.append(myproject)			
				state.append(data[key]["state"])
				city.append(data[key]["city"])
				industry.append(data[key]["industry"])
				position.append(data[key]["position"])
				hrsalary= data[key]["salary_type"]
				hrformysalary=0
				if hrsalary != None:
					salary = re.findall(r'(\w*[0-9]+)\w*',hrsalary)
					if len(salary)==2:
						hrformysalary = (int(salary[0])+int(salary[1]))/2
					elif len(salary)==1:
					    hrformysalary = int(salary[0])	
				salary_type.append(hrformysalary)
				job_degree_level.append(data[key]["job_degree_level"])
				job_skill.append(data[key]["job_skill"])
				job_exp.append(data[key]["job_exp"])
				mydesc=data[key]["long_desc"]
				if mydesc!=None:
				    mydesc = "".join(mydesc.split())
				    mydesc = re.sub('<[^>]+>','',mydesc)
				    long_desc.append(mydesc)
				else:
				    long_desc.append("")	
				employment_type.append(data[key]["employment_type"])
        myfile.close()
df = pd.DataFrame([status_id,status_title,name,sex,age,workexp_months,marriage,school_name,school_level,major_name,degree_level,expect_jobtype,expect_location,expect_salary,expect_industry,expect_position,expect_spec,latest_workexp_job_salary,latest_workexp_job_industry,latest_workexp_job_spec,latest_workexp_job_position,skill,workexp,projectexp,state,city,industry,position,salary_type,job_degree_level,job_skill,job_exp,long_desc,employment_type,location]).T
df=df.rename(columns ={0:"status_id",1:"status_title",2:"name",3:"sex",4:"age",5:"workexp_months",6:"marriage",7:"school_name",8:"school_level",9:"major_name",10:"degree_level",11:"expect_jobtype",12:"expect_location",13:"expect_salary",14:"expect_industry",15:"expect_position",16:"expect_spec",17:"latest_workexp_job_salary",18:"latest_workexp_job_industry",19:"latest_workexp_job_spec",20:"latest_workexp_job_position",21:"skill",22:"workexp",23:"projectexp",24:"state",25:"city",26:"industry",27:"position",28:"salary_type",29:"job_degree_level",30:"job_skill",31:"job_exp",32:"long_desc",33:"employment_type",34:"location"}) 
# i=0
# for x in df["status_title"]:
# 	if x == u"面试不合格":
# 		i+=1
# print i	    
# df.loc[df["status_title"]==u"筛选不合格","status"]=0
# df.loc[df["status_title"]!=u"筛选不合格","status"]=1	
for x in df["status_title"].unique():
	print x
df2 = df["status_title"]	
print df2.describe()	

# df.loc[df["status_title"]==u"筛选不合格","status"]=0
# df.loc[df["status_title"]!=u"筛选不合格","status"]=1
# df.loc[df["sex"]==u"M","sex"]=0
# df.loc[df["sex"]==u"F","sex"]=1
# df["sex"]=df["sex"].fillna(0)
# df.loc[df["age"]<1,"age"]=22
# df["workexp_months"]=df["workexp_months"].fillna(0)
# df.loc[df["marriage"]=="","marriage"]="4"
# df.loc[df["marriage"]==u"0","marriage"]="4"
# df["school_level"]=df["school_level"].fillna("0")
# df.loc[df["degree_level"]==u"大专","degree_level"]=1	
# df.loc[df["degree_level"]==u"中技","degree_level"]=0
# df.loc[df["degree_level"]==u"中专","degree_level"]=0
# df.loc[df["degree_level"]==u"初中","degree_level"]=0
# df.loc[df["degree_level"]==u"高中","degree_level"]=0
# df.loc[df["degree_level"]=="","degree_level"]=1
# df.loc[df["degree_level"]==u"本科","degree_level"]=2
# df.loc[df["degree_level"]==u"硕士","degree_level"]=3
# df.loc[df["degree_level"]==u"博士","degree_level"]=3
# df.loc[df["degree_level"]==u"MBA","degree_level"]=3
# df["degree_level"]=df["degree_level"].fillna(1)
# df["latest_workexp_job_salary"]=df["latest_workexp_job_salary"].fillna("0")
# df.loc[df["latest_workexp_job_salary"]=="350066","latest_workexp_job_salary"]="3500"
# df.loc[df["job_degree_level"]==u"大专","job_degree_level"]=1	
# df.loc[df["job_degree_level"]==u"中技","job_degree_level"]=0
# df.loc[df["job_degree_level"]==u"中专","job_degree_level"]=0
# df.loc[df["job_degree_level"]==u"高中","job_degree_level"]=0
# df.loc[df["job_degree_level"]==u"本科","job_degree_level"]=2
# df.loc[df["job_degree_level"]==u"硕士","job_degree_level"]=3
# df.loc[df["job_degree_level"]==u"其他","job_degree_level"]=4
# df[["job_degree_level"]]=df[["job_degree_level"]].fillna(3)
# df.loc[df["job_exp"]==u"实习生","job_exp"]=0	
# df.loc[df["job_exp"]==u"应届毕业生","job_exp"]=-1
# df.loc[df["job_exp"]==u"学生兼职/假期工","job_exp"]=0
# df.loc[df["job_exp"]==u"1年以上","job_exp"]=12
# df.loc[df["job_exp"]==u"2年以上","job_exp"]=24
# df.loc[df["job_exp"]==u"3年以上","job_exp"]=36
# df.loc[df["job_exp"]==u"5年以上","job_exp"]=60
# df.loc[df["job_exp"]==u"8年以上","job_exp"]=96
# df.loc[df["job_exp"]==u"10年以上","job_exp"]=120
# df[["job_exp"]]=df[["job_exp"]].fillna(0)
# predictors=["sex","age","workexp_months","job_exp","marriage","school_level","degree_level","job_degree_level","salary_type","latest_workexp_job_salary","expect_salary","location"]
# x=df[predictors].astype(float)
# y=df["status"].astype(int)
# kbest=SelectKBest(f_classif, k=10).fit(x,y)
# x=kbest.transform(x)
# print  kbest.get_support()
# print kbest.scores_
# x_train, x_test,y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.3,random_state=100)
# # clf=ensemble.RandomForestClassifier(n_estimators=10)
# # clf=svm.SVC(kernel="linear")
# # clf=linear_model.LogisticRegression()
# clf = tree.DecisionTreeClassifier()
# clf.fit(x_train,y_train)
# # print x_train
# # print y_train
# print clf.score(x_train,y_train)
# print clf.score(x_test,y_test)
# dot_data = StringIO()
# tree.export_graphviz(clf,out_file=dot_data)
# graph=pydot.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("D:/luheng/mypython/mytree.pdf")
# df["try"]=df["job_exp"]-df["workexp_months"].astype(int)
# print df
# for x in  df["try"].unique():
#     print x  
# print df.describe()
# df2=df[["latest_workexp_job_spec","latest_workexp_job_position","workexp","projectexp"]]
# df3=df[["industry","position"]]
# df3.to_csv("D:/luheng/mypython/HR.txt",index=False,header=False)
end = time.time()
print u"花费时间：%.2fs"%(end-begin)