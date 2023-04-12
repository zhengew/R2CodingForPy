# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 14:05
# 文件名称: globals_locals_demo1.py

"""
目标：学习globals() locals()
"""

name = 'alex'
age = 18

def func():
    sex = "男"
    print(locals())

print(globals())

print('****************')
func()

print("***********")

