# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: with上下文管理器创建互斥锁.py
# @datatime: 2023/4/29 11:34

"""
目标:掌握通过with上下文管理器创建互斥锁
"""
from multiprocessing import Process, Lock

lock = Lock() # 互斥锁

with lock:
    print("通过上下文管理器with创建互斥锁，自动进行了一些异常处理，保证即使一个进程代码出错退出也会归还钥匙")

print(111)
