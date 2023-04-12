# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 20:04
# 文件名称: 闭包.py

def get_avg():
    """
    闭包案例
    1.嵌套函数
    2.内层函数对外层函数非全局变量的引用
    3.引用的外层的非全局变量：被称为自由变量
    :return:
    """
    data = []
    def average(price: float):
        data.append(price)
        return sum(data) / len(data)
    return average

ret = get_avg()

avg1 = ret(10000.0)
print(avg1) # 10000.0
avg2 = ret(20000.0)
print(avg2) # 15000.0

print(ret.__code__.co_freevars) # ('data',) 自由变量 data