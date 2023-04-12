# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/31 07:16
# 文件名称: Circle.py

from math import pi
class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        面积 pi*radius**2
        :return:
        """
        return self.radius**2 * pi

    def perimeter(self):
        """
        周长 2 * radius * pi
        :return:
        """
        return 2 * pi * self.radius

c1 = Circle(5)
c2 = Circle(10)
print(c1.__dict__) # {'radius': 5}
print(c2.__dict__) # {'radius': 10}

print(f"c1的面积: {c1.area()}")
print(f"c1的周长: {c1.perimeter()}")
