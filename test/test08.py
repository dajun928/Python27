# -*- coding:utf-8 -*-

# 乘法表
def run():
    for i in range(1,10):
        for j in range(1,10):
            if j<=i:
                print str(j) + '*' + str(i) + "=" + str(j * i),
            if j==i:
                print "\n"

run()