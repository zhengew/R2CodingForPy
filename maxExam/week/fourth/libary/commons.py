# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: commons.py
# @datatime: 2023/4/13 07:10

from maxExam.week.fourth.libary.encryption_utils import Encryption
from maxExam.week.fourth.libary.serialize_utils.serialize_control import serialize
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.conf.settings import user_info_path, course_info_path, login_user_path


def login():
    """
    登陆认证
    保存当前登陆用户到文件中
    """
    users_dict = get_all_user(user_info_path)
    login_name = input("请输入用户名: ").strip()
    login_pwd = input("请用输入密码: ").strip()
    if login_name in users_dict and Encryption.get_md5(login_name, login_pwd) == users_dict[login_name]['pwd']:
        obj = serialize('json', login_user_path)
        obj.dump({'login_name': login_name, 'status': True})
        return {'login_name': login_name, 'identity': users_dict[login_name]['identity']}
    return False


def get_all_user(path:str):
    """
    注册用户信息
    :param path:
    :return: {'alex': {'pwd': '94e4ccf5e2749b0bfe0428603738c0f9', 'identity': '1'}, ...)
    """
    users_dict = {}
    obj = serialize('pickle', path)
    for user in obj.load():
        users_dict[user.name] = {"pwd": user.pwd, "sex": user.sex, "birth": user.birth, "education": user.education, "identity": user.identity}
    return users_dict

def get_all_course(path: str):
    """
    课程信息
    :param path:
    :return: 返回课程信息字典 {'python22期': {'price': '19800.00', 'period': '6 month', 'teacher': '景女神', 'begin_time': '2023-03-01', 'end_time': '2023-09-30'}}
    """
    course_dict = {}
    obj = serialize('pickle', path)
    for course in obj.load():
        course_dict[course.cname] = {"price": course.price, 'period': course.period, 'teacher': course.teacher, 'begin_time': course.begin_time, 'end_time': course.end_time}
    return course_dict


if __name__ == '__main__':
    from maxExam.week.fourth.core.user import User
    d1 = {'name': 'alex', 'age': 10}
    obj = serialize('pickle', user_info_path)
    print([i.__dict__ for i in obj.load()])
    # ret = login()
    # if ret:
    #     print('登录成功～')
    #     print(ret)
    # else:
    #     print('登录失败～')

    c = get_all_course(course_info_path)
    print(c)

    obj = serialize('json', login_user_path)
    print(next(obj.load()))