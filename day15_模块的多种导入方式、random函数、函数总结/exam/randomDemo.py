# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/17 07:47
# 文件名称: randomDemo.py

"""
random模块常用方法
"""
import random

# random [0.0~1.0)之间的随机数
print(random.random())

# uniform(a, b) 获取 [a, b) 范围内的浮点数
print(random.uniform(10, 20))

# randint(a, b) 获取[a, b] 范围内的整数
print(random.randint(10, 20))

# shuffle(可变数据类型)  把参数中的元素打散，实参必须是可变数据类型
l1 = list(range(10))
random.shuffle(l1)
print(l1)

# sample(x, k) 从x中随机抽取k个元素，返回一个列表
print(random.sample(range(10), 10))

## 变相打散元组
tu = (1, 2, 3, 4, 5)
ret = random.sample(tu, len(tu))
print(ret) # [4, 1, 3, 5, 2]