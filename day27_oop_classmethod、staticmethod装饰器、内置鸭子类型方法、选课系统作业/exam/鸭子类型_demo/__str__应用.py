# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __str__应用.py
# @datatime: 2023/4/11 22:52

"""
目标：__str__应用
打印班级对象，获取班级信息
"""

class Clas(object):
    def __init__(self, cname, teacher, period):
        self.cname = cname
        self.teacher = teacher
        self.period = period
        self.students = []
    def __str__(self):
        """打印实例对象时的返回值"""
        return "%s" %{'name': self.cname, 'teacher': self.teacher, "period": self.period, 'students': self.students}

if __name__ == '__main__':
    py22 = Clas('py22', 'alex', '6month')
    py22.students.append('大壮')
    py22.students.append('于文洋')

    print(py22) # {'name': 'py22', 'teacher': 'alex', 'period': '6month', 'students': ['大壮', '于文洋']}