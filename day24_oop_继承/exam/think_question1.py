# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 15:57
# 文件名称: think_question1.py

class Foo():
    def __init__(self):
        self.func()

    def func(self):
        print('in Foo')

class Son(Foo):
    def func(self):
        print('in Son')

Son() # in Son