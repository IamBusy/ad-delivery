#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: app.py 
@time: 19/01/2018 4:36 PM 
"""
import sys
from material.handler import start_produce_materials

if __name__ == '__main__':
    res = start_produce_materials.delay(None, 1)
    print res.get()
