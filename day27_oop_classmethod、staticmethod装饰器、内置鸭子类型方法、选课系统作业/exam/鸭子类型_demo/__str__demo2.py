# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __str__demo2.py
# @datatime: 2023/4/11 22:23

"""
目标：理解常见鸭子类型(魔术方法)
4.__str__  打印的对象
反例: 类中实现str方法，打印实例对象时会调用类中的__str__方法
"""

class List(object):
    def __init__(self):
        self.lst = []
    def append(self, obj: object):
        self.lst.append(obj)

    def __str__(self):
        return "%s" % len(self.lst)

if __name__ == '__main__':
    l1 = List()
    l1.append(1)
    print(l1) # 1
    l1.append(2)
    print(l1) # 2

