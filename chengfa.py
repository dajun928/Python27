#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@version : 
@file : chengfa.py
@time : 2019/03/25 23:56:47
@func : 
"""
# 乘法表
def run():
    for i in range(1,10):
        for j in range(1,10):
            if j<=i:
                print str(j) + '*' + str(i) + "=" + str(j * i),
            if j==i:
                print "\n"

run()