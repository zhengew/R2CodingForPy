# -*- coding: utf-8 -*-
#@author: erwei.zheng
#@file: course.py
#@datatime: 2023/4/12 下午1:13

class Course(object):
    """课程类"""
    def __init__(self, cname, price, period, teacher, begin_time, end_time):
        self.cname = cname              # 课程名
        self.price = price              # 价格
        self.period = period            # 周期
        self.teacher = teacher          # 教师
        self.begin_time = begin_time    # 开班时间
        self.end_time = end_time        # 毕业时间

    def __str__(self):
        """打印对象的属性"""
        return "%s" % self.__dict__


if __name__ == '__main__':
    python = Course('python', 19800.00, '6 month', 'alex', '2023-01-01', '2023-07-31')
    print(python)


