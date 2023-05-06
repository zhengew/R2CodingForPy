# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 关闭进程.py
# @datatime: 2023/4/29 09:04

"""
目标:掌握如何关闭进程
terminate 终止进程：terminate命令只是告诉CPU要kill掉这个进程，但不是立即执行该命令，需要等待cpu时间片轮转到
"""

from multiprocessing import Process
import os
import time
def func():
    print(os.getpid())

if __name__ == '__main__':
    p1 = Process(target=func)
    p1.start()
    print(p1.is_alive()) # True
    p1.terminate() # 终止进程：terminate命令只是告诉CPU要kill掉这个进程，但不是立即执行该命令
    time.sleep(0.01)
    print(p1.is_alive()) # False