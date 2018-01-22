#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: account.py 
@time: 21/01/2018 11:40 AM 
"""

from client import Client


class AccountService(Client):
    def __init__(self):
        Client.__init__(self, 'bydsp', 'v1', 'AccountService')

    def get_account_info(self):
        return self._request('getAccountInfo')
