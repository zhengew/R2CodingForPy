# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: serialize_control.py
# @datatime: 2023/4/12 21:01

import sys
from maxExam.week.fourth.libary.serialize_utils.my_json import MyJson
from maxExam.week.fourth.libary.serialize_utils.my_pickle import MyPickle

def serialize(kind: str, path: str):
    """归一化设计接口"""
    kind = "MyPickle" if kind == 'pickle' else "MyJson"
    if hasattr(sys.modules['__main__'], kind):
        class_obj = getattr(sys.modules['__main__'], kind)(path)
        return class_obj



if __name__ == '__main__':
    d1 = {'name': 'alex', 'age': 10}
    print(sys.modules)
