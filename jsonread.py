#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
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
from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
"""
这个py文件主要是用来读取json文件，并将其量化，存入pkl中
"""
reload(sys)
sys.setdefaultencoding('utf-8')#中文字体兼容
begin = time.time()
source = "D:/luheng/mydata/parsedata"#json文件夹所在目录
status_id, status_title, name, sex, age, workexp_months, marriage, school_name, school_level, major_name, degree_level, expect_jobtype, expect_location, expect_salary, expect_industry, expect_position, expect_spec, latest_workexp_job_salary, latest_workexp_job_industry, latest_workexp_job_spec, latest_workexp_job_position, skill, workexp, projectexp, state, city, industry, position, salary_type, job_degree_level, job_skill, job_exp, long_desc, employment_type, location, sim,hrjob1,hrjob2,peoplejob1,peoplejob2 ,com,myid,comsource= [
], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],[],[],[],[],[],[],[]
hrjob1,hrjob2,peoplejob1,peoplejob2,simi=[],[],[],[],[]#初始化所遇需要的属性
for root, dirs, files in os.walk(source):
    for OneFileName in files:
        if OneFileName.find('.txt') == -1:
            continue
        OneFullFileName = join(root, OneFileName)
        myfile = open(OneFullFileName)#读每一个txt
        for line in myfile:
            data = json.loads(line,strict=False)#分行读每一个json
            for key in data:
                myid.append(data[key]["id"])
                if data[key]["comp_name"] == None:
                    com.append(-1)
                elif "test" in data[key]["comp_name"]:
                    com.append(-1)
                elif  "Test" in data[key]["comp_name"]:
                    com.append(-1) 
                elif  "pipipi" in data[key]["comp_name"]:
                    com.append(-1)     
                elif  "淘贝贝" in data[key]["comp_name"]:
                    com.append(-1)        
                else:    
                    com.append(data[key]["comp_name"])#给测试数据的公司名打标记
                status_id.append(data[key]["status_id"])
                status_title.append(data[key]["status_title"])
                name.append(data[key]["name"])
                sex.append(data[key]["sex"])
                birth = data[key]["dateofbirth"]
                try:
                    age.append(2016 - time.strptime(birth, "%Y-%m-%d")[0])
                except:
                    age.append(0)#年龄
                workexp_months.append(data[key]["workexp_months"])
                marriage.append(data[key]["marriage"])
                school_name.append(data[key]["school_name"])
                school_level.append(data[key]["school_level"])
                major_name.append(data[key]["major_name"])
                degree_level.append(data[key]["degree_level"])
                expect_jobtype.append(data[key]["expect_jobtype"])
                matchcity = ""
                if data[key]["expect_location"] != "":
                    expect_location.append(
                        data[key]["expect_location"]["city"])
                    matchcity += data[key]["expect_location"]["city"]
                else:
                    expect_location.append("")
                if matchcity == "":
                    location.append(1)
                elif city == data[key]["city"]:
                    location.append(1)
                else:
                    location.append(0)#工作地点是否匹配
                nextsalary = 0
                if data[key]["expect_salary"] == u"面议" or data[key]["expect_salary"] == "":
                    nextsalary = 0
                else:
                    salary = re.findall(
                        r'(\w*[0-9]+)\w*', data[key]["expect_salary"])
                    if len(salary) == 2:
                        nextsalary = (int(salary[0]) + int(salary[1])) / 2
                    elif len(salary) == 1:
                        nextsalary = int(salary[0])
                expect_salary.append(nextsalary)#计算期望薪资
                expect_industry.append(data[key]["expect_industry"])
                expect_position.append(data[key]["expect_position"])
                expect_spec.append(data[key]["expect_spec"])
                latest_workexp_job_salary.append(
                    data[key]["latest_workexp_job_salary"])
                latest_workexp_job_industry.append(
                    data[key]["latest_workexp_job_industry"])
                latest_workexp_job_spec.append(
                    data[key]["latest_workexp_job_spec"])
                latest_workexp_job_position.append(
                    data[key]["latest_workexp_job_position"])
                skill.append(data[key]["skill"])
                myworkexp = data[key]["workexp"]
                mywork = ""
                if myworkexp != None:
                    for key1 in myworkexp:
                        mywork += myworkexp[key1]["job_text"]
                        mywork +="2.718281828459" 
                    mywork = "".join(mywork.split())
                else:
                    mywork = "".join("2.718281828459")    
                workexp.append(mywork)#记录每一段工作经验，用e隔开
                myprojectexp = data[key]["projectexp"]
                myproject = ""
                if myprojectexp != None:
                    for key2 in myprojectexp:
                        myproject += myprojectexp[key2]["project_desc"]
                        myproject += myprojectexp[key2]["responsibility"]
                        myproject +="2.718281828459"
                    myproject = "".join(myproject.split())
                else:
                    myproject = "".join("2.718281828459")     
                projectexp.append(myproject)#记录每一段项目经验，用e隔开
                state.append(data[key]["state"])
                city.append(data[key]["city"])
                industry.append(data[key]["industry"])
                position.append(data[key]["position"])
                hrsalary = data[key]["salary_type"]
                hrformysalary = 0
                if hrsalary != None:
                    salary = re.findall(r'(\w*[0-9]+)\w*', hrsalary)
                    if len(salary) == 2:
                        hrformysalary = (int(salary[0]) + int(salary[1])) / 2
                    elif len(salary) == 1:
                        hrformysalary = int(salary[0])
                salary_type.append(hrformysalary)#计算HR提供的薪资
                job_degree_level.append(data[key]["job_degree_level"])
                job_skill.append(data[key]["job_skill"])
                job_exp.append(data[key]["job_exp"])
                mydesc = data[key]["long_desc"]
                if mydesc != None:
                    mydesc = "".join(mydesc.split())
                    mydesc = re.sub('<[^>]+>', '', mydesc)
                    long_desc.append(mydesc)
                else:
                    long_desc.append("")#职位要求
                employment_type.append(data[key]["employment_type"])     
        myfile.close() 
