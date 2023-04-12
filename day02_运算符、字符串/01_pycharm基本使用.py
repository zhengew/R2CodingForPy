# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/417:48
# 文件名称: 01_pycharm基本使用.py
import sys

username = input("用户名：")
password = input("密码：")

code = "qwer";
your_code = input("验证码:")

if your_code == code:
    if username == "test1" and password == "123456":
        print("登录成功")
    else:
        print("用户名或密码错误")
else:
    print("验证码错误")

print(sys.path)