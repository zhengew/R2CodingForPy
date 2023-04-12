# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __len__demo.py
# @datatime: 2023/4/11 21:11

"""
目标：理解常见鸭子类型(魔术方法)
2.__len__  对象的长度
如果需要获取一个类的实例化对象的长度，就在类中实现 __len__方法
"""

class Cls(object):
    def __init__(self, name):
        self.name = name
        self.students = []
    def __len__(self):
        return len(self.students)

if __name__ == '__main__':
    py22 = Cls('py22')
    py22.students.append('alex')
    py22.students.append('taibai')
    print(len(py22)) # 2
    print(py22.__len__()) # 2
