# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: common.py
# @datatime: 2023/5/7 09:56

import hashlib
import hmac

class Common(object):
    """客户端公共组件"""

    @staticmethod
    def get_pwd_md5(public_key: str, pwd: str, digestmod='md5'):
        """生成服务端md5值"""
        return hmac.new(public_key.encode('utf-8'), pwd.encode('utf-8'), digestmod=digestmod).hexdigest()


if __name__ == '__main__':
    ret = Common.get_pwd_md5('test1', '123456')
    print(ret, len(ret))