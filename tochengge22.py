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
reload(sys)
sys.setdefaultencoding('utf-8')
begin = time.time()
source = "D:/luheng/mypython/parsedata2"
status_id,status_title,name,sex,dateofbirth,workexp_months,marriage,school_name,school_level,major_name,degree_level,expect_jobtype,expect_location,expect_salary,expect_industry,expect_position,expect_spec,latest_workexp_job_salary,latest_workexp_job_industry,latest_workexp_job_spec,latest_workexp_job_position,skill,workexp,projectexp,state,city,industry,position,salary_type,job_degree_level,job_skill,job_exp,long_desc,employment_type=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
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
				dateofbirth.append(data[key]["dateofbirth"])
				workexp_months.append(data[key]["workexp_months"])
				marriage.append(data[key]["marriage"])
				school_name.append(data[key]["school_name"])
				school_level.append(data[key]["school_level"])
				major_name.append(data[key]["major_name"])
				degree_level.append(data[key]["degree_level"])
				expect_jobtype.append(data[key]["expect_jobtype"])
				if data[key]["expect_location"] !="":
				    expect_location.append(data[key]["expect_location"]["city"])
				else :
				    expect_location.append("")    
				expect_salary.append(data[key]["expect_salary"])
				expect_industry.append(data[key]["expect_industry"])
				expect_position.append(data[key]["expect_position"])
				expect_spec.append(data[key]["expect_spec"])
				latest_workexp_job_salary.append(data[key]["latest_workexp_job_salary"])
				latest_workexp_job_industry.append(data[key]["latest_workexp_job_industry"])
				latest_workexp_job_spec.append(data[key]["latest_workexp_job_spec"])
				latest_workexp_job_position.append(data[key]["latest_workexp_job_position"])
				skill.append(data[key]["skill"])
				workexp.append(data[key]["workexp"])
				projectexp.append(data[key]["projectexp"])
				state.append(data[key]["state"])
				city.append(data[key]["city"])
				industry.append(data[key]["industry"])
				position.append(data[key]["position"])
				salary_type.append(data[key]["salary_type"])
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
df = pd.DataFrame([status_id,status_title,name,sex,dateofbirth,workexp_months,marriage,school_name,school_level,major_name,degree_level,expect_jobtype,expect_location,expect_salary,expect_industry,expect_position,expect_spec,latest_workexp_job_salary,latest_workexp_job_industry,latest_workexp_job_spec,latest_workexp_job_position,skill,workexp,projectexp,state,city,industry,position,salary_type,job_degree_level,job_skill,job_exp,long_desc,employment_type]).T
df=df.rename(columns ={0:"status_id",1:"status_title",2:"name",3:"sex",4:"dateofbirth",5:"workexp_months",6:"marriage",7:"school_name",8:"school_level",9:"major_name",10:"degree_level",11:"expect_jobtype",12:"expect_location",13:"expect_salary",14:"expect_industry",15:"expect_position",16:"expect_spec",17:"latest_workexp_job_salary",18:"latest_workexp_job_industry",19:"latest_workexp_job_spec",20:"latest_workexp_job_position",21:"skill",22:"workexp",23:"projectexp",24:"state",25:"city",26:"industry",27:"position",28:"salary_type",29:"job_degree_level",30:"job_skill",31:"job_exp",32:"long_desc",33:"employment_type"}) 
# print df["employment_type"]
# for s in  df["employment_type"].unique():
# 	print s
df2=df[["workexp","projectexp"]]
print df2
df2.to_csv("D:/luheng/mypython/tochenge_people.txt",index=False,header=False)
end = time.time()
print u"花费时间：%.2fs"%(end-begin)