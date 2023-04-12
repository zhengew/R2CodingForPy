# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 2.反射当前文件(脚本)中的成员.py
# @datatime: 2023/4/8 13:40

"""
目标: 理解反射原理
反射本模块中的成员
"""
import sys
class A(object):
    Role = '战士'
    def __init__(self, name):
        self.name = name
        self.hp = 1000
    def change(self, hp):
        self.hp += hp

a = A('alex')
flag = True

def func():
    print('in func')

if __name__ == '__main__':
    A= getattr(sys.modules['__main__'], 'A') # 反射本模块中的类 A
    print(A) # <class '__main__.A'>

    obj = getattr(sys.modules['__main__'], 'a') # 反射本模块中的实例对象
    print(obj) # <__main__.A object at 0x10e343af0>

    flag = getattr(sys.modules['__main__'], 'flag') # 反射本模块中的全局变量
    print(flag) # True

    ret = getattr(sys.modules['__main__'], 'func') # 反射本模块中的函数
    ret() # in func