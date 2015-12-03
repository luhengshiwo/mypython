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
data = pd.read_csv("D:/luheng/mypython/school.txt",header=None)
schooldata = data[[1,9]]
schooldata = schooldata.rename(columns={1:"school",9:"degree"})
print schooldata
a =schooldata[(schooldata["school"]=="清华大学")]
print len(a)