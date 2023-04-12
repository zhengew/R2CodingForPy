# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 2.被property装饰的方法可通过类名或对象名调用.py
# @datatime: 2023/4/8 09:55

"""
目标：理解@property装饰器
1.被装饰的方法，通过类名或对象名调用
"""
from math import pi
class Circle(object):

    def __init__(self,r):
        self.r = r
    @property
    def area(self):
        return pi * self.r**2

if __name__ == '__main__':
    c = Circle(10)
    print(c.area) # 314.1592653589793
    print(Circle.area) # <property object at 0x108a76fc0>