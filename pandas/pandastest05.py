# -*- coding:utf-8 -*-

# 四、数据输出到数据库保存
from MysqlHelper import MysqlHelper
import MySQLdb
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

list=[]

# sql="select * from student"
sql="select * from dept"

sqlhelper = MysqlHelper('127.0.0.1', 3306, 'test', 'root', '1234')

list=sqlhelper.get_all(sql)

# df=pd.DataFrame(list)
# list.append("a")
# list.append("b")
# list.append("c")
# list.append("d")
# list.append("e")



# print list.decode('unicode-escape')
print list

for ll in list:

    print ll

# rr=list.chain.from_iterable(list)
#
# print rr












































































