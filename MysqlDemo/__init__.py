#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='1234',db='test')
cur = conn.cursor()
cur.execute('select * from stu')



cur.fetchall()

cur.close()
conn.close()
