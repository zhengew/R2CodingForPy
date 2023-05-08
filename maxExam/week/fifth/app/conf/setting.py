# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: setting.py
# @datatime: 2023/5/6 08:02

import os
class ConfingHandler:
    # 系统标识
    os_type = os.name  # posix -> linux/mac os, nt -> windows

    # 服务端IP
    server_addr = ('127.0.0.1', 9002)

    # 客户端公钥
    public_key = 'transmit'

    # 服务端文件根目录
    home_path = r'/Users/erwei.zheng/Downloads/home/' if os_type == 'posix' else r'D:\\home\\'

    # 文件断点续传分片大小 10M
    part_size = 1024 * 1024 * 1024 * 10