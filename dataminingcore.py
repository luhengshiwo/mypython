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
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
path= os.path.abspath('.')

# jsondata = sys.argv[1]
# jsondata =''' {"resume":{"latest_workexp_job_industry":"计算机/互联网/通信/电子行业","sex":"男","expect_position":"电信/通信技术开发及应用、软件/互联网开发/系统集成、公","latest_workexp_job_spec":"计算机/互联网/通信/电子","school_name":"南京理工大学","projectexp":[{"text_simility":0.17708943087295356,"project_name":"用户分析模型建模"},{"text_simility":0.3258652209430445,"project_name":"SmartMiner 智能挖掘算法开发"},{"text_simility":0.04561623158518793,"project_name":"IDE 工具开发"}],"expect_salary":"10001-15000","dateofbirth":"1987-04-01","workexp":[{"text_simility":0.22574529760915765,"job_spec":"计算机/互联网/通信/电子","job_title_category":"计算机软件","job_industry_category":"计算机/互联网/通信/电子行业","job_months":"38","job_salary":"8001-10000 元"}],"marriage":"未婚","expect_spec":"","expect_industry":"互联网/电子商务、通信/电信运营、增值服务、计算机软件、 通信/电信/网络设备、政府/公共事业/非盈利机构、交通/运输、学术/科研","expect_location":"江苏 ","name":"张为","workexp_months":36,"degree_level":"硕士","expect_jobtype":"","latest_workexp_job_salary":"8001-10000 元","latest_workexp_job_position":"计算机软件","school_level":0},"job":{"position":"数据挖掘开发工程师","salary_type":"8000-10000","company_id":"111","state":"江苏省","position_spec":"计算机/互联网/通信/电子","job_degree_level":"本科","position_category":"算法工程师","industry":"计算机/互联网/通信/电子行业","job_exp":"1年以上","comp_name":"南京枇杷派网络科技有限公司","city":"南京市"},"skill_sim":0.2}'''

