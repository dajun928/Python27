#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 
@file : logging_demo.py
@time : 2019/03/25 00:22:21
@func : 
"""
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(level=logging.DEBUG,format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.basicConfig(level=logging.INFO,format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.basicConfig(level=logging.WARNING,format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.basicConfig(level=logging.ERROR,format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.basicConfig(level=logging.CRITICAL,format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")
