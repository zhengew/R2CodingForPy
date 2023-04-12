# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/1 16:05
# 文件名称: count_class_new_obj.py

"""
实现一个类，能够自动统计这个类实例化了多少个对象
"""

class A():
    """
    统计类实例化次数
    """
    Count = 0
    def __init__(self):
        A.Count += 1 # 类中的静态变量，每个实例话对象共有，在类中只有一份，每次实例化都共享这一份

for i in range(10):
    A()

print(A.Count) # 10