# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: Process类的其他方法.py
# @datatime: 2023/4/27 21:00

"""
目标:了解Process类的其他属性
"""
import time
from multiprocessing import Process

class MyProcess(Process):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super(MyProcess, self).__init__()

    def run(self):
        print(self.name, self.ident, self.pid, self.a, self.b, self.c)

if __name__ == '__main__':
    p1 = MyProcess(1, 2, 3)
    p1.start()
    print(p1.name, p1.pid, p1.ident)
    print(p1.is_alive()) # True
    p1.terminate() # 强制结束一个子进程， 异步非阻塞
    print(p1.is_alive()) # True
    time.sleep(0.01)
    print(p1.is_alive()) # False
