# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: my_json.py
# @datatime: 2023/4/13 19:56

import json
from maxExam.week.fourth.libary.serialize_utils.serialize import Serialize
class MyJson(Serialize):
    def dump(self, obj):
        """json序列化"""
        with open(self.path, mode='wt', encoding='utf-8') as f:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")

    def load(self):
        """json反序列化"""
        with open(self.path, mode='rt', encoding='utf-8') as f:
            for line in f:
                yield json.loads(line)