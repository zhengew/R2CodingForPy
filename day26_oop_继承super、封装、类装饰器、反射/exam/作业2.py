# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 作业2.py
# @datatime: 2023/4/8 16:37

class User:
    def __init__(self,name,age,sex):
        self.name = name
        self.age  = age
        self.sex  = sex
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

# 用户输入用户名密码性别
# 实例化对象
# 用户任意输入内容 : 不能用异常处理
    # 如果输入的是属性名 打印属性值
    # 如果输入的是方法名 调用方法
    # 如果输入的什么都不是 不做操作

if __name__ == '__main__':
    name = input("姓名: ")
    age = input("年龄: ")
    sex = input("性别: ")
    obj = User(name, age, sex)

    while True:
        info = input("请输入任意内容: ").strip()
        if hasattr(obj, info):
            ret = getattr(obj, info)
            if callable(ret):
                ret()
            else:
                print(ret)