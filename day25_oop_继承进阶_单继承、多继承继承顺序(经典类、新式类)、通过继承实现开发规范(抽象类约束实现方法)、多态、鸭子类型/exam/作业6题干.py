# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 作业6题干.py
# @datatime: 2023/4/6 07:59

"""
# 需求
1. while循环提示用户输 : 户名、密码、邮箱(正则满足邮箱格式)
2. 为每个用户创建1个对象，并添加到列表中。
3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        # 用户列表，数据格式：[user对象，user对象，user对象]
        self.user_list = []

    def login(self):
        """
        用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
        :return:
        """
        pass

    def register(self):
        """
        用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
        :return:
        """
        pass

    def run(self):
        """
        主程序
        :return:
        """
        pass


if __name__ == '__main__':
    obj = Account()
    obj.run()