"""打开两个文件，用求职者的职位和HR的职位大类小类做匹配
读取项目经验工作经验和职位要求的相似度
"""        
myfilehr = open("D:/luheng/mydata/myhr.txt",'r') 
for line in myfilehr:
    index1 = line.find("\t")
    if index1!=0:
        job1=line[2:index1-1]
        hrjob1.append(job1.decode("utf-8"))
        index2 = line.find("\t",index1+1)
        job2=line[index1+2:index2-1]
        hrjob2.append(job2.decode("utf-8"))
    else: 
        hrjob1.append("dosomething")    
        hrjob2.append("dosomething")
myfilehr.close()
myfilepeople = open("D:/luheng/mydata/mypeople.txt",'r') 
for line in myfilepeople:
    index1 = line.find("\t")
    if index1!=0:
        job1=line[2:index1-1]
        peoplejob1.append(job1.decode("utf-8"))
        index2 = line.find("\t",index1+1)
        job2=line[index1+2:index2-1]
        peoplejob2.append(job2.decode("utf-8"))
    else: 
        peoplejob1.append("dosomething")    
        peoplejob2.append("dosomething")        
myfilehr.close()      
wanghuifile = open("D:/luheng/mydata/toluhengnew2.txt",'r') 
for line in wanghuifile:
    if line=="数据不全\n":
        simi.append(-1)
    elif line=="文本无意义\n":    
        simi.append(-1)
    else :
        index = line.find("\n")
        score = line[0:index]
        simi.append(float(score))  
wanghuifile.close()                 
df = pd.DataFrame([status_id, status_title, name, sex, age, workexp_months, marriage, school_name, school_level, major_name, degree_level, expect_jobtype, expect_location, expect_salary, expect_industry, expect_position, expect_spec, latest_workexp_job_salary,
                   latest_workexp_job_industry, latest_workexp_job_spec, latest_workexp_job_position, skill, workexp, projectexp, state, city, industry, position, salary_type, job_degree_level, job_skill, job_exp, long_desc, employment_type, location,hrjob1,hrjob2,peoplejob1,peoplejob2,simi,com,myid]).T
df = df.rename(columns={0: "status_id", 1: "status_title", 2: "name", 3: "sex", 4: "age", 5: "workexp_months", 6: "marriage", 7: "school_name", 8: "school_level", 9: "major_name", 10: "degree_level", 11: "expect_jobtype", 12: "expect_location", 13: "expect_salary", 14: "expect_industry", 15: "expect_position", 16: "expect_spec", 17: "latest_workexp_job_salary",
                        18: "latest_workexp_job_industry", 19: "latest_workexp_job_spec", 20: "latest_workexp_job_position", 21: "skill", 22: "workexp", 23: "projectexp", 24: "state", 25: "city", 26: "industry", 27: "position", 28: "salary_type", 29: "job_degree_level", 30: "job_skill", 31: "job_exp", 32: "long_desc", 33: "employment_type", 34: "location",35:"hrjob1",36:"hrjob2",37:"peoplejob1",38:"peoplejob2",39:"simi",40:"com",41:"id"})
