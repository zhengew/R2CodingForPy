# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: Account.py
# @datatime: 2023/4/6 下午12:21
import re

from Users import Users
from mypickle import MyPickle
class Account(object):
    """
    账户类
    """
    path = "userinfo"
    def __init__(self):
        self.user_list = []

    def login(self):
        """登陆"""
        name = input("请输入用户名: ")
        users = MyPickle(self.path).load()
        for user in users:
            if name == user.name:
                pwd = input("请输入密码： ")
                if pwd == user.password:
                    print(f"用户{name}登陆成功～")
                    return
                else:
                    print('用户名或密码错误～')
                    break
        else:
            print('用户名或密码错误～')

    def register(self):
        """注册"""
        while True:
            name = input("用户名：").strip()
            try:
                users = MyPickle(self.path).load()
                for user in users:
                    if name == user.name:
                        print(f"用户名{name}已被注册，请重新输入～")
                        break
                else:
                    break
            except Exception:
                break

        while True:
            pwd = input("密码:")
            pwd2 = input("密码2：")
            if pwd != pwd2:
                print("两次密码输入不一致，请重新收入～")
            else:
                break
        email_regex = "^\w+@([\da-zA-Z]+[.])+?(com|cn)$"
        while True:
            email = input("请输入邮箱:")
            if re.match(email_regex, email):
                obj = Users(name, pwd, email)
                MyPickle(self.path).dump(obj)
                print(f"用户[{name}]注册成功～")
                return
            else:
                print(f'邮箱不符合规范～{email}')
    def run(self):
        """程序入口"""
        commands = [self.login, self.register]
        while True:
            for id, command in enumerate(commands, 1):
                print(f"{id}:{command.__name__}")
            selected = input("请选择： ")
            if selected == '1':
                commands[0]()
            elif selected == '2':
                commands[1]()
            elif selected.upper() == 'Q':
                break

if __name__ == '__main__':
    obj = Account()
    obj.run()