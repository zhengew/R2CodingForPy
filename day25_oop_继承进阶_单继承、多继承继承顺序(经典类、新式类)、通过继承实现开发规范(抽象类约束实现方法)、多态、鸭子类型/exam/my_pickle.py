# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/3 20:44
# 文件名称: my_pickle.py
import pickle

class MyPickle(object):

    def __init__(self, path: str):
        self.path = path

    def my_dump(self, obj):
        """序列化"""
        with open(self.path, mode='ab') as f:
            pickle.dump(obj, f)

    def my_load(self):
        """反序列化"""
        with open(self.path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f) # 生成器
                except EOFError:
                    return

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age



if __name__ == '__main__':
    obj = MyPickle('userinfo')

    alex = People('alex', 12)
    wusir = People('wusir', 20)

    obj.my_dump(alex)
    obj.my_dump(wusir)

    for i in obj.my_load():
        print(i.__dict__)