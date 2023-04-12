# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 20:47
# 文件名称: 1.集合的增删改查.py

"""
目标：集合定义及常用方法

1.集合定义
集合是无序的，不重复的数据集合，集合的元素是可哈希的(不可变类型),但是集合本身是不可哈希的，所以集合不能所字典的key
2.集合主要用处：
- 去重，把一个列表变成集合，就自动去重
- 关系测试，测试两组数据之间的交并差
"""

# 1.集合的创建
# 空集合
set1 = set()
print(set1, type(set1)) # set() <class 'set'>

# 静态初始化集合
set2 = {1, 2, 3, 3}
print(type(set2))  # <class 'set'>
print(set2) # {1, 2, 3} 自动去重

# 2.集合的增
# add()
set3 = set()
set3.add(1)
print(set3) # {1, }

# update {1, 2, 3, 4, 5}
set3.update([2, 3 ,4, 5])
print(set3)

# 3.集合的删
set4 = set3.copy()
print(set4) # {1, 2, 3, 4, 5}
# remove(value) # 删除元素
set4.remove(5)
print(set4)

# pop() 随机删除
set4.pop()
print(set4)

# clear() 清空
set4.clear()
print(set4) # set()

# 删除集合
del set4
# print(set4) # NameError: name 'set4' is not defined. Did you mean: 'set1'?
