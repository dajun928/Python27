#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 2.7.14
@file : ApschedulerDemo.py
@time : 2019/03/09 16:19:55
@func : 定时调度工具   APScheduler是一个Python定时任务框架
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from OtherClass import *

#本类的方法
def my_job01():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 设置定时调度本类的方法
    scheduler.add_job(my_job01, 'cron', hour ='16',minute ='20')

    # 设置定时调度其他类的方法
    other = OtherClass()
    scheduler.add_job(other.my_job02, 'cron', hour ='16',minute ='19')

    # 启动调度
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()


