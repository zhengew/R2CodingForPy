# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/27 20:31
# 文件名称: os_module_demo.py

import os
import sys
import time

# .path系列
# ret = os.path.abspath('.')
# print(ret) # /Users/erwei.zheng/PycharmProjects/R2CodingForPython/day21_递归习题讲解、shutil、logging模块/exam
#
# ret = os.path.split('/Users/erwei.zheng/Downloads/test_download_mail/test.txt')
# print(ret) # ('/Users/erwei.zheng/Downloads/test_download_mail', 'test.txt')
#
# ret = os.path.dirname(__file__)
# print(ret)
#
# ret = os.path.basename('/Users/erwei.zheng/Downloads/test_download_mail/test.txt')
# print(ret)
#
# ret = os.path.exists('/Users/erwei.zheng/Downloads/test_download_mail/')
# print(ret) # True

# ret = os.path.isabs('/Users/erwei.zheng/Downloads/test_download_mail/')
# print(ret) # True
#
# ret = os.path.join(os.path.dirname(__file__), 'test1.txt')
# print(ret)
#
# ret = os.path.getsize('/Users/erwei.zheng/Downloads/')
# print(ret) # 2624
#
# ret = os.path.getatime('/Users/erwei.zheng/Downloads/')
# print(ret) # 1679921711.534007
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ret))) # 2023-03-27 20:55:11
#
#
# ret = os.path.getmtime('/Users/erwei.zheng/Downloads/')
# print(ret) # 1679582685.2479136
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ret))) # 2023-03-23 22:44:45
#
# # os.makedirs('test1/test2')
#
# # ret = os.listdir('.')
# # print(ret)
#
# ret = os.stat('/Users/erwei.zheng/Downloads')
# print(ret) # os.stat_result(st_mode=16832, st_ino=296066, st_dev=16777223, st_nlink=82, st_uid=501, st_gid=20, st_size=2624, st_atime=1679921711, st_mtime=1679582685, st_ctime=1679582685)

# os.system('pwd')
# os.popen('pwd').read()
# ret = os.getcwd()
# print(ret)


print(os.linesep)
print(os.pathsep)
print(os.name) # posix
print(sys.platform) # darwin

