# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 08:01

"""
FTP 客户端入口
"""
import socket
from maxExam.week.fifth.app.conf.setting import ConfingHandler

class TransmitClient(object):

    # 服务端IP
    server_addr = ConfingHandler.server_addr
    sk = socket.socket()
    # 首页菜单
    __home_options = [('登陆', 'login'), ('注册', 'register'), ('退出', 'exit')]
    # 登陆后的菜单
    __login_options = [('上一级目录', 'upper_dir'), ('下一级目录', 'lower_dir'), ('新建目录', 'make_dir'),
                       ('查看当前目录', 'show_dir'), ('上传文件', 'upload'), ('下载文件', 'download'),
                       ('退出', 'exit')]
    def __init__(self):
        self.sk.connect(self.server_addr)

    def __str__(self):
        print(self.__dict__)

    def show_menu(self, login_status: str):
        """
        更具登陆状态展示菜单
        :param login_status: 201 登陆成功， 202 登陆失败
        :return:
        """
        print('in show menu')

if __name__ == '__main__':
    obj = TransmitClient()
    while True:
        obj.sk.send(b'hello')
        print(obj.sk.recv(1024).decode('utf-8'))

