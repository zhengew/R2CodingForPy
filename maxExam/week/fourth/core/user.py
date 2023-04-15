# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: user.py
#@datatime: 2023/4/12 下午1:18
import time
import sys
from maxExam.week.fourth.libary.encryption_utils import Encryption
from maxExam.week.fourth.libary.serialize_utils.serialize_control import serialize
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle
from maxExam.week.fourth.libary.commons import update_login_status, get_all_course
from maxExam.week.fourth.conf.settings import course_info_path

class User(object):
    """
    用户类: 管理员类、学生类、教师类的父类
    """
    def __init__(self, name, pwd, sex, birth, education):
        """
        用户属性
        :param name: 姓名
        :param sex: 性别
        :param birth: 出生年月日 yyyy-mm-dd
        :param education: 学历
        :parameter __identity: 身份 0-管理员 1-学生 2-教师
        """
        self.name = name
        self.__pwd = pwd
        self.sex = sex
        self.birth = birth # yyyy-mm-dd
        self.education = education
        self.__identity = '1'

    def __str__(self):
        """
        返回实例对象属性
        :return:
        """
        return "%s" % self.__dict__
    @property
    def age(self):
        """年龄"""
        struct_t = time.localtime()
        y = int(self.birth[:4])
        m = int(self.birth[5:7])
        d = int(self.birth[-2:])
        age_res = struct_t.tm_year - int(self.birth[:4])
        return age_res \
            if (struct_t.tm_mon > m or (struct_t.tm_mon == m and struct_t.tm_mday >= d)) \
            else (age_res - 1)

    @property
    def identity(self):
        """
        查看用户身份
        :return:
        """
        return self.__identity
    @identity.setter
    def identity(self,ident):
        """
        修改用户身份
        :param ident: 默认 1-学生
        :return:
        """
        self.__identity = ident

    @property
    def pwd(self):
        """
        查看用户密码(加密后的密码)
        :return:
        """
        return Encryption.get_md5(self.name, self.__pwd)
    @pwd.setter
    def pwd(self, new_password):
        """
        修改用户密码
        :param new_password:
        :return:
        """
        self.__pwd = new_password

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
    def quit(cls):
        """
        退出系统
        :return:
        """
        update_login_status()
        sys.exit()

if __name__ == '__main__':
    pass

    # for i in obj.load():
    #     print(i)

