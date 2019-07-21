#coding=utf-8
import matplotlib.pyplot as plt
import random
import sys
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
import matplotlib
# matplotlib.use('qt4agg')
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
# 画条形图显示电影票房对比
plt.figure(figsize=(20, 8), dpi=100)

# 准备好数据， 电影名称，电影票房
movie_name = [u'雷神3：诸神黄昏',u'正义联盟',u'东方快车谋杀案',u'寻梦环游记',u'全球风暴',u'降魔传',u'追捕',u'七十七天',u'密战',u'狂兽',u'其它']
y = [73853,57767,22354,15969,14839,8725,8716,8318,7916,6764,52222]
# 显示x坐标必须是数字
x = range(len(movie_name))

# 通过bar去显示条形图
plt.bar(x, y, width=0.2, color=['b','r','g','y','c','m','y','k','c','g','g'])

#美化X坐标显示
plt.xticks(x, movie_name)

plt.show()