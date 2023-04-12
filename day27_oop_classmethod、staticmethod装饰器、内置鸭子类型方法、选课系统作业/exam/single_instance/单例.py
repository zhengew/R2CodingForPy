# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 反射demo.py
# @datatime: 2023/4/12 07:01

"""
目标: 理解单例模式
__new__ 在对象初始化之前开辟存储对象的空间
"""
class Baby:

    __instance = None
    def __new__(cls, *args, **kwargs):
        """
        1.如果静态变量为 None, 才执行开空间这件事，并把这块空间作为返回值，返回给__instance静态变量
        2.并且这块空间会自动传给init方法，作为形参self参数,再完成对象的初始化
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,cloth,pants):
        self.cloth = cloth
        self.pants = pants
    def __str__(self):
        return "%s" %self.__dict__

if __name__ == '__main__':
    baby = Baby('红上衣','绿裤子')
    print(baby) # {'cloth': '红上衣', 'pants': '绿裤子'}
    baby2 = Baby('绿上衣', '红裤子')
    print(baby) # {'cloth': '绿上衣', 'pants': '红裤子'}
    print(baby2) # {'cloth': '绿上衣', 'pants': '红裤子'}