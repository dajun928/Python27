# -*- coding:utf-8 -*-

import MySQLdb

try:
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='test')
    cur=conn.cursor()
    sname = raw_input("请输入学生姓名：")
    params = [sname]
    result=cur.execute("insert into stu(sname) values(%s)",params)

    print result

    conn.commit()
    cur.close()
    conn.close()
except Exception,e:
    print e.message
