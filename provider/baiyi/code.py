#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: code.py 
@time: 21/01/2018 10:48 AM 
"""

from client import Client


class CodeService(Client):
    def __init__(self):
        Client.__init__(self, 'bydsp', 'v1', 'CodeService')

    def get_all_category(self):
        self._request('getAllCategory')

    def get_all_region(self):
        self._request('getAllRegion')

