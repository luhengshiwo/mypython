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
begin = time.time()
df = pd.read_csv("D:/luheng/20160310/resume_p2final.csv", index_col=0)
print len(df)
df3 = df[df["position"]==3]
df4 = df[df["position"]!=3]
print len(df3)
print len(df4)
# print df3
select = np.random.permutation(5000)
df33= df3.take(select)
dffinal = pd.concat([df33,df4],ignore_index=True)
print dffinal
dffinal.to_csv("D:/luheng/20160310/resumerandomselect.csv",index=False)
#tianjiaxiugai
end = time.time()
print u"花费时间：%.2fs" % (end - begin)