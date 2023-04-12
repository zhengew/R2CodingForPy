# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 作业4.py
# @datatime: 2023/4/8 16:38

"""
# 作业4
# 写一个自定义模块,里面有你自己实现的mypickle和myjson,我只需要给你传递一个参数 'pickle'还是'json'
"""

import pickle
import json
import sys
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
class MyJson(Serialize):
    def dump(self, obj):
        """json序列化"""
        with open(self.path, mode='at') as f:
            f.write(json.dumps(obj) + "\n")

    def load(self):
        """json反序列化"""
        with open(self.path, mode='rt') as f:
            for line in f:
                yield json.loads(line)


def serialize(method: str, path):
    """归一化设计接口"""
    method = "MyPickle" if method == 'pickle' else "MyJson"
    if hasattr(sys.modules['__main__'], method):
        class_obj = getattr(sys.modules['__main__'], method)(path)
        return class_obj


if __name__ == '__main__':
    class User(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age

    pickle_path = "pickle_path"
    obj = MyPickle(pickle_path)

    alex = User('alex', 20)
    taibai = User('taibai', 21)
    #
    # obj.dump(alex)
    # obj.dump(taibai)
    #
    # ret = [i.__dict__ for i in obj.load()]
    # print(ret)

    obj = serialize('pickle', pickle_path)
    obj.dump(alex)
    ret = obj.load()
    alex = next(ret)
    print(alex.name)
    print(alex.age)
    print(alex.__dict__)

    dic = {'name': 'taibai', 'age': 21}
    json_path = 'json_path'
    obj = serialize('json', json_path)
    obj.dump(dic)
    ret = obj.load()
    dic = next(ret)
    print(dic)