"""
建立了DataFrame 框架，后续操作可以用pandas
"""
# df["my"]=2.718281828459 
# dfwanghui=df[["long_desc","my","workexp","projectexp"]]
# print dfwanghui
# dfwanghui.to_csv("D:/luheng/mypython/towanghui.txt",index=False,header=False)
# print u"给王会的文件写入成功！"
# dfchenge=df[["industry","position","long_desc"]]
# print dfchenge
# dfchenge.to_csv("D:/luheng/mypython/myhrbf.txt",index=False,header=False)
# dfchenge=df[["latest_workexp_job_industry","latest_workexp_job_spec","latest_workexp_job_position","workexp","projectexp"]]
# print dfchenge
# dfchenge.to_csv("D:/luheng/mypython/mypeoplebf.txt",index=False,header=False)
# print u"给陈戈的文件写入成功！"
#筛选不合格=18594
# 面试不合格=355
# 已面试=6721
# 面试取消=2019
# 已发offer=126
# 试用期=1238
# 离职=90
# 筛选合格=5315
# 缺席=275
#拒绝offer=250
# 复试=240
# 联系方式无效=14
# 将面试=166
# 接受offer=90
# 面试合格=255
# 已通知落选=220
# 转正=75
# 筛选待定=365
# 辞退=29
# 需再联系=35
df.loc[df["status_title"] == u"筛选不合格", "status"] = 0
df.loc[df["status_title"] == u"面试不合格", "status"] = 1
df.loc[df["status_title"] == u"已面试", "status"] = 1
df.loc[df["status_title"] == u"面试取消", "status"] = 1
df.loc[df["status_title"] == u"已发offer", "status"] = 1
df.loc[df["status_title"] == u"试用期", "status"] = 1
df.loc[df["status_title"] == u"离职", "status"] = 1
df.loc[df["status_title"] == u"筛选合格", "status"] = 1
df.loc[df["status_title"] == u"缺席", "status"] = 1
df.loc[df["status_title"] == u"拒绝offer", "status"] = 1
df.loc[df["status_title"] == u"复试", "status"] = 1
df.loc[df["status_title"] == u"联系方式无效", "status"] = 1
df.loc[df["status_title"] == u"将面试", "status"] = 1
df.loc[df["status_title"] == u"接受offer", "status"] = 1
df.loc[df["status_title"] == u"面试合格", "status"] = 1
df.loc[df["status_title"] == u"已通知落选", "status"] = 1
df.loc[df["status_title"] == u"转正", "status"] = 1
df.loc[df["status_title"] == u"筛选待定", "status"] = 2
df.loc[df["status_title"] == u"辞退", "status"] = 1
df.loc[df["status_title"] == u"需再联系", "status"] = 1
df.loc[df["sex"] == u"M", "sex"] = 0
df.loc[df["sex"] == u"F", "sex"] = 1
df["sex"] = df["sex"].fillna(0)
df.loc[df["age"] <= 1, "age"] = 22
df["workexp_months"] = df["workexp_months"].fillna(0)
df.loc[df["marriage"] == "", "marriage"] = "4"
df.loc[df["marriage"] == u"0", "marriage"] = "4"
df["school_level"] = df["school_level"].fillna("0")
df.loc[df["degree_level"] == u"大专", "degree_level"] = 1
df.loc[df["degree_level"] == u"中技", "degree_level"] = 0
df.loc[df["degree_level"] == u"中专", "degree_level"] = 0
df.loc[df["degree_level"] == u"初中", "degree_level"] = 0
df.loc[df["degree_level"] == u"初中及以下", "degree_level"] = 0
df.loc[df["degree_level"] == u"高中", "degree_level"] = 0
df.loc[df["degree_level"] == "", "degree_level"] = 1
df.loc[df["degree_level"] == u"本科", "degree_level"] = 2
df.loc[df["degree_level"] == u"硕士", "degree_level"] = 3
df.loc[df["degree_level"] == u"博士", "degree_level"] = 4
df.loc[df["degree_level"] == u"博士后", "degree_level"] = 4
df.loc[df["degree_level"] == u"MBA", "degree_level"] = 3
df["degree_level"] = df["degree_level"].fillna(1)
df["latest_workexp_job_salary"] = df["latest_workexp_job_salary"].fillna("0")
df.loc[df["latest_workexp_job_salary"] ==
       "350066", "latest_workexp_job_salary"] = "3500"
