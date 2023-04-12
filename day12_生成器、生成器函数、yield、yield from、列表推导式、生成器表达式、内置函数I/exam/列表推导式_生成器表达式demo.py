# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 09:54
# 文件名称: 列表推导式_生成器表达式demo.py

l1 = []
for i in range(1, 11):
    l1.append(i)
print(l1)

# 列表推导式
l2 = [i for i in range(1, 11)]
print(l2)

# 练习：
# (1)10以内所有整数的平方写入列表
l1 = [i**2 for i in range(11)]
print(l1)

# (2)100以内所有的偶数写入列表
l2 = [i for i in range(2, 101, 2)]
print(l2)

# (3)从python1期到python100期写入列表
l3 = [f'python{i}期' for i in range(1, 101)]
# print(l3)

l4 = [i for i in range(1, 31) if i % 3 == 0]
print(l4)

# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
l1 = ['barry', 'ab', 'alex', 'wusir', 'xo']
ret = [i.upper() for i in l1 if len(i) > 3]
print(ret)

print('*******************')
# 含有两个'e'的所有的人名全部大写留下来
names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
         ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]

# 正常实现方式
ret = []
for i in names:
    for name in i:
        if name.count('e') == 2:
            ret.append(name.upper())
print(ret)

# 嵌套列表推导式
ret = [name.upper() for i in names for name in i if name.count('e') == 2]
print(ret)


# 构建一个列表: [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
l1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
l2 = [i for i in range(2, 11)] + list('JQKA')
print(l2)