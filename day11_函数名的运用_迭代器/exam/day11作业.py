# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 17:48
# 文件名称: day11作业.py
import copy

# 1. 写代码完成99乘法表.(**选做题，面试题**)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={i*j}', end="\t")
#     print()

# 2.写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(**选做题**)
# 例如：[(‘红心’，2),(‘草花’，2), …(‘黑桃’，‘A’)]
# def getCards():
#     color = ['♣️', '♠️', '♥️', '♦️']
#     number = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
#     cards = ['大🃏', '小🃏', ]
#
#     for i in number:
#         for j in color:
#             cards.append((j, i))
#     return cards
#
#
# cards = getCards()
# print(cards)

# 3.写函数，传入一个参数n，返回n的阶乘,例如:cal(7) 计算7*6*5*4*3*2*1

# def factorial(nunber: int):
#     result = 1
#     for i in range(nunber, 1, -2):
#         print(f'{i}*{i-1}')
#     return result
#
# print(factorial(7))

# 4.写函数，传入n个数，返回字典{‘max’:最大值,’min’:最小值}
# 例如:min_max(2,5,7,8,4) 返回:{‘max’:8,’min’:2}(此题用到max(),min()内置函数)

# def min_max(*args):
#     # return {'max': max(args), 'min': min(args)}
#     # 冒泡排序（正序）
#     args = list(args)
#     for i in range(len(args) - 1):
#         for j in range(len(args) - i - 1):
#             if args[j] > args[j+1]:
#                 temp = args[j+1]
#                 args[j+1] = args[j]
#                 args[j] = temp
#
#     return {'max': args[-1], 'min': args[0]}
#     """
#     _max: 2
#          loop1: 4次
#          loop2: 3次
#          loop3: 2次
#          loop4: 1次
#
#     """
#
# print(min_max(2, 5, 7, 8, 4)) # {'max': 8, 'min': 2}


# 5.写代码：用while循环模拟for内部的循环机制（**面试题**）

# data = [1, 2, 3, 4, 5 ,6]
# while True:
#     data = data.__iter__()
#     try:
#         print(data.__next__())
#     except StopIteration:
#         break


# 6. 如何判断该对象是否是可迭代对象或者迭代器？
# obj1 = 'strabcefeg'
# result = True if '__iter__' in obj1.__dir__() else False
# print(obj1+f'是可迭代对象:{result}')
#
# obj2 = copy.deepcopy(obj1).__iter__()
# result2 = True if ('__iter__' in obj2.__dir__() and '__next__' in obj2.__dir__()) else False
# print(f'obj2是迭代器: {result2}')

# 7.用你的理解解释一下什么是可迭代对象，什么是迭代器。
#
#    可迭代对象就是一个可以重复取值的实实在在的东西。
#
#    迭代器是一个可以迭代取值的工具。


# 8. 看代码写结果
# (1)
# def func1():
# 	print('in func1')
# def func2():
# 	print('in func2')
# ret = func1
# ret()
# ret1 = func2
# ret1()
# ret2 = ret
# ret3 = ret2
# ret2()
# ret3()

'''
in func1
in func2
in func1
in func1
'''

# (2)
# def func1():
# 	print('in func1')
# def func2():
# 	print('in func2')
# def func3(x,y):
# 	x()
# 	print('in func3')
# 	y()
# print(111)
# func3(func2,func1)
# print(222)

'''
111
in func2
in func3
in func1
222
'''

# (3)
# def func1():
# 	print('in func1')
# def func2(x):
# 	print('in func2')
# 	return x
# def func3(y):
# 	print('in func3')
# 	return y
# ret = func2(func1)
# ret()
# ret2 = func3(func2)
# ret3 = ret2(func1)
# ret3()

'''
in func2
in func1
in func3
in func2
in func1
'''

# (4)
# def func(arg):
#     return arg.replace('苍老师', '***')
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
# run()

'''
Alex的女朋友***和大家都是好朋友
'''

# (5)
# def func(arg):
#     return arg.replace('苍老师', '***')
#
# def run():
#     msg = "Alex的女朋友苍老师和大家都是好朋友"
#     result = func(msg)
#     print(result)
#
# data = run()
# print(data)

'''
Alex的女朋友***和大家都是好朋友
None
'''

# (6) ***
DATA_LIST = []

def func(arg):
    return DATA_LIST.insert(0, arg)

data = func('绕不死你')
print(data)
print(DATA_LIST)

'''
[]
['绕不死你', ]
'''

# (7)
# def func():
#     print('你好呀')
#     return '好你妹呀'
#
#
# func_list = [func, func, func]
#
# for item in func_list:
#     val = item()
#     print(val)

'''
你好呀
好你妹呀
你好呀
好你妹呀
你好呀
好你妹呀
'''

# (8)
# def func():
#     print('你好呀')
#     return '好你妹呀'
# func_list = [func, func, func]
# for i in range(len(func_list)):
#     val = func_list[i]()
#     print(val)

'''
你好呀
好你妹呀
你好呀
好你妹呀
你好呀
好你妹呀
'''

# (9)
# def func():
#     return '烧饼'
# def bar():
#     return '豆饼'
# def base(a1, a2):
#     return a1() + a2()
# result = base(func, bar)
# print(result)

'''
烧饼豆饼
'''

# （10）
for item in range(10):
    print(item)

print(item) # 循环遍历结束后，item最终等于 9

'''
0～9
9
'''

# （11）
# def func():
#     for item in range(10):
#         pass
#     print(item)
# func()

'''
9
'''

print('*******************')
# （12）
item1 = '老男孩'
def func():
    item1 = 'alex'
    def inner():
        print(item1)
    for item1 in range(10):
        pass
    inner()
func()

'''
9
'''

print('***************')

# （13）
# l1 = []
# def func(args):
#     l1.append(args)
#     return l1
# print(func(1))
# print(func(2))
# print(func(3))

'''
[1,]
[1, 2, ]
[1, 2, 3, ]

'''

# (14)

# name = '太白'
# def func():
#     global name
#     name = '男神'
# print(name)
# func()
# print(name)

'''
太白
男神

'''

# （15）
# name = '太白'
# def func():
#     print(name)
# func()

'''
太白
'''

# （16）
# name = '太白'
# def func():
#     print(name)
#     name = 'alex' # 优先在局部找变量，不能先使用后申明
# func()

# （17）
# def func():
#     count = 1
#     def inner():
#         nonlocal count
#         count += 1
#         print(count)
#     print(count)
#     inner()
#     print(count)
# func()

'''
1
2
2
'''

# （18）
# def extendList(val,list=[]):
# 	list.append(val)
# 	return list
#
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
#
# print('list1=%s'%list1) # [10, 'a', ]
# print('list2=%s'%list2) # [123, ]
# print('list3=%s'%list3) # [10, 'a', ]


# (19)
# def extendList(val,list=[]):
# 	list.append(val)
# 	return list
# print('list1=%s'% extendList(10)) # [10, ]
# print('list2=%s'% extendList(123,[])) # [123, ]
# print('list3=%s'% extendList('a')) # [10, 'a']