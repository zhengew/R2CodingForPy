# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: students.py
#@datatime: 2023/4/12 下午1:14
import sys

from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.libary.commons import get_all_course
from maxExam.week.fourth.conf.settings import course_info_path, login_user_path, user_info_path, stu_course_info
from maxExam.week.fourth.libary.serialize_utils.serialize_control import serialize
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.conf.settings import course_info_path

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
        course_dict = get_all_course(course_info_path)
        for id, cname in enumerate(course_dict, 1):
            print(f"{id} {cname}: {course_dict[cname]}")

    @classmethod
    def select_courses(cls):
        """
        选修课程
        :return:
        """
        cls.show_courses()
        cname = input("请输入课程名称: ")
        obj_course = serialize('pickle', course_info_path)
        for course in obj_course.load():
            if cname == course.cname:
                # {'login_name': 'alex', 'status': True}
                login_dict = next(serialize('json', login_user_path).load())
                print(login_dict)
                print(course)
                login_user = login_dict['login_name']
                for user in serialize('pickle', user_info_path).load():
                    if user.name == login_user:
                        login_user = Student(user)
                        login_user.major_course.append(course)
                        serialize('pickle', stu_course_info).dump(login_user)
                        break
            return # pass

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