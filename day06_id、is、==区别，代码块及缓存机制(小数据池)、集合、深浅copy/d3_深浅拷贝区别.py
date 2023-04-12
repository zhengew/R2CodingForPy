# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 21:45
# 文件名称: d3_深浅拷贝区别.py

"""
浅拷贝：copy()
在栈区重新开辟空间保存内存地址，内存地址还是原拷贝对象的内存地址

深拷贝：copy.deepcopy()
在栈区重新开辟空间保存内存地址，对于不变数据还沿用原内存地址，对于可变的数据，则在堆内存中重新开辟空间复制一份
"""
import copy

list1 = [1, 2, 3, {4, 5}]
# 浅拷贝
list2 = list1.copy()

print(list2) # [1, 2, 3, {4, 5}]
list2[-1].add(6) # 修改 浅拷贝中的元素，被拷贝的列表元素也跟着变
print(list2) # [1, 2, 3, {4, 5, 6}]
print(list1) # [1, 2, 3, {4, 5, 6}]
print(list2 == list1) # True

# 深拷贝
print("深拷贝".center(50, "*"))
list3 = copy.deepcopy(list1)
print(list3) # [1, 2, 3, {4, 5, 6}]

list3[-1].add(7)
print(list1) # [1, 2, 3, {4, 5, 6}]
print(list3) # [1, 2, 3, {4, 5, 6, 7}]
print(list3 == list1) # False
