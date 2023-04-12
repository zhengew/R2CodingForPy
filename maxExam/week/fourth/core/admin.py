# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: admin.py
#@datatime: 2023/4/12 下午1:17

from user import User
from course import Course
class Admin(User):
    """
    创建课程、创建学生学生账号、查看所有课程、查看所有学生、查看所有学生的选课情况、退出程序
    """

    def __init__(self, name, pwd, sex, birth, education):
        super(Admin, self).__init__(name, pwd, sex, birth, education)
        self.identity = 0

    def create_course(self):
        """
        创建课程
        :return:
        """
        pass

    def create_stu_acc(self):
        """
        创建学生账号
        :return:
        """
        pass

    def show_courses(self):
        """
        查看所有课程
        :return:
        """
        pass

    def show_stu(self):
        """
        查看所有学生
        :return:
        """
        pass

    def show_stu_course(self):
        """
        查看所有学生选课情况
        :return:
        """
        pass

    def quit(self):
        """
        退出系统
        :return:
        """
        pass

if __name__ == '__main__':
    wusir = Admin('wusir', '123456', 'male', '1998-01-01', '本科')
    print(wusir)