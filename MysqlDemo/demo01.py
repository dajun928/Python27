# -*- coding:utf-8 -*-


import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
cur = conn.cursor()