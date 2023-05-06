# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 面向对象方式开启子进程并传递参数.py
# @datatime: 2023/4/29 08:47

"""
目标:
1.掌握面向对象方式开始进程
2.重写init方法给子进程传参
注意：如果直接用对象调用run方法的方式启动进程，就不能再使用join方法阻塞进程，
否则会抛出异常。AssertionError: can only join a started process
"""
from multiprocessing import Process
class MyProcess(Process):
    def __init__(self, user, emailAddr):
        self.user = user
        self.email_addr = emailAddr
        super(MyProcess, self).__init__()
    def run(self):
        self.send_email(self.email_addr)
    def send_email(self, emailAddr):
        for addr in emailAddr:
            print('%s正在向%s发送邮件～' %(self.user, addr))

if __name__ == '__main__':
    email_list = ['alex@126.com', 'taibai@126.com', 'wusir@qq.com']
    p = MyProcess('大壮', email_list)
    p.start()
    # p.run() # AssertionError: can only join a started process
    p.join()
    print('所有邮件发送完毕～')