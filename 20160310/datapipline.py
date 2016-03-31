# -*- coding: UTF-8 -*-   
# __author__ = 'lz'

import numpy as np
import pandas as pd
import cPickle as pickle
import time
import datetime
import pymysql


# class data():
#     def __init__(self):
#         pass
#
#
#     def read_data(self,path):
#         f = open(path)
#         data = ''
#         reg_date_new = ''
#         post_time_new = ''
#         instance = ''
#         line = f.readline().strip()
#         line = f.readline().strip()
#         while line:
#             dt = line.split(',')
#             model_id,prov_id,city_id,reg_date,report_price,mile_age,post_time,liter,model_year,model_price,che300_price = self.splitline(dt)
#             year,month,day = reg_date.split('-')
#             year1,month1,day1 = post_time.split('-')
#             reg_date_new=str(year)+'-'+str(month)+'-'+str(day)
#             post_time_new=str(year1)+'-'+str(month1)+'-'+str(day1)
#             instance+=model_id+'\t'
#             instance+=prov_id+'\t'
#             instance+=city_id+'\t'
#             instance+=reg_date_new+'\t'
#             instance+=report_price+'\t'
#             instance+=mile_age+'\t'
#             instance+=post_time_new+'\t'
#             instance+=liter+'\t'
#             instance+=model_year+'\t'
#             instance+=model_price+'\t'
#             instance+=che300_price+'\n'
#             line = f.readline().strip()
#         open('errorReport_self.csv','wb').write(instance)













#findindex的用法是返回featureid在feature_set中的索引位置，以数字返回
def findIndex(feature_id,feature_set):
    index=-1
    for _id in feature_set:
        index+=1
        if _id ==feature_id:
            return index

def oneHotEncoding(instance,feature_set,feature_id):
    feature_index = findIndex(feature_id,feature_set)
    for i in range(len(feature_set)):
        if i==feature_index:
            instance+='1'+','
        else:
            instance+='0'+','
    return instance

#从数据表中将model_id,car_source,prov_set,city_set去重
def getIdSet( ):
    model_set=set()
    car_source_set=set()
    prov_set=set()
    city_set=set()
    #读取model_id,car_source,prov_set,city_set
    f_model_id = open('C:/danhua/da_carset_id_Set/da_carset_id_Set/model_id_set_1.csv')
    line_model_id = f_model_id.readline().strip()
    while line_model_id:
        d_model_id = line_model_id
        model_set.add(d_model_id)
        line_model_id = f_model_id.readline().strip()
    #读取car_source
    f_car_source_item = open('C:/danhua/da_carset_id_Set/da_carset_id_Set/car_source_set_1.csv')
    line_car_source = f_car_source_item.readline().strip()
    while line_car_source:
        d_car_source = line_car_source
        car_source_set.add(d_car_source)
        line_car_source = f_car_source_item.readline().strip()
     #prov_set
    f_prov_id = open('C:/danhua/da_carset_id_Set/da_carset_id_Set/prov_set_1.csv')
    line_prov_id = f_prov_id.readline().strip()
    while line_prov_id:
        d_prov_id = line_prov_id
        prov_set.add(d_prov_id)
        line_prov_id = f_prov_id.readline().strip()
     #读取city_set
    f_city_id = open('C:/danhua/da_carset_id_Set/da_carset_id_Set/city_set_1.csv')
    line_city_id = f_city_id.readline().strip()
    while line_city_id:
        d_city_id = line_city_id
        city_set.add(d_city_id)
        line_city_id = f_city_id.readline().strip()
    return model_set,car_source_set,prov_set,city_set



#更换csv格式文件的间隔符
def changeCsv(frompath ):
    from_file = open(frompath)
    line  = from_file.readline().strip()
    line  = from_file.readline().strip()
    instance = ''
    feature = ''
    while line:
        dt = line.split('\t')
        model_id, prov_id, city_id, reg_date, car_source, car_status, mile_age, post_time, liter, model_year, model_price,report_price = splitline1(dt)
        instance+=model_id+'\t'
        instance+=prov_id+'\t'
        instance+=city_id+'\t'
        instance+=reg_date+'\t'
        # instance+=car_source+','
        # instance+=car_status+','
        instance+=mile_age+'\t'
        instance+=post_time.strip()+'\t'
        instance+=liter+'\t'
        instance+=model_year+'\t'
        instance+=model_price+'\t'

        instance+=report_price+'\n'
        line  = from_file.readline().strip()

    feature+=instance
    open('da_car_series_1.csv','wb').write(feature)



#处理csv格式问题
def dealCsv(df):
    # f = open(path)
    line  = df.readline().strip()
    line  = df.readline().strip()
    d1 = datetime.datetime(2016, 3, 3)
    feature = ''
    while line:
        instance = ''
        dt = line.split('\t')
        model_id, prov_id, city_id, reg_date,  mile_age, post_time, liter, model_year, model_price,report_price = splitline1(dt)
        year,month,day=reg_date.split('-')
        d2 = datetime.datetime(int(year),int(month),int(day))
        reg_date_day=(d1-d2).days
        year,month,day=post_time.split('-')
        d2 = datetime.datetime(int(year),int(month),int(day))
        post_date_day=(d1-d2).days
        instance+=prov_id+','
        instance+=city_id+','
        instance+=str(reg_date_day)+','
        instance+=mile_age+','
        instance+=str(post_date_day)+','
        instance+=liter+','
        instance+=model_year+','
        instance+=model_price+','
        instance+=report_price+'\n'
        feature+=instance
        line  = df.readline().strip()
    open('C:/danhua/cheprice_series1.csv','wb').write(feature)







