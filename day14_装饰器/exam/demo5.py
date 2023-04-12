# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/15 21:31
# 文件名称: demo5.py

# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。

def wrapper(func):
    def inner(*args, **kwargs):
        print('每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码')
        ret = func(*args, **kwargs)
        return ret
    return inner

@wrapper
def func(a: int, b: int):
    return a + b

if __name__ == '__main__':
    r1 = func(1, 2)
    r2 = func(1, 2)
    r3 = func(1, 2)
    r4 = sum((1, 3))
