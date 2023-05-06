# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 07:17

"""
FTP核心逻辑
"""

import socketserver
from maxExam.week.fifth.transmit.conf.setting import ConfingHandler

class TransmitServer(socketserver.BaseRequestHandler):
    """
    FTP服务端程序入口
    """
    def handle(self):
        """
        @:param: login_status 当前登陆用户状态
        :return:
        """
        self.login_status = {'login_user': None, 'status': False}
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
    server = socketserver.ThreadingTCPServer(ConfingHandler.server_addr, TransmitServer)
    server.serve_forever()

if __name__ == '__main__':
    run()
