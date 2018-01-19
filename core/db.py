#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: db.py 
@time: 19/01/2018 2:31 PM 
"""

from orator import DatabaseManager
from pymongo import MongoClient

# TODO Reuse connections
__clients = {}


def get_mysql_client(config):
    return DatabaseManager({
        'default': 'mysql',
        'mysql': config
    })


def get_mongo_client(config):
    for key in ['user', 'password', 'host', 'port']:
        if key not in config:
            config[key] = None
    if "database" not in config:
        raise Exception('database is necessary when connecting mongodb')

    conn = MongoClient(username=config['user'],
                       password=config['password'],
                       host=config['host'],
                       port=config['port'])
    return conn.config['db']
