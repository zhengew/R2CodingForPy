# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/25 14:52
# 文件名称: day20_递归相关练习题.py
import os


# 递归相关
# 1.计算阶乘 100! = 100*99*98*97*96....*1

# 循环方式

# def loop_func(n: int):
#     sum = 1
#     for i in range(1, n+1, 2):
#         sum *= i * (i+1)
#     return sum
#
# ret = loop_func(100)
# print(ret) # 169150
#
# # 递归实现
# def recursion_func(n: int):
#     if n == 1:
#         return n
#     else:
#         return n * recursion_func(n-1)
#
#
# ret = recursion_func(100)
# print(ret)

# ------------- 递归阶乘推理
# def recursion_func(7):
#     if 7 == 1:
#         return n
#     else:
#         return 7 * recursion_func(6) # 6 * 4 * 3 * 2 * 1 -> 7 * 6 * 4 * 3 * 2 * 1 这是最外层了，结果返回给函数的调用者
#
#
# def recursion_func(6):
#     if 6 == 1:
#         return n
#     else:
#         return 6 * recursion_func(5) # 4 * 3 * 2 * 1 -> 6 * 4 * 3 * 2 * 1
#
# def recursion_func(5):
#     if 5 == 1:
#         return n
#     else:
#         return 5 * recursion_func(4) # 4 * 3 * 2 * 1 -> 5 * 4 * 3 * 2 * 1
#
# def recursion_func(4):
#     if 4 == 1:
#         return n
#     else:
#         return 4* recursion_func(3) # 3 * 2 * 1 -> 4 * 3 * 2 * 1
#
#
# def recursion_func(3):
#     if 3 == 1:
#         return n
#     else:
#         return 3 * recursion_func(2) # 2 * 1 -> 3 * 2 * 1
#
# def recursion_func(2):
#     if 2 == 1:
#         return n
#     else:
#         return 2 * recursion_func(1) # 2 * 1
#
#
# def recursion_func(1):
#     if 1 == 1:
#         return n -> 此时 n = 1, n return 给了上层函数的  recursion_func(1)
#     else:
#         return 2 * recursion_func(1)

# 2.os模块:查看一个文件夹下的所有文件,这个文件夹下面还有文件夹,不能用walk【要求：掌握】
# path = os.path.join(os.path.dirname(__file__), 'a')
# res = os.listdir(path)
# print(res)
# def show_file(path: str):
#     files = os.listdir(path)
#     for name in files:
#         abs_path = os.path.join(path, name)
#         if os.path.isfile(abs_path):
#             print(name)
#         else:
#             show_file(abs_path)
#
# show_file('a')

# 3.os模块:计算一个文件夹下所有文件的大小.这个文件夹下面还有文件夹,不能用walk【要求：看懂，并知道实现方法】

# def get_dir_file_size(path: str):
#     files = os.listdir(path)
#     sum = 0
#     for name in files:
#         abs_path = os.path.join(path, name)
#         if os.path.isfile(abs_path):
#             print(os.path.getsize(abs_path), abs_path)
#             sum += os.path.getsize(abs_path)
#             print(f"-->{sum}")
#         else:
#             sum += get_dir_file_size(abs_path)
#     return sum
#
# ret = get_dir_file_size('a')
#
# print(f"-->ret: {ret}")


# 4.计算斐波那契数列（要求：会写）
    # 找第100个数
    # 1 1 2 3 5...

# 循环方式
def get_feibo(n: int):
    a, b = 1, 1
    while n > 2:
        a, b = b, a+b
        n -= 1
    return b

ret = get_feibo(6)
print(ret)

# 递归方式
def feibo(n, a=1, b=1):
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a+b
        return feibo(n-1, a, b)


print(feibo(6))