jsondata ='''{"resumes":[{"resume":{"latest_workexp_job_industry":"计算机/互联网/通信/电子行业","sex":"男","expect_position":"电信/通信技术开发及应用、软件/互联网开发/系统集成、公","latest_workexp_job_spec":"计算机/互联网/通信/电子","school_name":"南京理工大学","projectexp":[{"text_simility":0.17708943087295356,"project_name":"用户分析模型建模"},{"text_simility":0.3258652209430445,"project_name":"SmartMiner智能挖掘算法开发"},{"text_simility":0.04561623158518793,"project_name":"IDE工具开发"}],"expect_salary":"10001-15000","dateofbirth":"1987-04-01","workexp":[{"text_simility":0.22574529760915765,"job_spec":"计算机/互联网/通信/电子","job_title_category":"计算机软件","job_industry_category":"计算机/互联网/通信/电子行业","job_months":"38","job_salary":"8001-10000元"}],"marriage":"未婚","expect_spec":"","expect_industry":"互联网/电子商务、通信/电信运营、增值服务、计算机软件、通信/电信/网络设备、政府/公共事业/非盈利机构、交通/运输、学术/科研","expect_location":"江苏","name":"张为","workexp_months":36,"degree_level":"硕士","expect_jobtype":"","latest_workexp_job_salary":"8001-10000元","latest_workexp_job_position":"计算机软件","school_level":0},"job":{"position":"数据挖掘开发工程师","salary_type":"8000-10000","company_id":"111","keywords":[{"weight":1,"word":"数据挖掘"},{"weight":0.39125712471680174,"word":"技术"},{"weight":0.38963393715357275,"word":"数据"},{"weight":0.3752452856649167,"word":"算法"},{"weight":0.36992839726038934,"word":"需求"},{"weight":0.2513875319503111,"word":"产品"},{"weight":0.25041813182915074,"word":"机器"},{"weight":0.21140793821599146,"word":"创新性"},{"weight":0.19533471806201652,"word":"分析"},{"weight":0.19262960663560597,"word":"优先"},{"weight":0.19230138138779726,"word":"平台"},{"weight":0.17364073103526062,"word":"学习"},{"weight":0.1722837787184479,"word":"计划"},{"weight":0.1674611858460714,"word":"保证数据"},{"weight":0.1665932483039919,"word":"挖掘"},{"weight":0.16589938578233165,"word":"代表性"},{"weight":0.16574502084181986,"word":"业务"},{"weight":0.16540898663730688,"word":"方案"},{"weight":0.161745973455111,"word":"原型"},{"weight":0.16114825317993328,"word":"模型"},{"weight":0.15530860188790874,"word":"数学"},{"weight":0.15418886785934915,"word":"定期检查"},{"weight":0.1441781985500781,"word":"有效性"},{"weight":0.13943102341002506,"word":"准确性"},{"weight":0.13376294309467301,"word":"统计学"},{"weight":0.13069435701724497,"word":"研究"},{"weight":0.1251440390238369,"word":"互联网"},{"weight":0.12237251413986476,"word":"python"},{"weight":0.12133377400563719,"word":"产出"},{"weight":0.12017188488966743,"word":"相关"}],"state":"江苏省","position_spec":"计算机/互联网/通信/电子","job_degree_level":"本科","position_category":"算法工程师","industry":"计算机/互联网/通信/电子行业","job_exp":"1年以上","job_skill":["java","python","数据挖掘","机器学习","自然语言处理"],"comp_name":"南京枇杷派网络科技有限公司","city":"南京市"},"skill_sim":0},{"resume":{"latest_workexp_job_industry":"计算机/互联网/通信/电子行业","sex":"","expect_position":"推荐系统项目","latest_workexp_job_spec":"计算机/互联网/通信/电子","school_name":"阜阳大学","projectexp":[],"expect_salary":"面议","dateofbirth":"","workexp":[{"text_simility":0.3020504400219017,"job_spec":"计算机/互联网/通信/电子","job_title_category":"计算机软件","job_industry_category":"计算机/互联网/通信/电子行业","job_months":"3","job_salary":""},{"text_simility":0.1266333754589638,"job_spec":"计算机/互联网/通信/电子","job_title_category":"计算机软件","job_industry_category":"计算机/互联网/通信/电子行业","job_months":"13","job_salary":""}],"marriage":"","expect_spec":"","expect_industry":"计算机/互联网/通信/电子行业","expect_location":"","name":"王亚军","workexp_months":12,"degree_level":"本科","expect_jobtype":"","latest_workexp_job_salary":"","latest_workexp_job_position":"计算机软件","school_level":0},"job":{"position":"数据挖掘开发工程师","salary_type":"8000-10000","company_id":"111","keywords":[{"weight":1,"word":"数据挖掘"},{"weight":0.39125712471680174,"word":"技术"},{"weight":0.38963393715357275,"word":"数据"},{"weight":0.3752452856649167,"word":"算法"},{"weight":0.36992839726038934,"word":"需求"},{"weight":0.2513875319503111,"word":"产品"},{"weight":0.25041813182915074,"word":"机器"},{"weight":0.21140793821599146,"word":"创新性"},{"weight":0.19533471806201652,"word":"分析"},{"weight":0.19262960663560597,"word":"优先"},{"weight":0.19230138138779726,"word":"平台"},{"weight":0.17364073103526062,"word":"学习"},{"weight":0.1722837787184479,"word":"计划"},{"weight":0.1674611858460714,"word":"保证数据"},{"weight":0.1665932483039919,"word":"挖掘"},{"weight":0.16589938578233165,"word":"代表性"},{"weight":0.16574502084181986,"word":"业务"},{"weight":0.16540898663730688,"word":"方案"},{"weight":0.161745973455111,"word":"原型"},{"weight":0.16114825317993328,"word":"模型"},{"weight":0.15530860188790874,"word":"数学"},{"weight":0.15418886785934915,"word":"定期检查"},{"weight":0.1441781985500781,"word":"有效性"},{"weight":0.13943102341002506,"word":"准确性"},{"weight":0.13376294309467301,"word":"统计学"},{"weight":0.13069435701724497,"word":"研究"},{"weight":0.1251440390238369,"word":"互联网"},{"weight":0.12237251413986476,"word":"python"},{"weight":0.12133377400563719,"word":"产出"},{"weight":0.12017188488966743,"word":"相关"}],"state":"江苏省","position_spec":"计算机/互联网/通信/电子","job_degree_level":"本科","position_category":"算法工程师","industry":"计算机/互联网/通信/电子行业","job_exp":"1年以上","job_skill":["java","python","数据挖掘","机器学习","自然语言处理"],"comp_name":"南京枇杷派网络科技有限公司","city":"南京市"},"skill_sim":0}]}'''


result = json.loads(jsondata)
# predictors = [ "sex","age", "workexp_months", "exp", "marriage", "school_level", "degree_level",
#               "degree", "salary_type", "latest_workexp_job_salary", "salary1","job1","job2","simi","location"]   
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
    age=0
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
#np.amax(projectsimi)
#worksimi_max
worksimi = [work["text_simility"] for work in result["resume"]["workexp"]] 
#np.amax(worksimi)
#simi
simi=(np.amax(projectsimi)+np.amax(worksimi))/2
#location
#job1
#job2
x =[[sex ,age, exp, marriage, school_level, degree_level,degree, salary_type, salary1,simi]]
path = "D:\\luheng\\mypython"
clf_file = open(path +"\\clf.pkl", "rb")
clf = pickle.load(clf_file)
clf_file.close()
xmean_file = open(path +"\\xmean.pkl", "rb")
xmean = pickle.load(xmean_file)
xmean_file.close()
xstd_file = open(path +"\\xstd.pkl", "rb")
xstd = pickle.load(xstd_file)
xstd_file.close()

y = clf.predict_proba(x)

print y[0]
print u"花费时间：%.2fs" % (end - begin)