# -*- coding:utf-8 -*-


# 四、数据预处理
import numpy as np
import pandas as pd

data={"id":[1001,1002,1003,1004,1005,1006,1007,1008],
        "gender":['male','female','male','female','male','female','male','female'],
        "pay":['Y','N','Y','Y','N','Y','N','Y',],
        "m-point":[10,12,20,40,40,40,30,20]}

df=pd.DataFrame(data)

print df

df_inner=pd.merge(df,df1,how='inner')  # 匹配合并，交集
df_left=pd.merge(df,df1,how='left')        #
df_right=pd.merge(df,df1,how='right')
df_outer=pd.merge(df,df1,how='outer')  #并集

# from sqlalchemy import create_engine
#
# ##将数据写入mysql的数据库，但需要先通过sqlalchemy.create_engine建立连接,且字符编码设置为utf8，否则有些latin字符不能处理
# yconnect = create_engine('mysql+mysqldb://root:password@localhost:3306/databasename?charset=utf8')
# pd.io.sql.to_sql(thedataframe, 'tablename', yconnect, schema='databasename', if_exists='append')














































































