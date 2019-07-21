# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iq_data = pd.read_csv('core.csv')
iq = iq_data['IQ']

mean = iq.mean()
mean

std = iq.std()
std

def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

# x的范围为60-150，以1为单位,需x根据范围调试
x = np.arange(50, 60,0.1)

# x数对应的概率密度
y = normfun(x, mean, std)

# 参数,颜色，线宽
plt.plot(x,y, color='g',linewidth = 1)

#数据，数组，颜色，颜色深浅，组宽，显示频率
plt.hist(iq, bins =7, color = 'r',alpha=0.5,rwidth= 0.9, normed=True)

plt.title('R3 distribution')
plt.xlabel('IQ score')
plt.ylabel('Probability')
plt.show()







