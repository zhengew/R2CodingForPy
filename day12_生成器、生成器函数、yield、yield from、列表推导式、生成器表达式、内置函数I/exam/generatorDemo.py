# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 22:43
# 文件名称: generatorDemo.py

# def func():
#     for i in range(1, 20001):
#         yield "包子" + str(i)
#
#
# ret = func()
# print(ret) # <generator object func at 0x108a43ed0>
#
# for i in range(10):
#     print(ret.__next__())



# def generatorDemo2(a, b):
#     print('这是一个生成器函数demo')
#     yield a + b
#     yield a - b
#     yield a * b
#     yield a / b
#
# ret = generatorDemo2(10, 5)
# try:
#     print(ret.__next__())
#     print(ret.__next__())
#     print(ret.__next__())
#     print(ret.__next__())
#     print(ret.__next__()) # StopIteration
# except StopIteration:
#     print("StopIteration")
#     pass


## 吃包子案例
# def gen_buns(number: int):
#     l1 = []
#     for i in range(number):
#         l1.append(f'{i+1}号包子')
#
#     return l1
#
# ret = gen_buns(2000)
# print(ret)

# 生成器函数吃包子案例
# def gen_buns2(number: int):
#     for i in range(number):
#         yield f'{i+1}号包子'
#
# ret = gen_buns2(2000)
# print(ret) # <generator object gen_buns2 at 0x104e21690>
#
# for i in range(200):
#     print(ret.__next__())
#
# for i in range(200):
#     print(ret.__next__())


# yield from

# def gen_demo(data:list):
#     yield from data
#
# ret = gen_demo([1, 2, 3, 4])
# for i in range(4):
#     print(ret.__next__())

