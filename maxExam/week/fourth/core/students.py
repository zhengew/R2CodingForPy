# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: students.py
#@datatime: 2023/4/12 下午1:14
import sys

from maxExam.week.fourth.core.user import User

class Student(User):

    __command_list = [('查看所有课程', 'show_courses'), ('选择课程', 'select_courses'),
                      ('查看已选课程', 'show_selected_courses'), ('退出', 'quit')]
    def __init__(self, name, pwd, sex, birth, education):
        super(Student, self).__init__(name, pwd, sex, birth, education)
        self.major_course = [] # 选修课程，可以选修多门课
    @classmethod
    def command_list(cls):
        return cls.__command_list

    @classmethod
    def show_courses(cls):
        """
        查看所有课程
        :return:
        """
        print('in show_courses')

    @classmethod
    def select_courses(cls):
        """
        选修课程
        :return:
        """
        print('in select_courses')

    @classmethod
    def show_selected_courses(cls):
        """
        查看已选修的课程信息
        :return:
        """
        print('in show_selected_courses')

    @classmethod
    def quit(cls):
        """
        退出系统
        :return:
        """
        sys.exit()

if __name__ == '__main__':
    yuwenyang = Student('于文洋', '123456', 'male', '1998-01-01', '本科')
    print(yuwenyang)
    yuwenyang.command_list()