# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: my_json.py
# @datatime: 2023/4/13 19:56

import json
from maxExam.week.fourth.libary.serialize_utils.serialize import Serialize
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