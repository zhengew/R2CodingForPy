# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/7 21:29
# 文件名称: 03_函数的传参.py

"""
形参：
    位置参数，**args, 默认值参数，**kwargs
实参：
    位置参数，关键字参数
"""

# 实参角度
# 1.位置参数，从左到右一一对应

# def meet(name, age, sex):
#     print("姓名: %s, 年龄: %d, 性别: %s" % (name, age, sex))
#
# meet("lucy", 19, "女")
#
# # 写一个函数，只接收2个int参数，将较大的数据返回
#
# def maxNum(n1: int, n2: int):
#     return n1 if n1 > n2 else n2
#
#
# print(maxNum(2, 1))
# print(maxNum(1, 2))
#
# # 三元运算符：简单的 if else
# a, b = 10, 20
# res = a if a > b else b
# print(res)
#
# print(max(1, 2))

# 2.关键字参数
# 一一对应
# def meet(name,age, sex, hight, weight):
#     print("姓名:%s, 年龄:%d, 性别:%s, 身高:%d, 体重:%d" %(name, age, sex, hight, weight))
#
# meet(name="lucy", sex="女", age=18, hight=190, weight=160)

# 练习：传入2个字符串参数，将2个参数拼接完成后形成的结果返回

# def addStr(str1: str, str2: str):
#     return str1 + str2
#
#
# print(addStr(str1="你好", str2="中国"))

'''
总结：实参角度
1.位置参数，按照顺序，一一对应
2.关键字参数，一一对应
3.混合参数：位置参数一定要在关键字参数前面
'''

"""
形参角度：
1.位置参数
2.默认值参数
3.**args 魔法位置参数
4.仅限关键字参数
5.**kwargs
"""

def func(data: list):
    return data[:2]

print(func([1, 2]))
print(func([3, 4, 5]))