# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 15:59
# 文件名称: 1.tuple.py

"""
tuple 元组：不可变数据类型

"""
# 1.创建空元素
t1 = ()
print(type(t1)) # <class 'tuple'>

# 2.元素在定义后只能查询，不能增删改
# t1[0] = "abc" # TypeError: 'tuple' object does not support item assignment

# 3.元组的切片查询
t2 = (1, 2, 3, 4)
print(t2[1:]) # (2, 3, 4)

# 4.元组的遍历
for i in t2:
    print(i)


# 5. index 通过元素找索引，找到第一个就返回索引位置，找不到则报错
t3 = t2
print(t3) # (1, 2, 3, 4)
print(t3.index(2)) # index = 1
# print(t3.index(5)) # ValueError: tuple.index(x): x not in tuple

# 6.count 统计某个元素在元组中出现的次数
print(t3.count(2)) # 1

# 7.len 元组长度
print(len(t3)) # 4
