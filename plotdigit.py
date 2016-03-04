#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__="luheng"

# Standard scientific Python imports
import matplotlib.pyplot as plt

# Import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics

# The digits dataset
digits = datasets.load_digits()

plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()  

print digits.images