# -*- coding:utf-8 -*-

import pandas as pd

df = pd.read_csv('D:\\MyWork\\test1.csv')

data = df.fillna(' ')

dct = data.to_dict(orient='split')

lst = []
loc = []
for index in dct['index'][0:1]:
    y = index
    for rows in dct['data']:
        for item in enumerate(rows):
            if item[1] == 'a':
                x = item[0]
                loc.append([x, y])
#                 print x,y
#                 lst.append(loc[x,y])


print len(loc)
print loc









