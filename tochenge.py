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
desc=[]
myfile = open("D:/luheng/mypython/out.json",'r') 
for eachline in myfile:
    line = "".join([eachline.rsplit("}" , 1)[0] , "}"]) 
    data = json.loads(line)
    mydesc=""
    # for key in data:
    # 	print key
    for project in data["projectinfo"]:
    	for key in project:
    		mydesc+=project[key]	
    # print data["workexp"]	
    for work in data["workexp"]:
        mydesc+=work[u"job_text"]	
        mydesc+=work[u"job_title"] 
    mydesc =     "".join(mydesc.split())
    desc.append(mydesc.encode("utf-8"))   
myfile.close()
df = pd.DataFrame([desc]).T
df.to_csv("D:/luheng/mypython/tochenge.txt",index=False,header=False)