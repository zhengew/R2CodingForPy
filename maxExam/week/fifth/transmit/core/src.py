# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 07:17

"""
FTP核心逻辑
"""

import socketserver

class TransmitServer(socketserver.BaseRequestHandler):
    """
    FTP服务端程序入口
    """

    # def __init__(self):
    #     self.login_status = {'login_user':None, 'status': False} # 保存用户登录状态
    #     super().__init__()

    def handle(self):
        """
        主要逻辑
        :return:
        """
        conn = self.request
        print(conn)
        while True:
            try:
                msg = conn.recv(1024).decode('utf-8')
                conn.send(msg.upper().encode('utf-8'))
            except ConnectionResetError:
                break


def run():
    """
    启动服务
    :return:
    """
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9001), TransmitServer)
    server.serve_forever()

if __name__ == '__main__':
    run()
