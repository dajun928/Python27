# -*- coding:utf-8 -*-

import pandas as pd
from MysqlHelper import MysqlHelper


sqlhelper = MysqlHelper('127.0.0.1', 3306, 'test', 'root', '1234')
df = pd.read_excel('D:\\work\\isoftstone\\pandastest\\test02.xlsx',sheet_name='Sheet1')

# print df

for index, row in df.iterrows():
    # print row
    # print row['name'], row['age'], row['class']
    # sql = "INSERT INTO stu01(name,age,class) VALUES(%s,%s,%s)".format(row['name'],row['age'],row['class'])
    # sql = "INSERT INTO stu01(name,age,class) VALUES(%s,%s,%s)".format(row['name'],row['age'],row['class'])
    # sql = "INSERT INTO stu01(name,age,class) VALUES('{name}','{age}','{clazz}')".format(name='12',age=25,clazz='36')
    #待解决插入中文乱码？？
    sql = "INSERT INTO stu01(name,age,class) VALUES('{name}','{age}','{clazz}')".format(name=row['name'],age=row['age'],clazz=row['class'])

    sqlhelper.insert(sql)

# params=['1',2,'3']
# sql="INSERT INTO stu01(name,age,class) VALUES(%s,%s,%s)"









