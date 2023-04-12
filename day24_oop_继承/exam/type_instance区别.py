# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 20:02
# 文件名称: type_instance区别.py

class People(object):
    """人类"""
    def __init__(self, name, age):
        """人类的共有属性"""
class Student(People):
    pass

# from piople_test import People, Student

def main():
    stu1 = Student('alex', 10)
    print(type(stu1) is Student)  # True
    print(type(stu1) is People)  # False
    print(isinstance(stu1, Student))  # True
    print(isinstance(stu1, People))  # True

    print(People.__name__)
    print(People.__module__)
    print(People.__init__.__doc__)
    print(People.__doc__)

if __name__ == '__main__':

    main()