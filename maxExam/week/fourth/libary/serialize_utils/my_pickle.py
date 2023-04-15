# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: my_pickle.py
# @datatime: 2023/4/13 19:54
import os
import pickle
from maxExam.week.fourth.libary.serialize_utils.serialize import Serialize
class MyPickle(Serialize):
    def dump(self, obj):
        """序列化对象"""
        with open(self.path, mode='ab') as f:
            pickle.dump(obj, f)
    def load(self):
        """
        反序列化对象
        :return: 生成器对象
        """
        with open(self.path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    return
