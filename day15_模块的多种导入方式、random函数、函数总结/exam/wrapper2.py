# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 07:36
# 文件名称: wrapper2.py

def wrapper(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret + 100
    return inner

@wrapper
def func(a, b):
    return a + b

if __name__ == '__main__':
    ret = func(1, 2)
    print(ret)