# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 队列.py
# @datatime: 2023/4/29 12:46

"""
目标: 掌握通过队列实现进程之间的通信
"""

from multiprocessing import Process, Queue

def consumer(q):
    for i in range(10):
        print(q.get())

def producter(q):
    for i in range(10):
        q.put(i)

if __name__ == '__main__':

    q = Queue()
    p1 = Process(target=producter, args=(q,))
    p1.start()

    p2 = Process(target=consumer, args=(q,))
    p2.start()



