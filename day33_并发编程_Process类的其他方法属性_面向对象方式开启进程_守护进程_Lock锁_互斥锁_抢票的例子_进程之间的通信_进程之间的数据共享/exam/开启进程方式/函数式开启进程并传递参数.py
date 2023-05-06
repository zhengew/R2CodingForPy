# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 函数式开启进程并传递参数.py
# @datatime: 2023/4/29 08:36

"""
目标：
1.掌握函数式开启进程的方式
2.主进程给子进程传递参数
"""
from multiprocessing import Process

def send_email(emailAddr):
    for addr in emailAddr:
        print(f"向{addr}发送邮件～")

if __name__ == '__main__':
    email_list = ['alex@126.com', 'taibai@126.com', 'wusir@qq.com']
    p = Process(target=send_email, args=(email_list,)) # 主进程给子进程传递参数，参数以元组的形式接收
    p.start() # 异步非阻塞
    p.join() # 同步阻塞 等子进程执行完后，再打印 所有邮件发送完毕
    print('所有邮件发送完毕～')

