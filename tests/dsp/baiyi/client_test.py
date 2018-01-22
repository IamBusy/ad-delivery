#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: client_test.py
@time: 22/01/2018 11:06 AM 
"""  

import os
import unittest
from dsp.baiyi import client


class TestClient(unittest.TestCase):
    def test_set_account(self):
        username = os.getenv('username')
        password = os.getenv('password')
        token = os.getenv('token')
        client.set_account(username, password, token)
        self.assertEqual(client.get_account()['username'], username)
        self.assertEqual(client.get_account()['password'], password)
        self.assertEqual(client.get_account()['token'], token)

    def test_client_init(self):
        print client.get_account()
        c = client.Client(os.getenv('product_line'), os.getenv('version'), os.getenv('service'))
        resp, ok = c._request(os.getenv('action'))
        self.assertTrue(ok)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestClient('test_set_account'))
    suit.addTest(TestClient('test_client_init'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
