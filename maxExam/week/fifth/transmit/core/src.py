# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: src.py
# @datatime: 2023/5/6 07:17

"""
FTP核心逻辑
"""
import logging
import socketserver
import struct
import os
import hashlib
import time

from maxExam.week.fifth.transmit.conf.setting import ConfingHandler
from maxExam.week.fifth.transmit.lib.serializeUtils import SerializeUtils
from maxExam.week.fifth.transmit.lib.common import Common

logging.basicConfig(level=logging.DEBUG)


class TransmitServer(socketserver.BaseRequestHandler):
    """
    FTP服务端程序入口
    """
    __home_options = ['login', 'register', 'exit']
    __login_options = ['upper_dir', 'lower_dir', 'make_dir', 'show_dir', 'upload', 'download', 'exit']

    def handle(self):
        """
        :login_status 当前登陆用户状态
        :operation_status 响应状态码
        :curr_path 用户当前所在目录
        :return:
        """
        self.login_status = {'login_user': None, 'status': False}
        self.operation_status = {'status_code': None}
        self.curr_path = None
        conn = self.request
        print(conn)
        while True:
            try:
                # 服务端需要先知道客户端要调用哪些功能
                self.home_menus(conn)
            except ConnectionResetError:
                break
            except struct.error:
                pass

    def send_operation_status(self, conn, operation_status: dict):
        """
        向客户端发送接口状态码
        :param conn:
        :param operation_status: 状态码 {'status_code': None}
        :return:
        """
        operation = SerializeUtils.json_dumps(operation_status)
        operation_blen = struct.pack('i', len(operation.encode('utf-8')))
        conn.send(operation_blen)
        conn.send(operation.encode('utf-8'))

    def login(self, conn):
        """
        登录
        状态码: 201-登录成功, 202-登录失败
        :param conn:
        :return:
        """
        login_user = self.recv_operation(conn)
        users = Common.get_all_users() # 当前已注册用户
        if login_user['username'] in users and Common.get_pwd_md5(ConfingHandler.private_key, login_user['pwd']) == users[login_user['username']]:
            # 更新self.login_status
            self.login_status['login_user'] = login_user['username']
            self.login_status['status'] = True
            logging.debug('当前登录用户:%s' % self.login_status)
            # 更新用户当前所在目录(默认在家目录)
            self.curr_path = os.path.join(ConfingHandler.home_path, login_user['username']+os.sep)
            logging.debug('当前登录用户%s所在目录:%s' %(login_user['username'], self.curr_path))
            # 更新状态吗
            self.operation_status['status_code'] = '201'
        else:
            self.operation_status['status_code'] = '202'
        # 向客户端发送注册接口响应结果
        self.send_operation_status(conn, self.operation_status)

    def register(self, conn):
        """
        注册
        状态吗: 203-注册成功, 204-注册失败
        服务端接收 {'username': 'alex', 'pwd': 通过公钥加密后的md5}
        :return:
        """
        # 接收客户端注册用户信息，判断是否为已注册用户，并返回是否注册成功
        reg_user = self.recv_operation(conn)
        if reg_user['username'] not in Common.get_all_users():
            self.operation_status['status_code'] = '203'
            # 私钥密码加密后保存用户信息
            reg_user['pwd'] = Common.get_pwd_md5(ConfingHandler.private_key, reg_user['pwd'])
            logging.debug('服务端私钥加密后的密码:%s' % reg_user['pwd'])
            SerializeUtils.json_dump(ConfingHandler.users_path, reg_user)
            # 为注册用户创建家目录
            Common.make_home_dir(reg_user['username'])
        else:
            self.operation_status['status_code'] = '204'
        # 向客户端发送注册接口响应结果
        self.send_operation_status(conn, self.operation_status)

    def exit(self, conn):
        """
        退出逻辑，需要服务端更新登录状态
        :return:
        """
        self.login_status['login_user'] = None
        self.login_status['status'] = False
        logging.debug('客户端退出后更新当前登录用户信息:%s' %self.login_status)

    def upper_dir(self, conn):
        """
        上一级目录
        判断当前目录的上一级目录是否为当前用户的家目录的上一级目录；
        :status_code: 231-成功, 214-失败
        :upper_dir:当前目录的上一级目录
        :home_dir:用户家目录
        :param conn:
        :return: {'data': sub_dir, 'status_code': '213'}
        """
        upper_dir = os.path.dirname(self.curr_path)
        logging.debug('当前目录的上一级目录:%s' %upper_dir)
        home_dir = ConfingHandler.home_path
        if upper_dir not in home_dir:
            # 非用户家目录
            self.operation_status['status_code'] = '213'
            # 更新 self.curr_path
            self.curr_path = upper_dir
        else:
            # 用户家目录
            self.operation_status['status_code'] = '214'
        # 发送请求响应，并打印当前目录
        dirs = {'data': self.curr_path, 'status_code': self.operation_status['status_code']}
        self.send_operation_status(conn, dirs)
        self.show_dir(conn)
    def lower_dir(self, conn):
        """
        下一级目录
        向客户端发送当前目录下的所有子目录
        接收客户端端请求，更新self.curr_path
        向客户端发送响应: {'data': sub_dir, 'status_code': '211'}
        :status_code: 211-下一级目录查看成功, 212-下一级目录查看失败(无子文件夹)
        :param conn:
        :return:
        """
        sub_dir = Common.get_curr_path_dirs(self.curr_path)
        # 发送请求响应状态码
        if sub_dir:
            self.operation_status['status_code'] = '211'
            # 当前目录下存在子目录
            dirs = {'data': sub_dir, 'status_code': self.operation_status['status_code']}
            self.send_operation_status(conn, dirs)
            dir_json = self.recv_operation(conn)
            # 像客户端发送子目录信息
            self.curr_path = os.path.join(self.curr_path, dir_json['dirname'])
            self.show_dir(conn)
        else:
            self.operation_status['status_code'] = '212'
            dirs = {'data': sub_dir, 'status_code': self.operation_status['status_code']}
            self.send_operation_status(conn, dirs)
    def make_dir(self, conn):
        """
        新建目录
        在用户当前所在路径下新建目录
        :status_code: 209 - 创建目录成功， 210 - 创建目录失败
        :param conn:
        :return:
        """
        dirname = self.recv_operation(conn)['dirname']
        if dirname not in os.listdir(self.curr_path):
            abs_path = os.path.join(self.curr_path, dirname)
            os.mkdir(abs_path)
            self.operation_status['status_code'] = '209'
        else:
            self.operation_status['status_code'] = '210'
        # 新建目录接口响应
        self.send_operation_status(conn, self.operation_status)
        # 创建完目录，客户端查看当前文件夹
        self.show_dir(conn)

    def show_dir(self, conn):
        """
        查看当前目录, 需要保存用户当前所在的目录
        :param conn:
        :return:
        """
        data = sorted([i for i in os.listdir(self.curr_path) if not i.startswith('.')], key=lambda i: i.lower())
        if data:
            self.operation_status['status_code'] = '215'
        else:
            self.operation_status['status_code'] = '216'
        dirs = {'data': data, 'status_code': self.operation_status['status_code']}
        logging.debug('当前目录的文件和文件夹:%s'% dirs)
        self.send_operation_status(conn, dirs)

    def upload(self, conn):
        """
        上传文件
        需要判断文件一致性；是否存在同名文件；如果同名文件需判断是否为同一个文件
        :upload_json:{'filename':xxx, 'size': xxx}
        :status_code: 205-上传成功， 206-上传失败
        :param conn:
        :return:
        """
        # 接收客户端文件上传请求json
        upload_json = self.recv_operation(conn)
        filesize = upload_json['size']
        # upload_file_abspath = os.path.join(self.curr_path, upload_json['filename'])
        upload_file_abspath = Common.get_abspath(self.curr_path, upload_json['filename'])
        md5 = hashlib.md5()  # 计算文件md5值
        # 接收文件
        received_size = 0 # 服务端已接收的文件大小
        with open(upload_file_abspath, mode='wb') as f:
            while filesize > 0:
                left_size = 2048 if filesize > 2048 else filesize # 避免与接收md5粘包
                content = conn.recv(left_size)
                filesize -= len(content)
                received_size += len(content)
                f.write(content)
                md5.update(content)
                logging.debug('文件上传进度:%s' % received_size)
        md5_value = md5.hexdigest()
        # 接收客户端发送的md5值并与服务端比较
        file_md5_json = self.recv_operation(conn)
        self.operation_status['status_code'] = '205' if md5_value == file_md5_json['md5'] else '206'
        self.send_operation_status(conn, self.operation_status)
        logging.debug('服务端接收文件完毕:%s' % file_md5_json)

    def download(self, conn):
        """
        下载文件
        向客户端发送当前目录下的可下载文件
        接收客户端选择的下载文件信息
        向客户端传输文件
        校验文件一致性
        :status_code: 207-下载成功, 208-下载失败
        :param conn:
        :return:
        """
        # 向客户端发送当前目录下的可下载文件
        curr_path_files = Common.get_curr_path_files(self.curr_path)
        # 判断当前目录是否有可下载的文件
        if not curr_path_files:
            self.operation_status['status_code'] = '208'
            download_files = {'data': curr_path_files, 'status_code': self.operation_status['status_code']}
            self.send_operation_status(conn, download_files)
            logging.debug('当前目录:%s,无可下载的文件: %s' %(self.curr_path, curr_path_files))
            return
        download_files= {'data': curr_path_files, 'status_code': self.operation_status['status_code']}
        self.send_operation_status(conn, download_files)
        # 接收客户端文件下载请求
        download_file_json = self.recv_operation(conn)
        # 向客户端返回文件下载json
        filename = download_file_json['filename']
        download_file_abspath = Common.get_abspath(self.curr_path, filename)
        filesize = os.path.getsize(download_file_abspath)
        download_json = {'filename': filename, 'size': filesize}
        logging.debug('服务端要发送的文件信息:%s' % download_json)
        self.send_operation_status(conn, download_json)
        # 开始下载文件
        md5 = hashlib.md5()
        sended_size = 0  # 客户端已发送的文件大小
        with open(download_file_abspath, mode='rb') as f:
            while filesize > 0:
                content = f.read(2048)
                filesize -= len(content)
                sended_size += len(content)
                conn.send(content)
                md5.update(content)
                logging.debug('文件上传进度:%s' %filesize)
        # 接收客户端发送的md5值，如果md5相同，则下载成功，不同则下载失败
        md5_value = md5.hexdigest()
        file_md5_json = self.recv_operation(conn)
        logging.debug('服务端下载文件任务执行完毕，md5值:%s' % file_md5_json)
        # 向客户端发送md5校验响应
        self.operation_status['status_code'] = '207' if md5_value == file_md5_json['md5'] else '208'
        self.send_operation_status(conn, self.operation_status)
        logging.debug('服务端下载文件任务执行完毕:%s' % file_md5_json)


    def recv_operation(self, conn):
        """
        接收客户端即将进行的操作
        :param conn:
        :return: 字符串类型的函数名
        """
        operation_blen = struct.unpack('i', conn.recv(4))[0]
        operation = SerializeUtils.json_loads(conn.recv(operation_blen).decode('utf-8'))
        return operation

    def home_menus(self, conn):
        """服务端主逻辑"""
        operation = self.recv_operation(conn)['operation']
        if not self.login_status['status'] and operation in self.__home_options:
            getattr(self, operation)(conn)
        elif self.login_status['status'] and operation in self.__login_options:
            getattr(self, operation)(conn)
        # 重置接口状态码
        self.operation_status['status_code'] = None


def run():
    """
    启动服务
    :return:
    """
    server = socketserver.ThreadingTCPServer(ConfingHandler.server_addr, TransmitServer)
    server.serve_forever()



if __name__ == '__main__':
    run()
