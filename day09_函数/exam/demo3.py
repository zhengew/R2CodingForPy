# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:34
# 文件名称: demo3.py

# 4.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def func(data: list):
    return data[:2]


print(func([1, ]))
print(func([1, 2, 3]))
print(func([1, 2]))
