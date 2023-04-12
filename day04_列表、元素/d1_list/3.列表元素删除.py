# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 15:22
# 文件名称: 3.列表元素删除.py

l1 = list()
l1.extend("abcdefghijk".upper())
print(l1) # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# pop 通过索引删除元素，默认删除最后一个；返回值为被删除的元素
res1 = l1.pop()
print(res1) # K

res2 = l1.pop(0)
print(res2) # A

# remove 删除指定元素值, 无返回值
l2 = l1.copy()
# print(id(l1) == id(l2)) # false
print(l2) # ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
res2 = l2.remove("B")
print(res2) # None
print(l2) # ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# clear 清空列表
l3 = l2.copy()
print(l3) # ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
l3.clear()
print(l3) # []

# del 按索引删除列表元素
l4 = l1.copy() # ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(l4)
del l4[0]
print(l4) # ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# 切片删除
del l4[::2]
print(l4) # ['D', 'F', 'H', 'J']


