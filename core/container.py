#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: handler.py
@time: 17/01/2018 1:10 PM 
"""
__container = {}


def register(name, object):
    __container[name] = object


def resolve(name):
    if name in __container:
        return __container[name]
    return None
