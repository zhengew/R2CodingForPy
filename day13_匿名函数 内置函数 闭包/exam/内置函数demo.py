# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 17:45
# 文件名称: 内置函数demo.py

# print(round(3.345, 2)) # 3.35
#
# print(pow(2, 3, 3)) # 2
#
# command = dict(zip([1, 2, 3], ['query', 'update', 'delete']))
# print(command)
#
# # 以绝对值的方式求最小值
# l1 = [33, 2, 54, 7, -1, -9, -2]
# def func(data):
#     return min([abs(i) for i in data])
#
#
# print(func(l1))
#
# ret = lambda data: min(abs(i) for i in data)
#
# print(ret(l1))
#
# ret = min(l1, key=abs)
# print(ret)


# 练习:求出值最小的键值对
#
# dic = {'a': 3, 'b': 2, 'c': 1}
# key = min(dic) # min默认是按照字典的键比较大小
# print(key) # a
#
# def func(a):
#     return dic[a]
# print(min(dic, key=func))
#
# print(min(dic, key=lambda args: dic[args]))

# 年龄最小的元组
# l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
#
# print(min(l2, key=lambda args: args[1])) # ('太白', 18)
# print(min(l2, key=lambda args: args[1])[0]) # 太白
# print(min(l2, key=lambda args: args[1])[1]) # 18

ret = map(lambda x : x ** 2, range(1, 6))
print(ret) # <map object at 0x1064da680>
print(list(ret)) # [1, 4, 9, 16, 25]