# -*- coding:utf-8 -*-

from datetime import datetime
# import datetime
import numpy as np
from pandas import Timestamp
import pandas as pd

# dt = datetime.datetime(2018, 9, 18)
dt = datetime.now()
ts = pd.DatetimeIndex([dt])[0]
dt64 = np.datetime64(dt)

# <type 'datetime.datetime'>
print dt
print type(dt)

# <class 'pandas._libs.tslib.Timestamp'>
print ts
print type(ts)

# <type 'numpy.datetime64'>
print dt64
print type(dt64)


# print datetime.datetime(2012, 5, 1, 0, 0)
# print type(datetime.datetime(2012, 5, 1, 0, 0))
#
#
# print np.datetime64('2012-05-01T01:00:00.000000+0100')
# print type(np.datetime64('2012-05-01T01:00:00.000000+0100'))

# 从时间戳中获取日期时间很容易：
print ts.to_pydatetime()
print type(ts.to_pydatetime())


# extract datetime from numpy.datetime64 type:
# pd.Timestamp(np.datetime64('2012-06-18T02:00:05.453000000-0400'))
# Timestamp('2012-06-18 06:00:05.453000')
#
# pd.Timestamp(np.datetime64('2012-06-18T02:00:05.453000000-0400')).to_pydatetime()
# datetime.datetime(2012, 6, 18, 6, 0, 5, 453000)












