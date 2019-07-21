#coding=utf-8
import matplotlib
# print matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('qt4agg')
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
plt.plot([-1,2,-5,3])
plt.title(u'中文')
plt.show()











