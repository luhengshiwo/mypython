#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "luheng"
import os  
  
#1. os.environ['CLASSPATH'] = '/home/aaron/workspace/javatest.jar'  
#2. os.environ['CLASSPATH'] = '/home/aaron/workspace/JavaTest/bin'  
  
import jnius_config  
  
#3. jnius_config.set_classpath('.','/home/aaron/workspace/JavaTest/bin')  
  
from jnius import autoclass  
  
JavaTest = autoclass('com.aaron.JavaTest') 
