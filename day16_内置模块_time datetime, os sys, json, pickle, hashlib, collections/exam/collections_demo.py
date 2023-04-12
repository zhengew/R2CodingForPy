# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 17:48
# 文件名称: collections_demo.py

"""
collections 模块: 容器类

nametuple(): 命名元组
defaultdict(): 默认值字典
Counter(): 计数器
"""

from collections import namedtuple, defaultdict, Counter

# 1.nametuple()
Rectangle = namedtuple('this_is_a_Rectangle_class', ['length', 'wigth'])

## 通过属性访问元组的元素
r = Rectangle(10, 5)
print(r.length)
print(r.wigth)

## 通过索引的方式访问元素
print(r[0])
print(r[1])


# 2.defaultdict
## 创建一个字典的方式
# d = {'name': 'alex', 'age': 10}
# d2 = dict(('name', 'andy'), ('age', 10))
# d3 = {k: v for k, v in [(1, 2), (3, 4)]}

## defaultdict
d = defaultdict(int, name = 'alex', age = 10)
print(d['name'])
print(d['age'])
print(d['addr']) #  ['addr': 0] 也会被添加到字典中
print(d)


## 自定义函数充当工厂函数
def f():
    return 'hello'
d = defaultdict(f, name = 'alex', age = 10)

print(d['addr'])
print(d) # defaultdict(<function f at 0x105fad6c0>, {'name': 'alex', 'age': 10, 'addr': 'hello'})

# 3.Counter(): 计数器

c = Counter('abcefgsaasdef')
print(c) # Counter({'a': 3, 'e': 2, 'f': 2, 's': 2, 'b': 1, 'c': 1, 'g': 1, 'd': 1})
print(c.most_common(3)) # [('a', 3), ('e', 2), ('f', 2)]