# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: Animal.py
# @datatime: 2023/4/8 13:08

"""
Animal类
"""
pi = 3.14
class Animal(object):
    Counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Counter += 1
    def eat(self):
        print(f'{self.name} is eating')

if __name__ == '__main__':
    xiaobai = Animal('小白', 2)
    print(Animal.Counter)