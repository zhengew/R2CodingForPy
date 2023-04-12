# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 21:18
# 文件名称: 4.enumerate枚举值.py

"""
目标：enumerate 枚举，对可迭代对象组成一个索引序列，利用它可以同时得到索引和值
"""


def query():
    print("query".center(50, "*"))


def update():
    print("update".center(50, "*"))


def delete():
    print("delete".center(50, "*"))


def insert():
    print("insert".center(50, "*"))


commands = {"query", "update", "delete", "insert", "quit"}
while True:
    for k, v in enumerate(commands, 1):
        print(f"{k}: {v}")
    command = input("请选择命令：")
    match command:
        case "1":
            query()
        case "2":
            update()
        case "3":
            delete()
        case "4":
            insert()
        case "5":
            break
        case _:
            print("输入错误！")





