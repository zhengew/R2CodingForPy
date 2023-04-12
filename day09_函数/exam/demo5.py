# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:35
# 文件名称: demo5.py

# 6.写函数，接收两个数字参数，返回比较大的那个数字。

def func(num1: int, num2: int):
    if type(num1) == int and type(num2) == int:
        return num1 if num1 > num2 else num2
    else:
        return "数据非法，非int类型数据"


print(func(1, 2)) # 2
print(func(2, 1)) # 2
print(func("1", 2)) # 数据非法，非int类型数据
print(func(1, "2")) # 数据非法，非int类型数据