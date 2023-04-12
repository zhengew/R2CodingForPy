# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 鸭子类型.py
# @datatime: 2023/4/5 13:09

"""
目标: 理解鸭子类型
在类中实现了某些特定的方法，那么这个类型就是鸭子类型
例如：只要实现了__iter__和__next__方法的类，就是迭代器类
"""
class list:
    def __init__(self, *args):
        self.l = list(*args)
        self.length = len(self.l)
    def append(self, num):
        self.l.append(num)
        self.length += 1
    def __len__(self): # 在调用len方法时，实际就是调用类中的__list__方法
        return self.length
def len(obj): # 相对与len方法：指的是这个这个形参obj类是否在内部实现了__len__方法，如果实现了就是鸭子类型
    return obj.__len__()

if __name__ == '__main__':
    l = [1, 2, 3] # 实例化一个list类型对象l
    l.append(4)
    length = len(l)
    print(length) # 4
