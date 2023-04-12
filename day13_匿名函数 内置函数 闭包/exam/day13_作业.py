# # -*- coding:utf-8 -*-
# # 开发人员: erwei.zheng
# # 开发时间: 2023/3/12 22:18
# # 文件名称: day13_作业.py
#
# ## day13 作业(张珵)
#
# 1.
# 看代码分析结果
#
# ```
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda: i)
#
# v1 = func_list[0]()
# v2 = func_list[5]()
# print(v1, v2)
#
# 执行结果：
# 9
# 9
# 注：func_list = [lambda: i, lambda: i...] = [i, i...]，函数执行时i = 9
# ```
#
# 1.
# 看代码分析结果
#
# ```
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# v1 = func_list[0](2)
# v2 = func_list[5](1)
# print(v1, v2)
#
# 执行结果：
# 11
# 10
# 注：与上题同理
# ```
#
# 1.
# 看代码分析结果
#
# ```
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for i in range(0, len(func_list)):
#     result = func_list[i](i)
#     print(result)
#
# 执行结果：
# 0, 2, 4..., 16, 18
# 注：函数执行时，i分别等于0, 1, 2..
# .9
#
# 类比另一题：
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for j in range(0, len(func_list)):
#     result = func_list[j](j)
#     print(result)
#
# 执行结果：
# 9, 10, 11..
# .17, 18
# 注：函数执行时，i = 9
# ```
#
# 1.
# 看代码写结果（面试题）：
#
# ```
#
#
# def func(name):
#     v = lambda x: x + name
#     return v
#
#
# v1 = func('太白')
# v2 = func('alex')
# v3 = v1('银角')
# v4 = v2('金角')
# print(v1, v2, v3, v4)
#
# 执行结果：
# < function
# func. < locals >.< lambda
#     > at 0x000000000246BBF8 > < function func.< locals >.< lambda > at 0x000000000246BC80 > 银角太白 金角alex
#     注：
#     v1= lambda x: x + '太白'
# v2 = lambda x: x + 'alex'
# v3 = '银角太白'
# v4 = '金角alex'
# ```
#
# 1.
# 看代码写结果【面试题】
#
# ```
# result = []
# for i in range(10):  # i=0,1,2...9
#     func = lambda: i
#     result.append(func)  # result=[lambda :i,lambda: i...]一共十个元素
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
#
# 执行结果：
# 9
# [第1个函数地址、第2个函数地址...第10个函数地址]
# 9
# 9
# ```
#
# 1.
# 看代码分析结果【面试题】
#
# ```
#
#
# def func(num):
#     def inner():
#         print(num)
#
#     return inner
#
#
# result = []
# for i in range(10):
#     f = func(i)
#     result.append(f)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)
#
# 执行结果：
# 9
# [第1个inner函数地址、第2个inner函数地址……第10个inner函数地址]
# 0
# 9
# None
# None
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# i = 0
# f = func(0) = inner
# result = [inner]
#
# i = 1
# f = func(1) = inner
# result = [inner, inner]
#
# ...
#
# i = 9
# f = func(9) = inner
# result = [inner, inner...inner]（共10个）
#
# print(i) = 9
# result = [inner, inner...inner]（共10个）
# inner函数没有返回值，所以v1, v2都是None
# 【问】为什么v1是0？
# 【答】由于i是通过func的参数的形式传到num的，不可变类型对象传参只传值，因此传的时候是多少就是多少，不会随着i的更新而更新
# ```
#
# 1.
# 看代码写结果【新浪微博面试题】
#
# ```
#
#
# def func():
#     for num in range(10):
#         pass
#     v4 = [lambda: num + 10, lambda: num + 100, lambda: num + 100, ]
#     result1 = v4[1]()
#     result2 = v4[2]()
#     print(result1, result2)
#
#
# func()
#
# 执行结果：
# 109
# 109
# ```
#
# 2.
# 请编写一个函数实现将IP地址转换成一个整数。【面试题，较难, 可以先做其他题】
#
# ```
# 如
# 10.3
# .9
# .12
# 转换规则为二进制：
# 10
# 00001010
# 3
# 00000011
# 9
# 00001001
# 12
# 00001100
# 再将以上二进制拼接起来计算十进制结果：00001010
# 00000011
# 00001001
# 00001100 = ？
# ```
#
# 方法一：张珵——基于二进制数字与十进制数字的转化原理
#
# ```
#
#
# def func(ip10_str):
#     def bin2int(x):
#         y = str(x)
#         power = len(y) - 1
#         s = 0
#         for i in y:
#             s = s + int(i) * (2 ** power)
#             power -= 1
#         return s
#
#     ip10_str_list = ip10_str.split('.')  # ['182','64','63','222']
#     ip10_int_list = [int(x.strip()) for x in ip10_str_list]  # [182,64,63,222]
#     ip2_str_list = ['0' * (8 - len(bin(x)[2:])) + bin(x)[2:] for x in ip10_int_list]
#     # ['10110110', '01000000', '00111111', '11011110']
#     num2_str = ''.join(ip2_str_list)  # '10110110010000000011111111011110'
#     num2_int = int(num2_str)  # 10110110010000000011111111011110
#     return (bin2int(num2_int))
#
#
# print(func('182.64.63.222'))
#
# 执行结果：3057663966
# ```
#
# 方法二：纳钦——基于
# `int(字符串, base=0)`
#
# ```
# ip = '182.64.63.222'
# l1 = ip.split('.')
# b_count = 0
# l2 = []
# b = '0b'
# for i in l1:
#     a = bin(int(i))
#     length = len(a) - 2
#     b += '0' * (8 - length) + a[2:]
# print(b, type(b))
# print(int(b, base=0))
#
# 执行结果：
# 0b10110110010000000011111111011110 <
#
#
# class 'str'>
#
#
# 3057663966
# ```
#
