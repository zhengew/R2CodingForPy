# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: settings.py
#@datatime: 2023/4/12 下午1:11
import os


# 根目录
__base_path = os.path.dirname(os.path.dirname(__file__))
# 用户注册文件路径
user_info_path= os.path.join(__base_path, 'db', 'user_info')
# 课程信息
course_info_path = os.path.join(__base_path, 'db', 'course_info')
# 当前登录人
login_user_path = os.path.join(__base_path, 'db', 'login_info')
# 学生选课信息
stu_course_info = os.path.join(__base_path, 'db', 'stu_course_info')
# 用户信息备份路径
user_info_temp_path = os.path.join(__base_path, 'db', 'user_info_temp')


if __name__ == '__main__':
    print(__base_path)
    print(user_info_path)
    print(course_info_path)