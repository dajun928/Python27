# -*- coding:utf-8 -*-

import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
    cs1=conn.cursor()
    count=cs1.execute("insert into stu(sname) values('c')")
    print count
    conn.commit()
    cs1.close()
    conn.close()
except Exception,e:
    print e.message
