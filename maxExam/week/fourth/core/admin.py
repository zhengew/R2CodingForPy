# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: admin.py
#@datatime: 2023/4/12 下午1:17
import sys
from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.core.course import Course
from maxExam.week.fourth.conf.settings import course_info_path, stu_course_info, user_info_path
from maxExam.week.fourth.libary.serialize_utils.serialize_control import serialize
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.libary.commons import get_all_course, get_all_user
from maxExam.week.fourth.core.students import Student

class Admin(User):
    """
    管理员类
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
        course_dict = get_all_course(course_info_path)
        cname = input("课程名: ")
        if cname in course_dict:
            print(f"课程:{cname}, 已存在～")
            return
        price = input("价格: ")
        period = input("周期: ")
        teacher = input("授课老师: ")
        begin_time = input("开班时间: ") # yyyy-mm-dd
        end_time = input("结课时间: ")   # yyyy-mm-dd
        cname = Course(cname, price, period, teacher, begin_time, end_time)
        obj = serialize('pickle', course_info_path)
        obj.dump(cname)


    @classmethod
    def create_stu_acc(cls):
        """
        创建学生账号
        注意: 因为用姓名当id，所以不能重名
        :return:
        """
        users_dict = get_all_user(user_info_path)
        sname = input('姓名: ')
        if sname in users_dict:
            print(f"用户{sname}已注册～")
            return
        pwd = input('密码: ')
        sex = input('性别: ')
        birth = input('出生日期: ')
        education = input('学历: ')
        sname = User(sname, pwd, sex, birth, education)
        obj = serialize('pickle', user_info_path)
        obj.dump(sname)

    @classmethod
    def show_courses(cls):
        """
        查看所有课程
        :return:
        """
        course_dict = get_all_course(course_info_path)
        for cname in course_dict:
            print(cname, course_dict[cname])

    @classmethod
    def show_stu(cls):
        """
        查看所有学生
        :return:
        """
        users_dict = get_all_user(user_info_path)
        for user in users_dict:
            if users_dict[user]['identity'] == '1':
                print(f"{user} {users_dict[user]}")

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
        sys.exit()

if __name__ == '__main__':
    wusir = Admin('wusir', '123456', 'male', '1998-01-01', '本科')
    print(wusir)

    print(type(Admin.command_list()))
    for id, command in enumerate(Admin.command_list(), 1):
        print(id, command[0])

    wusir.create_course('python22期')

