# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 08:01

"""
FTP 客户端入口
"""
import socket
from maxExam.week.fifth.app.conf.setting import ConfingHandler

server_addr = ConfingHandler.server_addr # 服务端IP
sk = socket.socket()
sk.connect(server_addr)

while True:
    sk.send(b'hello')
    content = sk.recv(1024).decode('utf-8')
    print(content)

