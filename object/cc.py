# encoding=utf-8

class Animal(object):

    def eat(self):
        print '--------吃---------'
    def sleep(self):
        print '--------睡---------'
    def run(self):
        print '--------跑---------'
    def drink(self):
        print '--------喝---------'


class Dog(Animal):
    def bark(self):
        print '--------汪汪汪---------'


class XiaoTian(Dog):
    def fly(self):
        print '--------飞---------'
    def bark(self):
        print  '-----------狂叫-------------'
        Dog.bark(self)

xiao=XiaoTian()

xiao.bark()

















