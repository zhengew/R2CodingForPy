# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 3.被装饰方法可与私有属性搭配使用.py
# @datatime: 2023/4/8 10:01

"""
目标：理解@property装饰器
1.被装饰的方法，与私有属性搭配使用，方便类外对私有属性的查询和修改
"""
import hashlib
class User(object):
    def __init__(self, name, password):
        self.name = name
        self.__pwd = password
    def __get_md5(self):
        m = hashlib.md5(self.name.encode('utf-8'))
        m.update(self.__pwd.encode('utf-8'))
        return m.hexdigest()
    @property
    def pwd(self):
       pass
    @pwd.getter
    def pwd(self):
        return self.__get_md5()
    @pwd.setter
    def pwd(self, new_password):
        self.__pwd = new_password
    @pwd.deleter
    def pwd(self):
        del self.__pwd

if __name__ == '__main__':
    taibai = User('太白', '123456')
    print(taibai.pwd) # b9d162498e465745204cb4e0c5f738c3
    taibai.pwd = '123' #
    print(taibai.pwd) # ea441fe92388414929ef5ab0645d65a4
    del taibai.pwd
    print(taibai.__dict__) # {'name': '太白'}
    # print(taibai.pwd) # AttributeError: 'User' object has no attribute '_User__pwd'
    # print(taibai.__pwd) # AttributeError: 'User' object has no attribute '__pwd'