def splitline1(dt):
    model_id = dt[1]
    prov_id = dt[2]
    city_id = dt[3]
    reg_date = dt[4]
    report_price = dt[5]
    mile_age = dt[8]
    post_time = dt[9][:-10]
    liter = dt[10]
    model_year = dt[11]
    model_price = dt[12]
    return  model_id, prov_id, city_id, reg_date,  mile_age, post_time, liter, model_year, model_price,report_price

def splitline2(dt):
    prov_id = dt[2]
    city_id = dt[3]
    reg_date = dt[4]
    report_price = dt[5]

    mile_age = dt[8]
    post_time = dt[9][:-10]
    liter = dt[10]
    model_year = dt[11]
    model_price = dt[12]
    return  prov_id, city_id, reg_date, mile_age, post_time, liter, model_year, model_price,report_price

def splitLine(dt):
    model_id=dt[0]
    prov_id=dt[1]
    city_id=dt[2]
    reg_date=dt[3]
    mile_age=dt[4]
    post_time=dt[5][:10]
    liter =dt[6]
    model_year=dt[7]
    model_price=dt[8]

    price =dt[9]

    return model_id,prov_id,city_id,reg_date,mile_age,post_time,liter,model_year,model_price,price



def PreprocessData(featureFile,path):
    # f = open(path)
    # line=f.readline().strip()
    # line=f.readline().strip()
    data=[]
    feature=''
    d1 = datetime.datetime(2016, 3, 3)
    model_set,car_source_set,prov_set,city_set = getIdSet()


    f = open(path)

    line=f.readline().strip()
    line=f.readline().strip()
    k=0
    while line:
		k+=1
		dt=line.split(',')
		model_id,prov_id,city_id,reg_date,mile_age,post_time,liter,model_year,model_price,price =splitLine(dt)

		year,month,day=reg_date.split('/')
		d2 = datetime.datetime(int(year),int(month),int(day))
		reg_date_day=(d1-d2).days

		year,month,day=post_time.split('/')
		d2 = datetime.datetime(int(year),int(month),int(day))
		post_date_day=(d1-d2).days
		# data.append(dt)
		# if float(price) < float(model_price)*(0.9**(1.*reg_date_day/365))*0.8 or float(price) > float(model_price)*(0.9**(1.*reg_date_day/365))*1.2:
		# 	line=f.readline().strip()
		# 	continue

		instance=''
		# one hot encoing model_id
		instance=oneHotEncoding(instnce,model_set,model_id)
		# instance=oneHotEncoding(instance,car_source_set,car_source)
		instance=oneHotEncoding(instance,prov_set,prov_id)
		instance=oneHotEncoding(instance,city_set,city_id)
		# print instance
		instance+=model_year+','
		instance+=model_price+','
		instance+=liter+','
		# instance+=car_status+','
		instance+=str(reg_date_day)+','
		instance+=str(post_date_day)+','
		instance+=mile_age+','

		instance+=price+'\n'




		# feature+=dt[2]+','+dt[3]+','+dt[4]+','+dt[5]+','+str(d)+','+str(index)+','+dt[9]+','+dt[10]+','+dt[7]+'\n'
		# webSource.add(dt[8])
		# print d
		# 28 23 31 344
		# 27 20 31 248

		# print len(instance[:-1].split(','))

		if k==1:
			print instance
			print len(instance.split(','))
		feature+=instance

		line=df.readline().strip()
        
    open(featureFile, 'wb').write(feature)



if __name__=='__main__':

    # conn=pymysql.connect(host="139.129.97.251",user="majian",passwd="MjAn@9832#",db="majian",charset="utf8")
    # cursor = conn.cursor()
    # sql= "select model_id,prov_id,city_id,reg_date,mile_age,post_time,liter,model_year,model_price,old_eval_price from da_car_series_i limit 1,1001"
    # cursor.execute(sql)
    # result = cursor.fetchall()
    # model_id,prov_id,city_id,reg_date,mile_age,post_time,liter,model_year,model_price,old_eval_price=[],[],[],[],[],[],[],[],[],[]
    # for line in result:
    #     model_id.append(line[0])
    #     prov_id.append(line[1])
    #     city_id.append(line[2])
    #     reg_date.append(line[3])
    #     mile_age.append(line[4])
    #     post_time.append(line[5])
    #     liter.append(line[6])
    #     model_year.append(line[7])
    #     model_price.append(line[8])
    #     old_eval_price.append(line[9])
    # df = pd.DataFrame([model_id,prov_id,city_id,reg_date,mile_age,post_time,liter,model_year,model_price,old_eval_price ]).T
    # df = df.rename(columns={0:"model_id" ,1:"prov_id",2:"city_id",3:"reg_date",4:"mile_age",5:"post_time",6:"liter",7:"model_year",8:"model_price",9:"old_eval_price"})




    # getIdSet('da_car_series_1202.csv')
    # changeCsv('da_car_series_1202.csv')
    # dealCsv('../data/da_car_series_1.csv')
    PreprocessData('C:/danhua/da_carset_features/da_carset_features/fea_da_car_series_1.csv',"C:/danhua/predict_price_series/predict_price_series_1.csv")


