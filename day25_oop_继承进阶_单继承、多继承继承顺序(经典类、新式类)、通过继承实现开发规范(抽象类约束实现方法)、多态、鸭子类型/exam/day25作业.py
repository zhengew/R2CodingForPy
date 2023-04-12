# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: day25作业.py
# @datatime: 2023/4/5 21:14

# **1.面向对象中为什么要有继承?**
# 当两个类中有相同或相似的静态变量或绑定方法时，使用继承可以减少代码的重用，提高代码可读性，规范编程模式

# **2.Python继承时，查找成员的顺序遵循什么规则?**
# Python2中的经典类遵循深度优先规则，Python2和Python3中的新式类遵循广度优先规则

# **3.看代码写结果
# class Base1:
#     def f1(self):
#         print('base1.f1')
#     def f2(self):
#         print('base1.f2')
#     def f3(self):
#         print('base1.f3')
#         self.f1()
#
# class Base2:
#     def f1(self):
#         print('base2.f1')
# class Foo(Base1, Base2):
#     def f0(self):
#         print('foo.f0')
#         self.f3()
#
# obj = Foo()
# obj.f0()

"""
解释：
先搜索并执行Foo自己的f0
然后搜索Foo自己的f3，没找到。由于继承顺序是先Base1再Base2，因此先找Base1，找到了，于是执行Base1的f3。
然后搜索Foo自己的f1，没找到，找Base1，找到了，遂执行之
foo.f0
base1.f3
base1.f1
"""
import re

# **4.看代码写结果
# class Base:
#     def f1(self):
#         print('base.f1')
#
#     def f3(self):
#         self.f1()
#         print('base.f3')
#
#
# class Foo(Base):
#     def f1(self):
#         print('foo.f1')
#
#     def f2(self):
#         print('foo.f2')
#         self.f3()
#
# obj = Foo()
# obj.f2()
"""
先搜做并执行Foo自己的f2, 打印 foo.f2
再再本类中搜索f3,没有就再父类Base中找，找到执行父类中的f3, 
然后先再本类中找f1(),找到后执行本类中的f1方法，打印 foo.f1,执行完后再返回父类中的f3函数打印 base.f3
foo.f2
foo.f1
base.f3
"""

# ** 5.补充代码实现下列需求 **
# 这个代码框里是题干
# user_list = []
# while True:
#     user = input(“请输入用户名:”)
#     pwd = input(“请输入密码:”)
#     email = input(“请输入邮箱:”)

"""
# 需求
1. while循环提示用户输 : 户名、密码、邮箱(正则满足邮箱格式)
2. 为每个用户创建1个对象，并添加到列表中。
3. 当列表中的添加 3个对象后，跳出循环并以此循环打印所有用户的姓名和邮箱
"""
import re

class Users(object):
    """用户类"""
    user_list = []
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

def create_users():
    email_regex = "^\w+@([\da-zA-Z]+[.])+?(com|cn)$"
    while True:
        user = input("请输入用户名:")
        pwd = input("请输入密码:")
        email = input("请输入邮箱:")
        if re.match(email_regex, email):
            obj = Users(user, pwd, email)
            Users.user_list.append(obj)
            if len(Users.user_list) == 3:
                for user in Users.user_list:
                    print(f'用户名:{user.name}, 邮箱:{user.email}')
                break
        else:
            print(f'邮箱不符合规范～{email}')


create_users()

# **7 看代码写结果
# class Base:
#     x = 1
#
# obj = Base()
#
# print(obj.x)
# obj.y = 123
# print(obj.y)
# obj.x = 123
# print(obj.x)
# print(Base.x)

"""
解释：
对象.变量名 = xxx 是赋值操作，相当于再对象self内存空间声明了一个变量
如果要访问类中的成员变量，应该使用类名.的方式

1
123
123
1
"""

# **8.
# class Parent:
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# print(Parent.x, Child1.x, Child2.x)
# Child2.x = 2
# print(Parent.x, Child1.x, Child2.x)
# Child1.x = 3
# print(Parent.x, Child1.x, Child2.x)

"""
解释：
子类继承父类，子类.变量 = xxx,相当于再子类自己的内存空间创建了一个静态成员变量，与父类没有关系
1, 1, 1
1, 1, 2
1, 3, 2
"""

# **9.
# class Foo(object):
#     n1 = '武沛齐'
#     n2 = '金老板'
#     def __init__(self):
#         self.n1 = 'eva'
#
# obj = Foo()
# print(obj.n1)
# print(obj.n2)

"""
eva
金老板
"""

# **9.
class Foo(object):
    n1 = '武沛齐'
    def __init__(self,name):
        self.n2 = name
obj = Foo('太白')
print(obj.n1)
print(obj.n2)
print(Foo.n1)
print(Foo.n2)

"""
武沛奇
太白
武沛奇
报错，Foo类中没有 n2, 属性未定义 # AttributeError: type object 'Foo' has no attribute 'n2'. Did you mean: 'n1'?
"""


