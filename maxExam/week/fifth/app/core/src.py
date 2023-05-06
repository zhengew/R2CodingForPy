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
    __login_options = [('上传文件', 'upload'), ('下载文件', 'download'),('查看当前目录', 'show_dir'),
                       ('新建文件夹', 'make_dir'), ('上一级目录', 'upper_dir'), ('下一级目录', 'lower_dir'),
                       ('退出', 'exit')]
    def __init__(self):
        # self.sk.connect(self.server_addr)
        self.login_status = {'login_user': 'alex', 'status': True}

    def __str__(self):
        return '%s' % self.__dict__

    def login(self):
        """登录"""
        print('in login')

    def register(self):
        """注册"""
        print('in register')

    def exit(self):
        """退出"""
        print('in exit')

    def upper_dir(self):
        """上一级目录"""
        print(' in upper_dir')

    def lower_dir(self):
        """下一级目录"""
        print('in lower_dir')

    def make_dir(self):
        """新建目录"""
        print('in make_dir')

    def show_dir(self):
        """查看当前目录"""
        print('in show_dir')

    def upload(self):
        """上传文件"""
        print('in upload')

    def download(self):
        """下载文件"""
        print('in download')

    def show_menus(self):
        """
        更具登陆状态展示菜单
        :param login_status: 201 登陆成功， 202 登陆失败
        :return:
        """
        if not self.login_status['status']:
            print('欢迎进入TransmitFTP客户端'.center(100, '='))
            for index, option in enumerate(self.__home_options, 1):
                print('%s: %s' %(index, option[0]))
        else:
            print('欢迎%s,请选则如下功能:' % self.login_status['login_user'])
            for index, option in enumerate(self.__login_options, 1):
                print('%s: %s' %(index, option[0]))

if __name__ == '__main__':
    obj = TransmitClient()
    # while True:
    #     obj.sk.send(b'hello')
    #     print(obj.sk.recv(1024).decode('utf-8'))
    obj.show_menus()
