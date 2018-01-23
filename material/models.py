#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: models.py 
@time: 19/01/2018 1:21 PM 
"""
from orator import Model
from core import config, db
Model.set_connection_resolver(db.get_mysql_client(config.get('material.db.mysql')))


class Material(Model):
    """
    原始物料信息
    """
    pass


class Creative(Model):
    """
    创意，即由原始物料产出的用于最终投放的广告创意
    """
    pass

