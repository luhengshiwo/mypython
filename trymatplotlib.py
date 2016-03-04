#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=['SimHei']#用来正常显示中文标签
print u"你好"
x=np.linspace(0,10,1000)
y=np.sin(x)+1
plt.figure(figsize=(8,4))
plt.plot(x,y,label = '$\sinx+1$',color='red',linewidth=2)
plt.xlabel(u"你好")
plt.ylabel("y")
plt.title(u"你好")
plt.ylim(0,2.2)
plt.legend()
plt.show()