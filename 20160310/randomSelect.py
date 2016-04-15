#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import json
import numpy as np
import re
import time
import csv
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 中文字体兼容
# begin = time.time()
# df = pd.read_csv("D:/luheng/20160310/resume_p2final.csv", index_col=0)
# print len(df)
# df3 = df[df["position"]==3]
# df4 = df[df["position"]!=3]
# print len(df3)
# print len(df4)
# # print df3
# select = np.random.permutation(5000)
# df33= df3.take(select)
# dffinal = pd.concat([df33,df4],ignore_index=True)
# print dffinal
# dffinal.to_csv("D:/luheng/20160310/resumerandomselect.csv",index=False)
# #tianjiaxiugai
# end = time.time()
# print u"花费时间：%.2fs" % (end - begin)

# a=[x for x in range(2)]
# print a
a=1
b=2
print type(a)
print abs(a-b)/min(a,b)<min(a,b)*0.02

# def getDf(data):
#     f = open(data)
#     model_data, prov_data, city_data, reg_data, car_source_data, car_status_data,mile_data, post_data, liter_data, model_year_data, model_price_data, price_data = [
#         ], [], [], [], [], [], [], [], [], [],[],[]
#     line = f.readline().strip()
#     line = f.readline().strip()
#     while line:
#         dt = line.split('   ')
#         # dt= line.split(',')
#         model_id, prov_id, city_id, reg_date,car_source, car_status, mile_age, post_time, liter, model_year, model_price, price = splitLine(dt)
#         model_data.append(model_id)
#         prov_data.append(prov_id)
#         city_data.append(city_id)
#         reg_data.append(reg_date)
#         car_source_data.append(car_source) 
#         car_status_data.append(car_status)
#         mile_data.append(mile_age)
#         post_data.append(post_time)
#         liter_data.append(liter)
#         model_year_data.append(model_year)
#         model_price_data.append(model_price)
#         price_data.append(price)
#         line = f.readline().strip()


#     df = pd.DataFrame([model_data, prov_data, city_data, reg_data,car_source_data, car_status_data, mile_data,
#                    post_data, liter_data, model_year_data, model_price_data, price_data]).T
#     df = df.rename(columns={0: "model_id", 1: "prov_id", 2: "city_id", 3: "reg_date", 4:"car_source",5:"car_status", 
#                         6: "mile_age", 7: "post_time", 8: "liter", 9: "model_year", 10: "model_price", 11: "price"})
#     # return df

#     df.to_csv('C:/danhua/da_carset/df1/da_car_series_1.csv',index=False)
#     df1=pd.read_csv('C:/danhua/da_carset/df1/da_car_series_1.csv')

#     df=pd.concat([df1,df])
#     df.to_csv('C:/danhua/da_carset/df1/da_car_brand_1.csv',index=False)

# if __name__=='__main__':

    
#     start = time.clock()
    
#     i=2
#     df=pd.read_csv('C:/danhua/da_carset/df1/da_car_series_1.csv')
#     while i<30:
#         try:
#             data = "C:/danhua/da_carset/da_car_series_%s.csv"%i
#             df=pd.concat([df,getDf(data)])
#             i+=1
#         except (AttributeError,ValueError,IOError):
#             i+=1
#             print u"出错啦"