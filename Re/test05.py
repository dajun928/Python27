#coding=utf-8

import re

ret1 = re.match("\w{4,20}@163\.com", "test@163.com")
print ret1.group()

ret2 = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
print ret2.group()

ret3 = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print ret3.group()

ret4 = re.match("\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
# print ret4.group()
