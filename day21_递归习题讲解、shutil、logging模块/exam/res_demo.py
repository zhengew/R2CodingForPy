# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/26 16:31
# 文件名称: res_demo.py
import os

path = '/Users/erwei.zheng/PycharmProjects/R2CodingForPython/day21_递归习题讲解、shutil、logging模块/outer'

# 打印指令文件路径下的所有文件名
# def show_file(path: str):
#     """
#     :param path:
#     :return:
#     """
#     files = os.listdir(path)
#     for name in files:
#         abs_path = os.path.join(path, name)
#         if os.path.isfile(abs_path):
#             print(name)
#         elif os.path.isdir(abs_path):
#             show_file(abs_path)
#
# show_file(path)

# 2.计算一个文件夹内所有文件的大小
# def get_file_size(path: str):
#     """
#     :param path:
#     :return:
#     """
#     files = os.listdir(path)
#     sum = 0
#     for name in files:
#         abs_path = os.path.join(path, name)
#         if os.path.isfile(abs_path):
#             sum += os.path.getsize(abs_path)
#             print(sum)
#         elif os.path.isdir(abs_path):
#             sum += get_file_size(abs_path)
#     return sum
# sum = get_file_size(path)
# print(sum)

# 斐波那契数列 生成器
def feib(n: int):
    if n == 1:
        yield 1
    else:
        yield from (1, 1)
    a, b = 1, 1
    while n > 2:
        a, b = b, a + b
        yield b
        n -= 1

for i in feib(100):
    print(i)
