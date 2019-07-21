# -*- coding:utf-8 -*-
# 往数据库插入数据
import pandas as pd
from MysqlHelper import MysqlHelper

sqlhelper = MysqlHelper('127.0.0.1', 3306, 'test', 'root', '1234')

params=['1',2,'3']
sql="INSERT INTO stu01(name,age,class) VALUES(%s,%s,%s)"
# sql="INSERT INTO stu01(name,age,class) VALUES('20',20,'20')"

sqlhelper.insert(sql,params)
# f1 = pd.read_sql('tick_data',engine,index_col='date',parse_dates=['date'])

# df.to_sql()

# for i in  df.items():
#     print i[1]

# df.to_csv("te01.csv")