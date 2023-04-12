# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 1.在类方法中实例化对象，并返回实例对象.py
# @datatime: 2023/4/11 20:22

"""
目标：理解被classmethod装饰的类方法
场景：
1.方法中不需要使用self及绑定方法
2.需要使用类中的成员或类名
"""

import time
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        """类方法中实例化并返回实例实例化对象"""
        struct_t = time.localtime()
        obj = cls(struct_t.tm_year, struct_t.tm_mon, struct_t.tm_mday)
        return obj

if __name__ == '__main__':
    d1 = Date.today()
    print(d1.__dict__) # {'year': 2023, 'month': 4, 'day': 11}