df.loc[df["job_degree_level"] == u"大专", "job_degree_level"] = 1
df.loc[df["job_degree_level"] == u"初中", "job_degree_level"] = 0
df.loc[df["job_degree_level"] == u"中技", "job_degree_level"] = 0
df.loc[df["job_degree_level"] == u"中专", "job_degree_level"] = 0
df.loc[df["job_degree_level"] == u"高中", "job_degree_level"] = 0
df.loc[df["job_degree_level"] == u"本科", "job_degree_level"] = 2
df.loc[df["job_degree_level"] == u"硕士", "job_degree_level"] = 3
df.loc[df["job_degree_level"] == u"博士", "job_degree_level"] = 4
df.loc[df["job_degree_level"] == u"其他", "job_degree_level"] = 1
df[["job_degree_level"]] = df[["job_degree_level"]].fillna(3)
df.loc[df["job_exp"] == u"实习生", "job_exp"] = 0
df.loc[df["job_exp"] == u"应届毕业生", "job_exp"] = 0
df.loc[df["job_exp"] == u"学生兼职/假期工", "job_exp"] = 0
df.loc[df["job_exp"] == u"1年以上", "job_exp"] = 12
df.loc[df["job_exp"] == u"2年以上", "job_exp"] = 24
df.loc[df["job_exp"] == u"3年以上", "job_exp"] = 36
df.loc[df["job_exp"] == u"5年以上", "job_exp"] = 60
df.loc[df["job_exp"] == u"8年以上", "job_exp"] = 96
df.loc[df["job_exp"] == u"10年以上", "job_exp"] = 120
df[["job_exp"]] = df[["job_exp"]].fillna(0)
df=df[(df["degree_level"]==0)|(df["degree_level"]==1)|(df["degree_level"]==2)|(df["degree_level"]==3)]
df = df[(df["status"]!=2)]   
df = df[(df["com"]!=-1)]
df = df.drop_duplicates(["name","com"])  #按名字和公司去重
output = open("D:/luheng/mydata/truedata.pkl", 'wb')
pickle.dump(df, output)
print u"成功写入pkl"
df.to_csv("D:/luheng/mydata/findcom.csv",index=False,header=True)
"""
上述过程对数据进行了预处理，并将结果存入pkl
"""
# predictors = ["sex", "age", "workexp_months", "job_exp", "marriage", "school_level", "degree_level",
#               "job_degree_level", "salary_type", "latest_workexp_job_salary", "expect_salary","simi" ,"location"]   
# # for x in df["job_degree_level"].unique():
# #     print x
# x = df[predictors]
# y = df["status"]
# # kbest = SelectKBest(f_classif, k=10).fit(x, y)
# # x = kbest.transform(x)
# # print kbest.get_support()
# # print kbest.scores_
# x_train, x_test, y_train, y_test = cross_validation.train_test_split(
#     x, y, test_size=0.3, random_state=100)
# # clf=ensemble.RandomForestClassifier(n_estimators=10)
# # clf=svm.SVC(kernel="linear")
# # clf=linear_model.LogisticRegression()
# clf = tree.DecisionTreeClassifier()
# # scores = cross_validation.cross_val_score(clf,x,y,cv=10)
# # print scores
# clf.fit(x_train, y_train)
# # print x_train
# # print y_train
# print clf.score(x_train, y_train)
# print clf.score(x_test, y_test)
# 画决策树图
# tree.export_graphviz(clf,outfile = "D:/luheng/mypython/tree.dot")
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
# # 画学习曲线图
# train_sizes = np.linspace(0.1, 1.0, 20)
# train_sizes, train_scores, test_scores = learning_curve(
#     clf, x, y, train_sizes=train_sizes)
# train_scores_mean = np.mean(train_scores, axis=1)
# train_scores_std = np.std(train_scores, axis=1)
# test_scores_mean = np.mean(test_scores, axis=1)
# test_scores_std = np.std(test_scores, axis=1)
# plt.title("Learning Curve with Tree")
# plt.xlabel("Training examples")
# plt.ylabel("Score")
# plt.ylim(0.0, 1.1)
# plt.grid()
# plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
#                  train_scores_mean + train_scores_std, alpha=0.1,
#                  color="r")
# plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
#                  test_scores_mean + test_scores_std, alpha=0.1, color="g")
# plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
#          label="Training score")
# plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
#          label="Cross-validation score")
# plt.legend(loc="best")
# plt.show()
end = time.time()
print u"花费时间：%.2fs" % (end - begin)
