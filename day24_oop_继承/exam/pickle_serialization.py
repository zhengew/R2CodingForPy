# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 20:35
# 文件名称: pickle_serialization.py

import pickle
from piople_test import People, Student

def serialization_obj(obj):
    """序列化对象"""
    with open('student_info', mode='ab') as f:
        pickle.dump(obj, f)
    f.close()

def deserialization_obj(path):
    """反序列化对象"""
    with open(path, mode='rb') as f:
        while True:
            try:
                obj = pickle.load(f)
                print(obj.__dict__)
            except EOFError:
                break

if __name__ == '__main__':
    alex = Student('alex', 18)
    taibai = Student('taibai', 20)
    serialization_obj(alex)
    serialization_obj(taibai)
    deserialization_obj('student_info')