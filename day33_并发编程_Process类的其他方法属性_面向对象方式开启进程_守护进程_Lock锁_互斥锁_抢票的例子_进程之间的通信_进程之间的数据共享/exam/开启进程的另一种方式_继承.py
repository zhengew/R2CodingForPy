# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 开启进程的另一种方式_继承.py
# @datatime: 2023/4/28 下午1:12

"""
目标:掌握面向对象方式开启进程
"""

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self, user): # 子类继承父类init方法并添加子类独有的派生属性
        self.user = user
        super(MyProcess, self).__init__()
    def run(self, n): # 重新父类 Process中的run方法，并给子进程传递参数
        for i in range(n, 0, -1):
            print(i)
        print('%s预备～跑！' % self.user)

if __name__ == '__main__':
    MyProcess('alex').run(3)    # 实例化对象并调用run方法
    MyProcess('taibai').run(3)

