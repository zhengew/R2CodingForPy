# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: students.py
#@datatime: 2023/4/12 下午1:14

from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.libary.commons import get_all_course, get_login_user, update_user_info
from maxExam.week.fourth.conf.settings import course_info_path, user_info_path
from maxExam.week.fourth.libary.serialize_utils.serialize_control import serialize
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle


class Student(User):
    """
    学生类: 查看课程、选课、查看已选课程、退出登录
    """
    __command_list = [('查看所有课程', 'show_courses'), ('选择课程', 'select_courses'),
                      ('查看已选课程', 'show_selected_courses'), ('退出', 'quit')]
    def __init__(self, name, pwd, sex, birth, education):
        super(Student, self).__init__(name, pwd, sex, birth, education)
        self.major_course = [] # 选修课程，可以选修多门课
    def __str__(self):
        """
        返回实例对象属性
        :return:
        """
        return "%s" % self.__dict__
    @classmethod
    def command_list(cls):
        return cls.__command_list

    @classmethod
    def select_courses(cls):
        """
        选修课程
        :return:
        """
        while True:
            cls.show_courses() # 打印课程信息
            cname = input("请输入课程名称: ").strip()
            if cname not in get_all_course(course_info_path):
                print(f'您输入的课程名称不存在')
                continue
            obj_course = serialize('pickle', course_info_path)
            # 拿到选择的课程对象
            for course in obj_course.load():
                if cname == course.cname:
                    # {'login_name': 'alex', 'status': True}
                    login_user = get_login_user()['login_name']
                    for user in serialize('pickle', user_info_path).load():
                        if user.name == login_user:
                            # 判断用户是否已选修该课程
                            if cname in [course.cname for course in user.major_course]:
                                print('您已经选修该课程～\n')
                                return
                            else:
                                # 否则就把选则的课程对象保存到 major_course 列表, 并更新用户信息
                                user.major_course.append(course)
                                update_user_info(user_info_path, user)
                                print(f"恭喜您，选课成功，您目前已选修课程有: {[course.cname for course in user.major_course]}")
                                return

    @classmethod
    def show_selected_courses(cls):
        """
        查看已选修的课程信息
        :return:
        """
        login_user = get_login_user()['login_name']
        user_info = serialize('pickle', user_info_path).load()
        for user in user_info:
            if user.name == login_user:
                print(f"您已选择如下课程:")
                for id, course in enumerate(user.major_course, 1):
                    print(f"{id}: {course.cname}")
                print()

if __name__ == '__main__':
    pass


