# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/1 22:30
# 文件名称: demo4.py


class A:
    Country = '中国'     # 静态变量/静态属性 存储在类的命名空间里的
    def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间里的
        self.name = name
        self.age = age
    def Country(self):
        return self.Country

a = A('alex',83,'印度')
b = A('wusir',74,'泰国')
print(a.Country) #
print(a.Country()) #