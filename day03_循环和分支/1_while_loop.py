# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/418:02
# 文件名称: 02_while_loop.py

name = input("姓名: ")
count = 0
while name:
    print("死循环")
    count += 1
    if count == 10:
        quit = input("是否退出: ")
        if quit:
            break
        else:
            count = 1