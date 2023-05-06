# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 守护进程.py
# @datatime: 2023/4/29 09:24

"""
目标:掌握如何开启守护进程 daemon
守护进程要再start方法之前设置；
守护进程守护的是主进程的代码，随着主进程代码执行直接而结束
"""
from multiprocessing import Process
import time
def func1():
    for i in range(2):
        print('in func1~')
        time.sleep(1)
def func2():
    for i in range(5):
        print('in func2~')
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()

    p2 = Process(target=func2)
    p2.daemon = True # p2开启守护进程
    p2.start()

    p1.join() # 主进程同步阻塞，要等p1执行完毕才会继续往下执行
    print('主进程代码执行完毕')