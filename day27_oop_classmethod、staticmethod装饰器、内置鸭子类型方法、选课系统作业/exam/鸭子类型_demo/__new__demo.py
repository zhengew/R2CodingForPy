# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __new__demo.py
# @datatime: 2023/4/11 21:43

"""
目标：理解常见鸭子类型(魔术方法)
3.__new__  开辟内存空间
实例化步骤：
1.实例化时首先在内存中开辟一块属于对象的内存空间，不能存储一个类指针，指向类的内存空间 --> __new__ 来实现
2.调用 __init__方法，把属于对象的内存地址传递给 __init__ 方法的形参self
3.__init__ 方法把实例化传递的实参存储在self空间里 -- 对象的初始化
4.init方法的形参self所指向的内存地址会作为返回值，返回给实例对象
"""

class SingleInstance(object):
    """饿汉单例"""
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

class Npc(SingleInstance):
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    daocaoren = Npc('稻草人')
    print(daocaoren.name, id(daocaoren)) # 稻草人 4414275200
    daocaoren2 = Npc('稻草人2')
    print(daocaoren.name) # 稻草人2
    print(daocaoren2.name) # 稻草人2
    print(daocaoren is daocaoren2) # True
    print(id(daocaoren), id(daocaoren2)) # 4414275200 4414275200