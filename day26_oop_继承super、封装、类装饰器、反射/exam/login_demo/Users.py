# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: Users.py
# @datatime: 2023/4/6 下午12:20

class Users(object):
    """用户类"""
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email