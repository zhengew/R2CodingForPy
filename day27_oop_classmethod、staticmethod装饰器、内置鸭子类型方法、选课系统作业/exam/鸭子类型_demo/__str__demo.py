# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __str__demo.py
# @datatime: 2023/4/11 22:16

"""
目标：理解常见鸭子类型(魔术方法)
4.__str__  打印的对象
反例: 类中未实现str方法，打印实例对象时得到的是一个对象地址
"""

class List(object):
    def __init__(self):
        self.lst = []
    def append(self, obj: object):
        self.lst.append(obj)

if __name__ == '__main__':
    l1 = List()
    l1.append(1)
    print(l1) # <__main__.List object at 0x106491990>
    l1.append(2)
    print(l1) # <__main__.List object at 0x107b15990>
