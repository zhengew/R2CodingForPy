# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: students.py
#@datatime: 2023/4/12 下午1:14

from user import User

class Student(User):
    def __init__(self, name, pwd, sex, birth, education):
        super(Student, self).__init__(name, pwd, sex, birth, education)
        self.major_course = [] # 选修课程，可以选修多门课

    def show_courses(self):
        """
        查看所有课程
        :return:
        """
        pass

    def select_courses(self):
        """
        选修课程
        :return:
        """
        pass

    def show_selected_courses(self):
        """
        查看已选修的课程信息
        :return:
        """
        pass

if __name__ == '__main__':
    yuwenyang = Student('于文洋', '123456', 'male', '1998-01-01', '本科')
    print(yuwenyang)