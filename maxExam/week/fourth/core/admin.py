# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: admin.py
#@datatime: 2023/4/12 下午1:17

from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.core.course import Course
class Admin(User):
    """
    创建课程、创建学生学生账号、查看所有课程、查看所有学生、查看所有学生的选课情况、退出程序
    """

    __command_list = [('创建课程', 'create_course'), ('查看所有课程', 'show_courses'),
                      ('创建学生账号', 'create_stu_acc'), ('查看所有学生', 'show_stu'),
                      ('查看学生选课情况', 'show_stu_course'), ('退出系统', 'quit')]

    def __init__(self, name, pwd, sex, birth, education):
        super(Admin, self).__init__(name, pwd, sex, birth, education)
        self.identity = 0
    @classmethod
    def command_list(cls):
        return cls.__command_list
    @classmethod
    def create_course(cls):
        """
        创建课程
        :return:
        """
        print('in create_course')

    @classmethod
    def create_stu_acc(cls):
        """
        创建学生账号
        :return:
        """
        print('in create_stu_acc')

    @classmethod
    def show_courses(cls):
        """
        查看所有课程
        :return:
        """
        print('in show_courses')

    @classmethod
    def show_stu(cls):
        """
        查看所有学生
        :return:
        """
        print('in show_stu')

    @classmethod
    def show_stu_course(cls):
        """
        查看所有学生选课情况
        :return:
        """
        print('in show_stu_course')

    @classmethod
    def quit(cls):
        """
        退出系统
        :return:
        """
        print('in quit')

if __name__ == '__main__':
    wusir = Admin('wusir', '123456', 'male', '1998-01-01', '本科')
    print(wusir)

    print(type(Admin.command_list()))
    for id, command in enumerate(Admin.command_list(), 1):
        print(id, command[0])
