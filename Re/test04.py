#coding=utf-8



import re

# 正确的地址
ret1 = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
print ret1.group()

# 不正确的地址
ret2 = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
# print ret.group()

# 通过$来确定末尾
ret3 = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.comheihei")
# print ret3.group()


