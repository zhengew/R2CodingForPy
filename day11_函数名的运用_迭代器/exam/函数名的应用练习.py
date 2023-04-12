# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 15:56
# 文件名称: 函数名的应用练习.py

# 1.函数名指向内存地址
# def func():
#     print('in func')
#
# print(func) # <function func at 0x10816c0d0>

# 2.函数名作为变量
# def func2():
#     print('in func2')
#
# ret = func2
# print(id(ret) == id(func2)) # True
# ret()

# 3.函数名作为容器类型数据的元素
# def func1():
#     print('in func1')
# def func2():
#     print('in func2')
# def func3():
#     print('in func3')
#
# functions = [func1, func2, func3]
# for i in functions:
#     i()

# 4.函数名作为函数实参

# def func1():
#     print('in func1')
#
# def func2(function):
#     print('in func2')
#     function()
#
# func2(func1)


# 5.函数名作为函数的返回值
def func1():
    print('in func1')

def func2(funtion):
    print('in func2')
    ret = funtion
    return ret


ret = func2(func1)

ret()