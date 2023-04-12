# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/28 07:53
# 文件名称: re_练习题.py

# 1.计算阶乘

def func(n: int):
    """
    计算 1～n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return n
    else:
        return n * func(n-1)

ret = func(5)
print(ret)