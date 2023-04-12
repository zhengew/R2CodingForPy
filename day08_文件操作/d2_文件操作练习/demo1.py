# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 20:38
# 文件名称: demo1.py

"""
apple 10 3
tesla 100000 1
mac 3000 2
lenovo 30000 3
chicken 10 3

通过代码，将其构建成这种数据类型：
[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1}......] 并计算出总价钱。
"""

goods = []
sum = 0
with open("file1", mode="r", encoding="utf-8") as f:
    for i in f:
        name, price, amount = i.strip().split(" ")
        goods.append({"name": name, "price": price, "amount": amount})
        sum += float(price)
# print(goods)
for i in goods:
    print(i)
print(sum)