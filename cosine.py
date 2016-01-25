#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"

from math import sqrt
import json
import numpy as np
import re
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容 
# source= sys.argv[1]
source = "D:/luheng/mydata/jobResumes4"#json文件所在目录
data = open(source)
x=[]
y=[]
peoid=[]
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
	if result["resume"]["expect_location"] == result["job"]["city"]:
		location=1
	else :
	    location=0		
	#job1
	if result["resume"]["latest_workexp_job_spec"] ==result["job"]["position_spec"]:
		job1=1
	else :
	    job1=0	
	#job2    
	if result["resume"]["latest_workexp_job_position"] ==result["job"]["position"]:
		job2=1
	else :
	    job2=0    

	#industry
	if result["resume"]["latest_workexp_job_industry"] ==result["job"]["industry"]:
		industry=1
	else :
	    industry=0
	#id
	peopleid = result["resume"]["id"]     
	peoid.append(peopleid)
	x_1 = [industry,job1,job2,exp, degree, salary1,location,simi,peopleid]
	x.append(x_1)
# for cov in x :
# 	print cov[0:-1]
# y = [1,1,1,1,1,1,1]
# print y	

def cosdist(x):
	x_up=0
	x_down=0
	for a in x:
		x_up+=a
		x_down +=a**2
	if x_down==0:
		return 0
	else :
	    return x_up/sqrt(x_down*7)
# answer  = {}
# i =1
# for cov in x :
# 	answer[cov[-1]] = cosdist(cov[0:-2]) *cov[-2]
# 	i+=1
# answer =  sorted(answer.iteritems(), key=lambda d:d[1], reverse = True )	
# print answer
for cov in x : 
	y.append(cosdist(cov[0:-2]) *cov[-2])
dfj =  pd.DataFrame(y,columns =["cosine"],index =peoid )
answer = dfj.to_json(orient="index")
print answer

    