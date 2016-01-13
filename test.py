#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
obj = Series([1,2,-3,4])
obj2 = Series([1,2,-3,4],index = ["a","d","b","c"])
obj3=obj2.reindex(list("abcd"))
obj4= DataFrame(np.random.randn(4,6),columns=list("abcdef"),index=list("love"))
a = sys.argv[1]
print a