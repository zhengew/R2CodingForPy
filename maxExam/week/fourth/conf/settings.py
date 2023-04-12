# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: settings.py
#@datatime: 2023/4/12 下午1:11
import os


class Settings(object):
    # 根目录
    base_path = os.path.dirname(os.path.dirname(__file__))
    # 用户注册文件路径
    user_info = os.path.join(base_path, 'db', 'userinfo')
    # 课程信息文件路径
    course_info = os.path.join(base_path, 'db', 'course_info')

if __name__ == '__main__':
    print(Settings.base_path)
    print(Settings.user_info)
    print(Settings.course_info)
