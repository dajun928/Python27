#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 2.7.14
@file : __init__.py.py
@time : 2019/03/12 23:46:52
@func : 生成指定年月的日历
"""

import calendar

def get_week_day(i):
  week_day_dict = {
    0 : u'星期一',
    1 : u'星期二',
    2 : u'星期三',
    3 : u'星期四',
    4 : u'星期五',
    5 : u'星期六',
    6 : u'星期天',
  }
  return week_day_dict[i]

def create_calendar(year,month):
    # 生成指定年月的日历
    rets=calendar.monthcalendar(year,month)
    for ret in rets:
        for index,i in enumerate(ret):
            if i!=0:
                print("-"*62+">")
                print(str(year)+u"年"+str(month)+u"月"+str(i)+u"日"+ "  " + get_week_day(index))


if __name__ == '__main__':
    year=2019
    month=3
    create_calendar(year,month)






