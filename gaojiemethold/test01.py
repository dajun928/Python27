# -*- coding:utf-8 -*-
from collections import Iterator


# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#
# 可以使用isinstance()判断一个对象是否是Iterator对象：
# l=[x*2 for x in range(5)]
#
#
# print l
#
# n=(x*2 for x in range(5))
#
# print n
#
# for i in n:
#     print i


def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        yield b
        a,b = b,a+b
        n+=1
    # return 'done'


F = fib(5)

# print next(F)
# print next(F)
# print next(F)
# print next(F)
# print next(F)


while True:
    try:
        print next(F)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break



















