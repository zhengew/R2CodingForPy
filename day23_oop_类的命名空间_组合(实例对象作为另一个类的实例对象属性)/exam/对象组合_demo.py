# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/1 16:32
# 文件名称: 对象组合_demo.py

# 练习 :
# 对象变成了一个属性
# 班级类
    # 包含一个属性 - 课程
# 课程
    # 课程名称
    # 周期
    # 价格

# 创建两个班级 linux57
# 创建两个班级 python22
# 查看linux57期的班级所学课程的价格
# 查看python22期的班级所学课程的周期

class Student:
    """
    学生类
    """
    def __init__(self,name,sex,age,number,clas,phone):
        self.name = name
        self.sex = sex
        self.age = age
        self.number = number
        self.clas = clas
        self.phone = phone
class Clas:
    """
    班级类
    """
    def __init__(self,cname,begint,teacher, course):
        self.cname = cname
        self.begint = begint
        self.teacher = teacher
        self.course = course
class Course():
    """
    课程类
    """
    def __init__(self, cname, period, price):
        self.cname = cname
        self.period = period
        self.price = price

linux = Course('linux', '5 Month', '19800.00')
python = Course('python', '6 Month', '20000.00')

linux57 = Clas('linux57', '20230101', 'wusir', linux)
python22 = Clas('python22', '20230228', 'taibai', python)

print(linux57.course.price)
print(python22.course.price)

linux57.course.price = '21500.00'
print(linux57.course.price)
