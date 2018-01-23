#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: william wei 
@license: Apache Licence  
@contact: weixiaole@baidu.com
@file: handler.py
@time: 15/01/2018 1:18 PM 
"""
import sys
from celery import Celery
from core import *
from constant import *
app = Celery('app',
             broker=config.get('app.celery.broker'),
             backend=config.get('app.celery.backend'))


"""
All tasks should be defined in this file to
be managed better
"""

logger.get(MODULE_NAME).info("start product materials")

@app.task
@logger.log('Material')
def start_produce_materials(schedule, task_id):
    """
    :param schedule:
    :param task_id:
    :return:

    schedule for material:
    {
        "number": 10,

    }
    """
    print logger.get(MODULE_NAME).debug('34355')
    print >> sys.stderr, schedule
    print logger.get('Material').info(schedule)
    version = schedule['version']
    material_limits = schedule['material']
