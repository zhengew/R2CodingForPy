# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:21
# 文件名称: demo2.py

# 3.写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。

def func(data):
    if "__iter__" in dir(data):
        flag = len(data) > 5
    else:
        flag = "参数错误，非可迭代对象"
    return flag

print(func([1, 2, 3, 4, 5, 6])) # True
print(func([1, 2, 3, 4, 5])) # False
print(func(1)) # 非可迭代对象

print(dir(1)) # dir(object), 判断一个对象有什么方法