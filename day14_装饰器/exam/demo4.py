# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/15 21:26
# 文件名称: demo4.py
from random import random


# 为函数写一个装饰器，把函数的返回值 +100 然后再返回。

def wrapper(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret + 100
    return inner


@wrapper
def func(a, b):
    return a + b

if __name__ == '__main__':
    ret = func(int(random() * 10), 1)
    print(ret)