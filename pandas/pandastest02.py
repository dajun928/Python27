# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

# df = pd.read_excel('D:\\work\\isoftstone\\pandastest\\test01.xlsx',sheet_name='Sheet1')

# df1=pd.DataFrame(df)

# print df
# print df1

dict01={"id":[1001,1002,1003,1004,1005,1006],
        "date":pd.date_range('20130102', periods=6),
        "city":['Beijing ', 'SH', '  guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
        "age":[23,44,54,32,34,32],
        "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
        "price":[1200,np.nan,2133,5433,np.nan,4432]}

df22 = pd.DataFrame(dict01,columns=['id','date','city','category','age','price'])


# print df22
# 用pandas创建数据表写入excel
# df22.to_excel("result01.xlsx")

print df22
# print df22.shapde
# print df22.info()
# print df22.columns
#
# 三、数据表清洗
# 1、用数字0填充空值
# df.fillna(value=0)
print df22.fillna(' ')







