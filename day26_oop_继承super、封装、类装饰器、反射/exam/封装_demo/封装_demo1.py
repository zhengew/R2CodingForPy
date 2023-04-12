# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 封装_demo1.py
# @datatime: 2023/4/7 22:05

"""
目标:理解封装的概念，类的成员私有化，
成员私有化后类内可以访问，类外不能访问的原因:
类内自动在私有成员名字前面加了: _类名
"""
import hashlib
class User(object):
    __Counter = 0 # 私有静态变量
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd # 私有的实例成员
    def __get_md5(self):
        """私有绑定方法"""
        obj = hashlib.md5(self.name.encode('utf-8'))
        obj.update(self.__pwd.encode('utf-8'))
        return obj.hexdigest()
    def getPwd(self):
        """对外提供查看pwd方法"""
        return self.__get_md5()
    def setPwd(self, new_pwd):
        """对外提供修改pwd方法"""
        self.__pwd = new_pwd

if __name__ == '__main__':
    taibai = User('太白', '123456')
    print(taibai.__dict__) # {'name': '太白', '_User__pwd': '123456'}
    print(User.__dict__) # {'_User__Counter': 0, '_User__get_md5': <function User.__get_md5 at 0x10a23a200>}