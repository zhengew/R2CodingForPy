# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: settings.py
# @datatime: 2023/5/6 07:16

import os

class ConfingHandler:
    # 系统标识
    os_type = os.name # posix -> linux/mac os, nt -> windows

    # 服务端IP
    server_addr = ('127.0.0.1', 9002)
    # 系统分割符
    __sep = os.sep

    # 项目根目录
    base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + __sep)

    # 用户信息
    users_path = os.path.join(base_path, 'db', 'users')

    # 保存服务端文件的md5值、文件大小、文件名信息
    files_md5 = os.path.join(base_path, 'db', 'files_md5')

    # 服务端公钥
    public_key = 'transmit'

    # 服务端私钥
    private_key = 'transmit_server'

    # 服务端文件根目录
    # '/Users/erwei.zheng/Downloads/home/'
    # '/home/zew/Downloads/home'
    home_path = r'/Users/erwei.zheng/Downloads/home/' if os_type == 'posix' else r'D:\\home\\'

if __name__ == '__main__':
    print(ConfingHandler.base_path)
    print(ConfingHandler.files_md5)
