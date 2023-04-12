# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: json_demo.py
# @datatime: 2023/4/5 19:33

"""
目标: 测试json
"""
import json

l1 = [1, 2, 3]

def serialize(path, obj):
    with open(path, mode='at', encoding='utf-8') as f:
        f.write(json.dumps(obj) + '\n')

def deserialize(path):
     with open(path, mode='rt', encoding='utf-8') as f:
         for i in f:
             yield json.loads(i)


serialize('serialize.txt', l1)


class A:
    def __init__(self, name):
        self.name = name

ret = deserialize('serialize.txt')
print(list(ret))