# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 封装pickle类.py
# @datatime: 2023/4/5 16:53

"""
目标: 封装pickle类
实现多次写入对象，多次读取对象
"""
import pickle
class MyPickle(object):
    def __init__(self, path):
        self.path = path # 序列化对象存储路径
    def dump(self, obj):
        """序列化对象"""
        with open(self.path, mode='ab') as f:
            pickle.dump(obj, f)
    def load(self):
        """反序列化对象"""
        with open(self.path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f) # 生成器
                except EOFError:
                    break


if __name__ == '__main__':
    pass