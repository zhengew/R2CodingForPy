# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: start.py
#@datatime: 2023/4/12 下午1:10

from maxExam.week.fourth.core.src import run
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.core.students import Student
from maxExam.week.fourth.core.admin import Admin

"""
启动程序
"""

def main():
    run()

if __name__ == '__main__':
    main()