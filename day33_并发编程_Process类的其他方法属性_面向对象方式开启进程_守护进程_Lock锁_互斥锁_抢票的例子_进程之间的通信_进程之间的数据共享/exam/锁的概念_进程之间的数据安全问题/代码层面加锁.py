# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 代码层面加锁.py
# @datatime: 2023/4/29 11:13

"""
目标:掌握如何在代码层面给进程加锁
acquire 拿钥匙
release 还钥匙
注意: acquire和release必须是成对出现，如果缺少release，就会进入阻塞事件，代码无法继续向下执行
"""

from multiprocessing import Process, Lock

lock = Lock()

lock.acquire()
print(111)
lock.acquire() # 没有释放锁，就去拿钥匙，进入阻塞事件
print(222)
lock.release()
