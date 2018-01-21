#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: client.py 
@time: 21/01/2018 11:31 AM 
"""


import requests
import json


__global_account = {}


class Client:
    __product_line = None
    __version = None
    __service = None
    __gateway = None
    global __global_account

    def __init__(self, product_line, version, service):
        """
        :param product_line:
        :param version:
        :param service:
        """
        self.__product_line = product_line
        self.__version = version
        self.__service = service
        self.__gateway = "https://api.baidu.com/json/%s/%s/%s/" % \
                         (self.__product_line, self.__version, self.__service)
        self.__username = self.__global_account['username'] if 'username' in self.__global_account else None
        self.__password = self.__global_account['password'] if 'password' in self.__global_account else None
        self.__token = self.__global_account['token'] if 'token' in self.__global_account else None

    def _request(self, action, param=None):
        """
        :param action:
        :param param:
        :return:
        """
        if self.__username is None or self.__password is None or self.__token is None:
            raise Exception('Invalid config for baiyi dsp')

        header = {
            "username": unicode(self.__username, 'utf-8'),
            "password": self.__password,
            "token": self.__token,
            "target": "",
            "accessToken": None,
            "action": None
        }
        response = requests.post(
            self.__gateway + action, data=json.dumps({"header": header, "body": param}), verify=False)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("NETWORK ERROR")

    def set_account(self, username, password, token):
        self.__username = username
        self.__password = password
        self.__token = token


# Define global account info here before using them
def set_account(username, password, token):
    global __global_account
    __global_account['username'] = username
    __global_account['password'] = password
    __global_account['token'] = token


def set_username(username):
    global __global_account
    __global_account['username'] = username


def set_password(password):
    global __global_account
    __global_account['password'] = password


def set_token(token):
    global __global_account
    __global_account['token'] = token
