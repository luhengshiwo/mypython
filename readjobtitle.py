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
jobtitle=[]
myfile = open("D:/luheng/mypython/jobtitle.txt",'r') 
for line in myfile:
	index = line.find("|")
	job=line[1:index]
	jobtitle.append(job.decode("utf-8"))
myfile.close()
df1 = pd.DataFrame([jobtitle]).T	
for x in df1[0].unique():
	print x