# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/1 22:01
# 文件名称: demo1.py

class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def func1(self):
        print(self)

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
A.Country = '英国'
a.Country = '日本'
print(a.Country) # 日本
print(b.Country) # 英国
print(A.Country) # 英国
print(a.__dict__) # {'name': 'alex', 'age': 83, 'Country': '日本'}
print(b.__dict__) # {'name': 'wusir', 'age': 74}