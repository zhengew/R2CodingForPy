# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/13 22:04
# 文件名称: timer装饰器.py
import time

def timer(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print(end_time - start_time)
    return inner
@timer
def func():
    time.sleep(1)
    print("测试装饰器")


func()