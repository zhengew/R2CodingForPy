# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 反射三大器的应用.py
# @datatime: 2023/4/8 14:43

"""
目标: 理解反射三大器
hasattr(__obj: object, __name:str)  判断__name 在 __obj中是否存在, 返回True, False
getattr(__obj: object, name:str) 反射__obj中的与name名字相同的成员
callable(__obj: object) 判断 __obj是否可调用, 返回True/False
"""
class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def func_A(self):
        print('in func_A')

if __name__ == '__main__':
    a = A('alex', 20)
    if hasattr(a, 'func_A'):  # 判断是否可以反射
        obj = getattr(a, 'func_A')  # 拿到反射对象
        if callable(obj): # 判断反射的对象是否可调用
            obj() # 执行通过反射得到的绑定方法

