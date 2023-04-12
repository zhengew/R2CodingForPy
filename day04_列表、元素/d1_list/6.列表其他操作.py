# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 15:46
# 文件名称: 6.列表其他操作.py

l1 = [1, 1, 2, 2, 2, 3, 3, 3]
# count 统计某个元素在列表中出现的次数
print(l1.count(1)) # 2
print(l1.count(3)) # 3

# index  找出某个元素在列表中第一次匹配的索引位置
print(l1.index(2)) # 2

# sort 列表排序，默认正序，参数reverse=True时，倒序排序
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

# reverse 列表倒序排序
l1.reverse()
print(l1)

# 列表相加
l2 = l1.copy()
l3 = l1 + l2
print(l3) # [3, 3, 3, 2, 2, 2, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1]

# 列表相乘
l4 = l1 * 3
print(l4)

l5 = [1, 2, 3, "A"]
l6 = [4, 5, 6,]
l7 = l5 + l6
print(l7)


# 列表嵌套
l8 = ["school", ["class1", "class2", "class3"]]
# print(l8[1][0])

for i in range(len(l8)):
    if type(l8[i]) != list:
        print(l8[i])
    else:
        for j in range(len(l8[i])):
            print(l8[i][j])

# 列表遍历
l9 = [1, 2, 3]
for i in l9:
    print(i)

