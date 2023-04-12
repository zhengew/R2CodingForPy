# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 12:44
# 文件名称: cirque_demo.py

# 第二大题:基于圆形类实现一个圆环类,要求接收参数 外圆半径和内圆半径
# 完成方法 :计算环形面积和环形周长(公式自己上网查)
# 要求,借助组合,要求组合圆形类的对象完成需求

from math import pi

class Circle(object):
    """圆形类"""
    def __init__(self, r):
        """
        :param r: 半径
        """
        self.r = r

    def area_circle(self):
        """圆形面积"""
        return pi * self.r ** 2

    def perimeter(self):
        """圆形周长"""
        return 2 * pi * self.r


class Ring(object):
    """圆环类"""
    def __init__(self, outer_radius, inner_radius):
        """
        圆环初始化时即实例化圆形类
        :param outre_radius: 外圆半径
        :param inner_radius: 内圆半径
        """
        # 避免传参数时先传内圆半径
        outer_radius, inner_radius = (outer_radius, inner_radius) if outer_radius > inner_radius else (inner_radius, outer_radius)
        self.outre_c = Circle(outer_radius)
        self.inner_c = Circle(inner_radius)

    def area_ring(self):
        """
        圆环面积 pi * (outre_radius ** 2 - inner_radius ** 2)
        :return:
        """
        return self.outre_c.area_circle() - self.inner_c.area_circle()

    def perimeter_ring(self):
        """
        圆环周长 2 * pi * (outre_radius + inner_radius)
        :return:
        """
        return self.outre_c.perimeter() + self.inner_c.perimeter()



def main():
    # outer_r = 10
    # inner_r = 5
    # outer_circle = Circle(outer_r)
    # inner_circle = Circle(inner_r)

    ring = Ring(5, 10)

    ring_area = ring.area_ring()
    ring_perimeter = ring.perimeter_ring()

    print(f"圆环面积: {ring_area}, 周长: {ring_perimeter}")



if __name__ == '__main__':
    main()