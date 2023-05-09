# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: common.py
# @datatime: 2023/5/6 22:18

import hashlib
import hmac
import os
import sys
from maxExam.week.fifth.transmit.lib.serializeUtils import SerializeUtils
from maxExam.week.fifth.transmit.conf.setting import ConfingHandler
class Common(object):
    """公共组件"""

    @staticmethod
    def get_pwd_md5(private_key: str, pwd: str, digestmod='md5'):
        """生成服务端md5值"""
        return hmac.new(private_key.encode('utf-8'), pwd.encode('utf-8'), digestmod=digestmod).hexdigest()

    @staticmethod
    def get_all_users():
        """
        查询当前注册用户信息
        :return: {'alex': '67c190a6a85e82d1673b90f478fdd92a', ...}
        """
        users = {}
        users_path = ConfingHandler.users_path
        for user in SerializeUtils.json_load(users_path):
            users[user['username']] = user['pwd']
        return users

    @staticmethod
    def make_home_dir(dirname: str):
        """
        注册用户新建家目录
        :param dirname:
        :return:
        """
        os.mkdir(os.path.join(ConfingHandler.home_path, dirname))

    @staticmethod
    def get_curr_path_dirs(path: str):
        """
        获取当前路径下的所有文件夹
        :return:
        """
        return sorted(next(os.walk(path))[1], key=lambda i: i.lower())

    @staticmethod
    def get_curr_path_files(path: str):
        """
        获取当前路径下的所有文件
        :param path:
        :return:
        """
        return sorted(next(os.walk(path))[2], key=lambda i: i.lower())


    @staticmethod
    def get_user_home_dir(login_user: str):
        """
        当前登录用户的家目录
        :param login_user:
        :return:
        """
        return os.path.join(ConfingHandler.home_path, login_user)

    @staticmethod
    def processBar(num, total):
        """
        上传下载进度条
        :param num:
        :param total:
        :return:
        """
        rate = num / total
        rate_num = int(rate * 100)
        if rate_num == 100:
            r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
        else:
            r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
        sys.stdout.write(r)
        sys.stdout.flush

    @staticmethod
    def get_abspath(basepath: str, subpath: str):
        """
        获取当前路径下某个文件或文件夹的绝对路径
        :param basepath:
        :param subpath:
        :return:
        """
        abspath = os.path.join(basepath, subpath)
        return abspath

if __name__ == '__main__':
    ret = Common.get_pwd_md5('test1', '123456')
    print(ret, len(ret))

    # Common.make_home_dir('alex')
    dirs = Common.get_curr_path_dirs('/Users/erwei.zheng/PycharmProjects/R2CodingForPy/maxExam/week/fifth')
    print(dirs)