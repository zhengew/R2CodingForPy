# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:15
# 文件名称: demo1.py

# 2.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。

def func(data: list):
    res = []
    for i in range(len(data)):
        if i % 2 != 0:
           res.append(data[i])
    return res


print(func([1, 2, 3, 4]))