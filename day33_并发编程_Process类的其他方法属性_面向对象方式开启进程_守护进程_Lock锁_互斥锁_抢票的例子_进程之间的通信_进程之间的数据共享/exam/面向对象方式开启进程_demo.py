# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 面向对象方式开启进程_demo.py
# @datatime: 2023/4/27 20:56

"""
目标:
1.面向对象的方式开启进程
2.传参
"""
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
    for i in range(10):
        MyProcess(1, 2, 3).run()
