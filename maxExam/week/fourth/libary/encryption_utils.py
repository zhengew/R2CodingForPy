# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: encryption_utils.py
# @datatime: 2023/4/12 21:04

import hashlib

class Encryption(object):

    @staticmethod
    def get_md5(name, pwd):
        m = hashlib.md5(name.encode('utf-8'))
        m.update(pwd.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def get_sha256(name, pwd):
        sha = hashlib.sha256(name.encode('utf-8'))
        sha.update(pwd.encode('utf-8'))
        return sha.hexdigest()


if __name__ == '__main__':
    ret = Encryption.get_md5('alex', '123456')
    print(ret)

    ret2 = Encryption.get_sha256('alex', '123456')
    print(ret2)