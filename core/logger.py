#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: william wei
@license: Apache Licence
@contact: weixiaole@baidu.com
@file: logger.py
@time: 15/01/2018 1:19 PM
"""

from logbook import Logger, StreamHandler, FileHandler
import sys
import config
import os
import time


__handler = None

__loggers = {}


def __get_log_file():
    log_type = config.get('app.log.type')
    if log_type == 'daily':
        return os.path.join(config.APP_PATH,
                            "storage/logs/ad-delivery-%s.log" % time.strftime('%Y-%m-%d', time.localtime()))
    else:
        return os.path.join(config.APP_PATH, 'storage/logs/ad-delivery.log')


def __init():
    driver = config.get('app.log.driver', 'stderr')
    level = config.get('app.log.level', 'DEBUG').upper()
    global __handler
    global __loggers
    if driver == 'stderr':
        __handler = StreamHandler(sys.stderr, level=level)
    elif driver == 'stdout':
        __handler = StreamHandler(sys.stdout, level=level)
    elif driver == 'file':
        __handler = FileHandler(filename=__get_log_file(), level=level)
    else:
        raise Exception('Invalid driver for log')
    __handler.push_application()
    __loggers['core'] = Logger('Core')


def get(channel):
    if channel not in __loggers:
        __loggers[channel] = Logger(channel)
    return __loggers[channel]


def debug(*args, **kwargs):
    __loggers['core'].debug(*args, **kwargs)


def info(*args, **kwargs):
    __loggers['core'].info(*args, **kwargs)


def notice(*args, **kwargs):
    __loggers['core'].notice(*args, **kwargs)


def warning(*args, **kwargs):
        __loggers['core'].warning(*args, **kwargs)


def error(*args, **kwargs):
    __loggers['core'].error(*args, **kwargs)


def critical(*args, **kwargs):
    __loggers['core'].critical(*args, **kwargs)


__init()

