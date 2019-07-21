# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv('D:\\MyWork\\test1.csv')

data=df.fillna(' ')

print data
# for index,rows in data.iteritems():
#     print index,rows
#     print type(index),type(rows)



