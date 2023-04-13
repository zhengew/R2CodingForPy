# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: serialize.py
# @datatime: 2023/4/13 19:54

from abc import ABCMeta, abstractmethod
class Serialize(object, metaclass=ABCMeta):
    def __init__(self, path):
        self.path = path
    @abstractmethod
    def dump(self):
        """子类重写序列化方法"""
        pass
    @abstractmethod
    def load(self):
        """子类重写反序列化方法"""
        pass