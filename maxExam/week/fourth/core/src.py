# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: src.py
#@datatime: 2023/4/12 下午1:11

"""
选课系统核心逻辑
"""
from maxExam.week.fourth.libary.commons import login
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.core.user import User
from maxExam.week.fourth.core.admin import Admin
from maxExam.week.fourth.core.students import Student

def run():
    while True:
        login_user = login()
        print(login_user) # {'login_name': 'alex', 'identity': '1'} {'login_name': 'wusir', 'identity': '0'}
        if login_user:
            clas_obj = Admin if login_user['identity'] == '0' else Student
            ident = '管理员' if login_user['identity'] == '0' else '学生'
            print(f"尊敬的{ident}用户{login_user['login_name']}，欢迎进入选课系统～")
            while True:
                for id, command in enumerate(clas_obj.command_list(), 1):
                    print(f"{id}: {command[0]}")
                option = input('请选择:').strip()
                if hasattr(clas_obj, clas_obj.command_list()[int(option)-1][1]):
                    ret = getattr(clas_obj, clas_obj.command_list()[int(option)-1][1])
                    if callable(ret):
                        ret()
        else:
            print("用户名或密码错误～")

if __name__ == '__main__':
    run()