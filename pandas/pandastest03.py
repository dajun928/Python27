# -*- coding:utf-8 -*-


# 数据表清洗
import numpy as np
import pandas as pd

dict01={"id":[1001,1002,1003,1004,1005,1006],
        "date":pd.date_range('20130102', periods=6),
        "city":['Beijing ', 'SH', '  guangzhou ', 'Shenzhen', 'shanghai', 'BEIJING '],
        "age":[23,44,54,32,34,32],
        "category":['100-A','100-B','110-A','110-C','210-A','130-F'],
        "price":[1200,np.nan,2133,5433,np.nan,4432]}

df = pd.DataFrame(dict01,columns=['id','date','city','category','age','price'])

print df
# 三、数据表清洗
# 1、用数字0填充空值
# df.fillna(value=0)
# print df.fillna(' ')

# 使用列price的均值对NA进行填充
# print df.fillna(df['price'].mean())
# df.fillna(df['price'].mean())

# 清除city字段的字符空格
# df22['city']=df22['city'].map(str.strip)
# df22['city']=df22['city'].str.lower()
# df=df.fillna(value=0)
# df=df['price'].astype('int')
#


# df1=df.rename(columns={'category': 'category-size'})
df['city']=df['city'].str.lower()
df2=df['city'].replace('sh', 'shanghai')
print df2


























































































