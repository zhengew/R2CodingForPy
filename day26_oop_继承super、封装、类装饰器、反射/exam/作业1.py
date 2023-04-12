# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 作业1.py
# @datatime: 2023/4/8 15:52

class Authentic:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def register(self):
        print('in register')
    def login(self):
        print('in login')

l = [('登录','login'),('注册','register')]
# 循环这个列表
# 显示 序号 用户要做的操作
# 用户输入序号
# 你通过序号找到对应的login或者register方法
# 先实例化
# 调用对应的方法,完成登录或者注册功能

def run():
    while True:
        for id, option in enumerate(l, 1):
            print(f"{id}: {option[0]}")
        option = input("请选择: ")
        obj = Authentic('taibai', 20)
        if option == '1':
            if hasattr(obj, l[int(option)-1][1]) and callable(getattr(obj, l[int(option)-1][1])):
                getattr(obj, l[int(option)-1][1])()
        elif option == '2':
            if hasattr(obj, l[int(option)-1][1]) and callable(getattr(obj, l[int(option)-1][1])):
                getattr(obj, l[int(option)-1][1])()
        elif option.upper() == 'Q':
            break
        else:
            print("输入错误～")


if __name__ == '__main__':
    run()

