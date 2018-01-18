#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: __init__.py.py 
@time: 15/01/2018 10:51 AM 
"""
import config
import logger
from container import register, resolve

__all__ = ['config', 'logger', 'register', 'resolve']
