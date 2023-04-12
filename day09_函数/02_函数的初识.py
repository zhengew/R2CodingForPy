# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/7 20:29
# 文件名称: 02_函数的初识.py

# s1 = "abcdefghijklmnopqrstuvwxyz"
#
# count = 0
# for i in s1:
#     count += 1
#
# print(count)
#
# l1 = [1, 2, 3, 4, 5, 6]
#
# # 函数式编程
# def my_len(string):
#     """
#     计算字符串长度
#     :param string:
#     :return:
#     """
#     count = 0
#     for i in string:
#         count += 1
#     return count
#
# print(my_len(s1))
# print(my_len(l1) == len(l1))

# 函数：以功能(完成一件事)为导向，登录、注册，len,一个函数就是一个功能
# 随调随用
# 减少代码的重复性
# 增强代码的可读性


#
def meet():
    print("打开tantan")
    print("左滑一下")
    print("右滑一下")
    print("悄悄话...")
    print("约...走起...")


"""
结构：def 关键字，定义函数
    meet 函数名:与变量设置相同，具有可描述性
    函数体：缩进，函数中尽量不要出现print
"""

# 函数什么时候执行？
# 当函数遇到函数名()时，才会执行
# meet()

# 函数的返回值
# s1 = "agbddeiigfjg"
# print(len(s1))

# return ：
# 在函数中遇到return直接结束函数
# 将数据返回给函数的执行者和调用者
# return返回多个元素，是以元组的形式返回给函数的执行者

""""
:return总结
    1.在函数中，终止函数
    2。return可以给函数执行者返回值
        return 单个值，返回单个值
        return 多个值,返回元组
"""

