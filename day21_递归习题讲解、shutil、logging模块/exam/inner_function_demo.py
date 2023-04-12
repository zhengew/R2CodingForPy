"""
内置函数
"""
import logging
import random

# sum
# ret = sum([1, 2, 3, 4, 5], 100) # 115
# print(ret)
#
# # min
# # def func(n: int):
# #     return abs(n)
# #
# # ret = min([11, -3, 5, 7, 11, 2, 12], key=func)
# # print(ret)
#
# # eval
# ret = eval('1+2+3')
# print(ret) # 6
#
# # exec 代码流
# msg = """
# for i in range(10):
#     print(i, end=' ')
# """
#
# exec(msg) # 执行代码 0 1 2 3 4 5 6 7 8 9
#
# # hash
# # print(hash([1, 2])) # TypeError: unhashable type: 'list'
# print(hash('abd')) # -6019060912062306342

# help
# import logging
# help(logging)

# callable 判断一个对象是否可调用
# def func(n: int):
#     return divmod(n, 2)
#
# print(callable(func)) # True
# ret = func(10)
# print(ret)

# int

# print(int(3.6))
#
# # float
# print(float(3))
# print(float(3.12))

# print(complex(1, 30))

# bin oct hex
# print(bin(8)) # 0b1000
# print(oct(8)) # 0o10
# print(hex(8)) # 0x8
#
# # divmod
# ret = divmod(10, 3)
# print(ret) # (3, 1)


# bytes
# s1 = 'test123'
# print(bytes(s1, encoding='utf-8'))
# b = s1.encode('utf-8')
# print(b) # b'test123'
# print(b.decode('utf-8'))
# c = bytes(s1, encoding='utf-8')
# print(c)


# ocr
# ret = ord('a')
# print(ret) # 97
#
# ret = chr(97)
# print(ret) # a
#
#
# # repr
# logger = logging.Logger
# print(repr(logger)) # <class 'logging.Logger'>
# s1 = 'erwei'
# print(repr(s1)) # 'erwei'
#
#
# # all
# ret = all([1, 2, 3, True, False, ''])
# print(ret) # False
#
# # any
# ret = any([1, 2, 3, True, False, ''])
# print(ret) # True
#
# # print
# print(1, 2, 3, 4, sep='*', end='\n')
#
# # list
# ret = list('abcdefg')
# print(ret) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# sum
# print(sum([i for i in range(1, 6)], 100)) # 115

# reversed
#
# l1 = [i for i in range(1, 11)]
# ret = reversed(l1)
# print(ret) # <list_reverseiterator object at 0x102a12740>
# print(list(ret)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(l1) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# l1 = [i for i in range(1, 11)]
# l1.reverse()
# print(l1) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# zip
# l1 = [1, 2, 3, 4, 5]
# tu1 = ('alex', 'taibai', 'dechen')
# s2 = 'abce'
# obj = zip(l1, tu1, s2)
# print(obj) # <zip object at 0x1089d8780>
# print(list(obj)) # [(1, 'alex', 'a'), (2, 'taibai', 'b'), (3, 'dechen', 'c')]
#
# dic = dict(zip((1, 2, 3), ('query', 'update', 'delete')))
# print(dic) # {1: 'query', 2: 'update', 3: 'delete'}
#
# dic2 = dict([(1, 'query'), (2, 'update'), (3, 'delete')])
# print(dic2)


# # min
# ret = min([-4, -6, 2, 3, 4], key=lambda x: abs(x))
# print(ret)
#
# def func(n: int):
#     return n % 3
#
# ret = min([10, 3, 5], key=func)
# print(ret) # 3

# max  pass

# sorted 排序
# l1 = [1, 3, 2, 5, 9]
# ret = sorted(l1, reverse=True)
# print(ret) # [9, 5, 3, 2, 1]
# print(l1)
#
# l1.sort(reverse=True)
# print(l1)
#
# scores = [('alex', 98), ('taibai', 80), ('wusir', 85)]
# ret = sorted(scores, key=lambda x: x[1])
# print(ret) # [('taibai', 80), ('wusir', 85), ('alex', 98)]
# ret2 = sorted(scores, key=lambda x: x[1], reverse=True)
# print(ret2) # [('alex', 98), ('wusir', 85), ('taibai', 80)]

# filter
# l1 = [i for i in range(1, 11) if i % 2 == 0]
# print(l1) # [2, 4, 6, 8, 10]
#
# ret = filter(lambda x: x % 2 == 0, range(1, 11))
# print(ret) # <filter object at 0x10f8ac940>
# print(list(ret)) # [2, 4, 6, 8, 10]

# map
l1 = [i**2 for i in range(1, 10)]
print(l1) # [1, 4, 9, 16, 25, 36, 49, 64, 81]

ret = map(lambda x: x**2, range(1, 10))
print(ret) # <map object at 0x109a54910>
print(list(ret)) #[1, 4, 9, 16, 25, 36, 49, 64, 81]
