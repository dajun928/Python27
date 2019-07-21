# -*- coding:utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
cur = conn.cursor()


# import records
#
# db = records.Database('mysql://root:1234@127.0.0.1:3306/test')
# rows = db.query('select * from stu')    # or db.query_file('sqls/active-users.sql')
# print rows.dataset


