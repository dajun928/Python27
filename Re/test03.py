#coding=utf-8

#验证手机号码
import re

patten='1[34578]\d{9}$'

str='13267149013'
str1='13267149wf013'
str2='13267149013fdf'
str3='1d3267149013'

result = re.match(patten,str)


print result
print result.group()