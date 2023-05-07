# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 08:01

"""
FTP 客户端入口
"""
import logging
import socket
import os
import struct
import re
from maxExam.week.fifth.app.conf.setting import ConfingHandler
from maxExam.week.fifth.app.lib.serializeUtils import SerializeUtils
from maxExam.week.fifth.app.lib.common import Common

logging.basicConfig(level=logging.DEBUG)

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
        self.sk.connect(self.server_addr)
        self.login_status = {'login_user': None, 'status': False}
        self.curr_path = None

    def __str__(self):
        return '%s' % self.__dict__

    def login(self):
        """登录"""
        while True:
            name = input('请输入用户名:').strip()
            pwd = input('请输入密码:').strip()
            if re.findall('\W', name) or re.findall('\W', pwd):
                print('用户名或密码只能由字母数字或下划线组成～')
            else:
                break
        login_user = {'username': name, 'pwd': Common.get_pwd_md5(ConfingHandler.public_key, pwd)}
        self.send_operation(login_user)
        status_code = self.recv_operation_status()['status_code']
        logging.debug('登录接口响应状态码:%s' %status_code)
        if status_code == '201':
            # 更新 self.login_status
            self.login_status['login_user'] = name
            self.login_status['status'] = True
            # 更新用户当前所在目录(默认在家目录)
            self.curr_path = os.path.join(ConfingHandler.home_path, login_user['username'] + os.sep)
            logging.debug('当前登录用户%s所在目录:%s' %(login_user['username'], self.curr_path))
            print('用户:%s, 登录成功～' % name)
        elif status_code == '202':
            print('用户:%s,登录失败，用户名或密码错误～' % name)

    def register(self):
        """
        注册
        服务端接收 {'username': 'alex', 'pwd': 通过公钥加密后的md5}
        :return:
        """
        while True:
            name = input('请输入用户名:').strip()
            pwd = input('请输入密码:').strip()
            if re.findall('\W', name) or re.findall('\W', pwd):
                print('用户名或密码只能由字母数字或下划线组成～')
            else:
                break

        pwd = Common.get_pwd_md5(ConfingHandler.public_key, pwd) # 公钥加密
        reg_user = {'username': name, 'pwd': pwd}
        logging.debug('客户端公钥加密后的密码:%s' % pwd)
        self.send_operation(reg_user) # 像服务端发送注册用户信息
        status_code = self.recv_operation_status()['status_code']
        if status_code == '203':
            print('用户:%s, 注册成功～' % name)
        elif status_code == '204':
            print('用户名:%s,已被注册，请更换用户名重新注册～' % name)

    def exit(self):
        """
        退出逻辑，需要服务端更新登录状态
        :return:
        """
        print('%s退出客户端，欢迎下次使用~' % self.login_status['login_user'])
        self.login_status['login_user'] = None
        self.login_status['status'] = False
        self.sk.close()
        return 'error999'

    def upper_dir(self):
        """
        上一级目录
        :return:
        """
        dirs = self.recv_operation_status()
        if dirs['status_code'] == '213':
            # 更新 self.curr_path
            self.curr_path = dirs['data']
            print('跳转到上一级目录成功~')
            logging.info('self.curr_path是否更新:%s' %self.curr_path)
        elif dirs['status_code'] == '214':
            print('当前目录:%s, 是用户%s的家目录～' %(self.curr_path, self.login_status['login_user']))
        # 查看当前目录
        self.show_dir()

    def lower_dir(self):
        """
        下一级目录
        要先拿到当前路径下的所有文件夹，再由用户选择需要进入的二级目录
        服务端返回子目录数据后，更新self.curr_path
        :return:
        """
        dirs = self.recv_operation_status()
        logging.debug('服务端接收的子目录:%s' % dirs)
        if dirs['status_code'] == '211':
            for id, dir in enumerate(dirs['data'], 1):
                print('%s: %s' %(id, dir))
            while True:
                dir_id = input('请选择要进入的子目录id:').strip()
                if re.findall('[^\d]', dir_id) or int(dir_id) < 1 or int(dir_id) > len(dirs['data']):
                    print('您输入的子目录id不存在～')
                else:
                    break
            # 请求 json
            dir_id = int(dir_id) - 1
            dir_json = {'dirname': dirs['data'][dir_id]}
            self.send_operation(dir_json)
            self.show_dir()
            # 更新 self.curr_path
            self.curr_path = os.path.join(self.curr_path, dir_json['dirname'])
            logging.info('self.curr_path是否更新:%s' %self.curr_path)
        elif dirs['status_code'] == '212':
            print('当前目录:%s,无子目录~' % self.curr_path)

    def make_dir(self):
        """新建目录"""
        while True:
            dirname = input('请输入文件夹名称: ')
            if re.findall('[^a-zA-Z\d]', dirname):
                print('文件夹名称只能由字母或数字组成，请重新输入～')
            else:
                break
        mkdir_json = {'dirname': dirname}
        self.send_operation(mkdir_json)
        status_code = self.recv_operation_status()['status_code']
        if status_code == '209':
            print('目录:%s,创建成功,当前路径下包含如下文件和文件夹:' % dirname)
        elif status_code == '210':
            print('目录:%s,创建失败，当前目录存在同名文件夹～' % dirname)
        # 查看当前目录
        self.show_dir()

    def show_dir(self):
        """查看当前目录"""
        dirs = self.recv_operation_status()
        logging.debug('响应:%s' %dirs)
        if dirs['status_code'] == '215':
            for id, dir in enumerate(dirs['data'], 1):
                print('%s: %s' %(id, dir))
        elif dirs['status_code'] == '216':
            print('当前目录:%s, 是空文件夹～' % self.curr_path)

    def upload(self):
        """上传文件"""
        print('in upload')

    def download(self):
        """下载文件"""
        print('in download')

    def send_operation(self, operation):
        """
        向服务端发送即将进行的操作
        :param operation: 函数名
        :return:
        """
        operation = SerializeUtils.json_dumps(operation)
        operation_blen = struct.pack('i', len(operation.encode('utf-8')))
        self.sk.send(operation_blen)
        self.sk.send(operation.encode('utf-8'))

    def recv_operation_status(self):
        """
        接收服务端返回的接口状态码 {'status_code': None}
        :return:
        """
        operation_blen = struct.unpack('i', self.sk.recv(4))[0]
        operation = SerializeUtils.json_loads(self.sk.recv(operation_blen).decode('utf-8'))
        return operation

    def home_menus(self):
        """
        FTP客户端首页
        :return:
        """
        print('欢迎进入TransmitFTP客户端'.center(100, '='))
        for index, option in enumerate(self.__home_options, 1):
            print('%s: %s' % (index, option[0]))
        try:
            option = int(input('请选择:')) - 1
            logging.debug('客户端当前操作:%s' % self.__home_options[option][0])
            if option >= 0 and option < len(self.__home_options) and hasattr(self, self.__home_options[option][1]):
                obj = getattr(self, self.__home_options[option][1]) # 反射方法
                if callable(obj):
                    operation = {'operation': self.__home_options[option][1]}
                    self.send_operation(operation) # 告诉客户端即将进行的操作
                    return obj()
        except ValueError:
            print('您选择的功能不存在～')

    def login_menus(self):
        """
        FTP客户端需登录认证的功能
        :return:
        """
        print('欢迎%s登录Transmit客户端～' % self.login_status['login_user'])
        for index, option in enumerate(self.__login_options, 1):
            print('%s: %s' % (index, option[0]))

        try:
            option = int(input('请选择:')) - 1
            logging.debug('客户端当前操作:%s' % self.__login_options[option][0])
            if option >= 0 and option < len(self.__login_options) and hasattr(self, self.__login_options[option][1]):
                obj = getattr(self, self.__login_options[option][1]) # 反射方法
                if callable(obj):
                    operation = {'operation': self.__login_options[option][1]}
                    self.send_operation(operation) # 告诉服务端即将进行的操作
                    return obj()
        except ValueError:
            print('您选择的功能不存在～')
    def show_menus(self):
        """
        根据用户登陆状态显示菜单
        :param login_status: 201 登陆成功， 202 登陆失败
        :return:
        """
        while True:
            ret = self.home_menus() if not self.login_status['status'] else self.login_menus()
            if ret == 'error999':
                break

def run():
    """
    主函数
    :return:
    """
    TransmitClient().show_menus()

if __name__ == '__main__':
    run()
