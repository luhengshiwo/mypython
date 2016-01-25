#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import pickle
import numpy as np
import scipy as sp
import pandas as pd
import json
import time
import os
import re
import sys
import cPickle
# from sklearn import tree
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
begin = time.time()
# source = sys.argv[1]
source = "D:/luheng/mydata/jobResumes"#json文件所在目录
data = open(source)
x=[]
peopleid=[]
for line in  data:
	result = json.loads(line)
	sex ,age,workexp_months, exp, marriage, school_level, degree_level,degree, salary_type, latest_workexp_job_salary, salary1,salary2,job1,job2,simi,location=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

	#sex
	if result["resume"]["sex"] == "男":
	    sex = 0 
	elif result["resume"]["sex"] == "女":
	    sex = 1    
	#age    
	try:
	    age=2016 - time.strptime(result["resume"]["dateofbirth"], "%Y-%m-%d")[0]
	except:
	    age=27
	#workexp_months    
	workexp_months = result["resume"]["workexp_months"] 
	#exp
	job_exp=0
	job_exp_notnum = result["job"]["job_exp"]
	if  job_exp_notnum == "实习生":
		job_exp = 0
	elif  job_exp_notnum == "应届毕业生":
		job_exp = 0
	elif  job_exp_notnum == "学生兼职/假期工":
		job_exp = 0
	elif job_exp_notnum == "1年以上":
		job_exp = 12
	elif job_exp_notnum == "2年以上":
		job_exp = 24
	elif job_exp_notnum == "3年以上":
		job_exp = 36
	elif job_exp_notnum == "5年以上":
		job_exp = 60
	elif job_exp_notnum == "8年以上":
		job_exp = 96
	elif job_exp_notnum == "10年以上":
		job_exp = 120									
	if job_exp==0:
		if workexp_months<=0:
			exp=1
		else :
		    exp=1.0/workexp_months
	elif job_exp>0:
	    if workexp_months<=0:
	        exp = 1.0/job_exp
	    elif workexp_months>0:
	        if workexp_months>=job_exp:
	            exp = 1
	        elif workexp_months<job_exp:    
	            exp = workexp_months/job_exp    	    	
	#marriage
	marriage_notnum = result["resume"]["marriage"]
	if marriage_notnum == "未婚":
		marriage =1
	elif marriage_notnum == "已婚未育":
	    marriage = 2	
	elif marriage_notnum == "已婚已育":
	    marriage = 3
	else :
	    marriage = 4  
	#school_level          
	school_level =  result["resume"]["school_level"] 
	#degree_level
	degree_level_notnum = result["resume"]["degree_level"] 
	degree_level = 1
	if degree_level_notnum =="中技" or degree_level_notnum =="中专" or degree_level_notnum =="初中" or degree_level_notnum =="初中及以下" or degree_level_notnum =="高中":
		degree_level =0
	elif degree_level_notnum =="大专" or degree_level_notnum =="":
		degree_level =1
	elif degree_level_notnum =="本科" :
		degree_level =2
	elif degree_level_notnum =="硕士" :
		degree_level =3
	elif degree_level_notnum =="博士" or degree_level_notnum =="MBA":
		degree_level =3	
	elif degree_level_notnum =="博士后" :
		degree_level =4	
	#degree
	degree = 0
	job_degree_level_notnum = result["job"]["job_degree_level"] 
	job_degree_level = 1
	if job_degree_level_notnum == "初中" or job_degree_level_notnum == "中技" or job_degree_level_notnum == "中专" or job_degree_level_notnum == "高中":
		job_degree_level =0
	elif job_degree_level_notnum == "大专" or job_degree_level_notnum == "其他"	:
		job_degree_level=1
	elif job_degree_level_notnum == "本科":
		job_degree_level=2
	elif job_degree_level_notnum == "硕士":
		job_degree_level=3	
	elif job_degree_level_notnum == "博士":
		job_degree_level=4	
	if job_degree_level==0:
		if degree_level==0:
			degree =1
		elif degree_level>0:
		    degree =0	
	if job_degree_level==1:
	    if degree_level==1 or degree_level ==2:
	        degree =1	    
	    else:
	    	degree = 0
	if job_degree_level==2:
	    if degree_level==2 or degree_level ==3:
	        degree =1	    
	    else:
	    	degree = 0
	if job_degree_level==3:
	    if degree_level==3 or degree_level ==4:
	        degree =1	    
	    else:
	    	degree = 0 
	if job_degree_level==4:
	    if degree_level==3 or degree_level ==4:
	        degree =1	    
	    else:
	    	degree = 0 
	#salary_type    	   	   	
	salary_type_notnum = result["job"]["salary_type"]
	salary_type = 0
	if salary_type_notnum != None:
	    salary= re.findall(r'(\w*[0-9]+)\w*', salary_type_notnum)
	    if len(salary) == 2:
	        salary_type = (int(salary[0]) + int(salary[1])) / 2
	    elif len(salary) == 1:
	        salary_type = int(salary[0])       
	#latest_workexp_job_salary
	latest_workexp_job_salary_notnum = result["resume"]["latest_workexp_job_salary"]
	latest_workexp_job_salary = 0
	if latest_workexp_job_salary_notnum != None:
	    salary= re.findall(r'(\w*[0-9]+)\w*', latest_workexp_job_salary_notnum)
	    if len(salary) == 2:
	        latest_workexp_job_salary = (int(salary[0]) + int(salary[1])) / 2
	    elif len(salary) == 1:
	        latest_workexp_job_salary = int(salary[0]) 
	#expect_salary       
	expect_salary_notnum = result["resume"]["expect_salary"]
	expect_salary = 0
	if expect_salary_notnum != None:
	    salary= re.findall(r'(\w*[0-9]+)\w*', expect_salary_notnum)
	    if len(salary) == 2:
	        expect_salary = (int(salary[0]) + int(salary[1])) / 2
	    elif len(salary) == 1:
	        expect_salary = int(salary[0]) 
	#salary1
	salary1 =0
	if salary_type ==0 or expect_salary ==0:
		salary1 =1
	elif salary_type>=expect_salary	:
		salary1 = float(expect_salary)/salary_type
	elif salary_type<expect_salary	:
		salary1 = float(salary_type)/expect_salary
	#projectsimi_max
	projectsimi = [pro["text_simility"] for pro in result["resume"]["projectexp"]]
	try: 
	    projectsimi_max = np.amax(projectsimi)
	except:
	    projectsimi_max = 0   
	#np.amax(projectsimi)
	#worksimi_max
	worksimi = [work["text_simility"] for work in result["resume"]["workexp"]] 
	try:
	    worksimi_max = np.amax(worksimi)
	except: 
	    worksimi_max=0    
	#np.amax(worksimi)
	#simi
	simi=max(projectsimi_max,worksimi_max)
	#location
	#job1
	#job2
	x_1 = [sex ,age, exp, marriage, school_level, degree_level,degree, expect_salary, salary1,simi]
	x.append(x_1)
	peopleid.append(result["resume"]["id"])
x = pd.DataFrame(x)
x = x.rename(columns={0:"sex" ,1:"age",2 :"exp",3: "marriage", 4:"school_level",5: "degree_level",6:"degree", 7:"expect_salary", 8:"salary1",9:"simi"})
begin = time.time()
path = "D:/luheng/mydata"
# path = "/home/zhangwei/project/datamining/core/"
clf_file = open(path +"\\clf.pkl", "rb")
clf = cPickle.load(clf_file)
clf_file.close()
# tree.export_graphviz(clf,out_file = "D:/luheng/mypython/tree.dot")
# with open("D:/luheng/mypython/tree.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f) 
xmean_file = open(path +"\\xmean.pkl", "rb")
xmean = pickle.load(xmean_file)
xmean_file.close()
xstd_file = open(path +"\\xstd.pkl", "rb")
xstd = pickle.load(xstd_file)
xstd_file.close()
x=(x-xmean)/xstd
y = clf.decision_function(x)
print len(y)
# yp = [y[1] for y in y]
# print yp
# dfj =  pd.DataFrame(yp,columns =["prob"],index =peopleid )
# json = dfj.to_json(orient="index")
# print json
end = time.time()
