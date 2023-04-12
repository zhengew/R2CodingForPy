# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 队列和栈_demo.py
# @datatime: 2023/4/5 16:27

"""
目标：通过继承的方式实现队列和栈
实现：put方法和get方法
队列：先进先出
栈：先进后出
"""

class Foo(object):
    def __init__(self):
        self.l = []
    def put(self, data):
        self.l.append(data)

    def get(self):
        return self.l.pop() if self.index else self.l.pop(0)

class Queue(Foo):
    """队列 先进先出"""
    def __init__(self):
        self.index = 0
        Foo.__init__(self)

class Stack(Foo):
    """栈 先进后出 """
    def __init__(self):
        self.index = -1
        Foo.__init__(self)

import queue


if __name__ == '__main__':
    # 队列： 先进先出
    q = Queue()
    q.put(1)
    q.put(2)
    print(q.get()) # 1

    # 栈：后进先出
    s = Stack()
    s.put(3)
    s.put(4)
    print(s.get())
    print(s.get())
    print(s.get()) # IndexError: pop from empty list
