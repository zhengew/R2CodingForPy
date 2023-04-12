# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/3 20:19
# 文件名称: 队列和栈_demo.py

"""
队列(queue): 先进先出
栈(stack): 先进后出
get put 方法
"""

class Foo(object):
    def __init__(self):
        self.data= [] # 存储队列元素
    def put(self, obj):
        """
        队列 put方法
        :param obj:
        :return:
        """
        self.data.append(obj)

    def get(self):
        """
        队列 get方法
        :return:
        """
        return self.data.pop() if self.index else self.data.pop(0)

class Queue(Foo):
    """队列"""
    def __init__(self):
        self.index = 0
        Foo.__init__(self)

class Stack(Foo):
    """栈"""
    def __init__(self):
        self.index = 1
        Foo.__init__(self)


if __name__ == '__main__':
    # 队列：先进先出
    q = Queue()
    for i in range(10):
        q.put(i)
    print(q.data)

    ret = q.get()
    print(ret)
    print(q.data)

    # 栈： 先进后出
    s = Stack()
    for i in range(11, 21):
        s.put(i)

    print(s.data)
    ret = s.get()
    print(ret)
    print(s.data)