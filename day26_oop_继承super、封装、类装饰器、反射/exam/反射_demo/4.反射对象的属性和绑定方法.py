# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 4.反射对象的属性和绑定方法.py
# @datatime: 2023/4/8 14:28

"""
目标: 理解反射原理
反射对象的属性和绑定方法
"""
class Student(object):
    def __init__(self, name, birth, hoby):
        self.__name = name
        self.__birth = birth
        self.hoby = hoby

    @property
    def getName(self):
        pass
    @getName.getter
    def getName(self):
        return self.__name
    @property
    def getBirth(self):
        pass
    @getBirth.getter
    def getBirth(self):
        return self.__birth

if __name__ == '__main__':
    alex = Student('alex', '19901108', 'run')
    print(getattr(alex, 'getName')) # alex  反射对象的绑定方法

    hoby = getattr(alex, 'hoby') # 反射对象的私有属性
    print(hoby) # run
