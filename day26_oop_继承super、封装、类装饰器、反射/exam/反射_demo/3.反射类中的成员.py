# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 3.反射类中的成员.py
# @datatime: 2023/4/8 14:16

"""
目标: 理解反射原理
反射本模块中的成员
"""

class A(object):
    obj_list = []
    def func(self):
        self.obj_list.append(1)

if __name__ == '__main__':
    obj_list = getattr(A, 'obj_list') # 访问类中的私有属性
    obj_list.append(10)
    print(obj_list) # [10]
