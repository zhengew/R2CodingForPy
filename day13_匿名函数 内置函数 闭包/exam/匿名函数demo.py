# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 17:26
# 文件名称: 匿名函数demo.py

# 匿名函数返回2个数的和
func1 = lambda a, b: a + b
ret = func1(10, 20)
print(func1, type(func1)) # <function <lambda> at 0x10c7400d0> <class 'function'>
print(ret) # 30

# 练习2
func2 = lambda data: (data[0], data[2])
ret = func2([1, 2, 3, 3])
print(ret) # (1, 3)

# 练习3
func3 = lambda a, b: a if a > b else b
ret = func3(10, 5)
print(ret) # 10