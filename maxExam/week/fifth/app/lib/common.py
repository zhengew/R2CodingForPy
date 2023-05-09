# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: common.py
# @datatime: 2023/5/7 09:56

import hashlib
import hmac
import os
import sys

class Common(object):
    """客户端公共组件"""

    @staticmethod
    def get_pwd_md5(public_key: str, pwd: str, digestmod='md5'):
        """生成服务端md5值"""
        return hmac.new(public_key.encode('utf-8'), pwd.encode('utf-8'), digestmod=digestmod).hexdigest()

    @staticmethod
    def get_upload_file_part(filename: str, filesize: int, part_size: int):
        """
        根绝文件大小及分片大小，计算待上传文件分几段上传和每段的实际大小
        :param filesize:
        :param part_size:
        :return:
        """
        quotient, remainder = divmod(filesize, part_size)
        ret = dict()
        for i in range(quotient + 1):
            ret[f'{filename}_{i}'] = part_size if i < quotient else remainder
        return ret

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

    ret = Common.get_upload_file_part('abc',100, 15)
    print(ret, len(ret))