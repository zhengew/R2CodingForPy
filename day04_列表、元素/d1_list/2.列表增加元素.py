# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 14:55
# 文件名称: 2.列表增加元素.py

l1 = list()

# append 给列表的最后一个索引追加元素
l1.append(1) # [1,]
print(l1)
l1.append(2) # [1, 2, ]
print(l1)

# insert 给指定索引位置插入元素
l1.insert(2, 3)
print(l1)

l1.insert(len(l1), 4)
print(l1)

# extend 迭代追加元素
l2 = [1, 2, 3]
l2.extend("456")
print(l2)