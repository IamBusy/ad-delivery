#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: config.py 
@time: 15/01/2018 11:27 AM 
"""

import toml
import os
import container

APP_PATH = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

__config = {}

for p, d, file_lists in os.walk(os.path.join(APP_PATH, 'config')):
    for f in file_lists:
        __config[f.split('.toml')[0]] = toml.load(os.path.join(p, f))


def get(key_str, def_val=None):
    cur = __config
    try:
        for key in key_str.split('.'):
            cur = cur[key]
        return cur
    except Exception as e:
        container.resolve('logger').notice("config key [%s] not found" % key_str)
        return def_val

