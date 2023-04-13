# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/13 07:10

from maxExam.week.fourth.libary.serialize_utils import *
from maxExam.week.fourth.conf.settings import user_info_path


alex = {'name': 'alex', 'pwd': '94e4ccf5e2749b0bfe0428603738c0f9'}
def auth(f):
    """
    登录认证装饰器
    :param f: 被装饰函数
    :return:
    """
    def inner(*args, **kwargs):
        """函数执行前进行登录认证"""
        name = inner("请输入用户名: ")
        pwd = input("请用输入密码: ")
        ret = f()
        """执行后return函数返回值"""
        return ret
    return inner


def get_all_user(path:str):
    obj = serialize('pickle', user_info_path)
    print(list(obj.load()))

if __name__ == '__main__':
    get_all_user(user_info_path)
