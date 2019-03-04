#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 2.7.14
@file : tool_0130.py
@time : 2019/03/04 23:55:30
@func : 生成一个指定日期至今的列表
"""
import datetime

def create_assist_date(datestart = None,dateend = None):
	# 创建日期辅助表
	if datestart is None:
		datestart = '20160101'
	if dateend is None:
		dateend = datetime.datetime.now().strftime('%Y%m%d')

	# 转为日期格式
	datestart=datetime.datetime.strptime(datestart,'%Y%m%d')
	dateend=datetime.datetime.strptime(dateend,'%Y%m%d')
	date_list = []
	date_list.append(datestart.strftime('%Y%m%d'))
	while datestart<dateend:
		# 日期叠加一天
	    datestart+=datetime.timedelta(days=+1)
	    # 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y%m%d'))
	print(date_list)

if __name__ == '__main__':

	create_assist_date("20190228")
    # output  ['20190228', '20190301', '20190302', '20190303', '20190304']

