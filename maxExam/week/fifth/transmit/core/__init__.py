# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __init__.py
# @datatime: 2023/4/26 下午3:46

from maxExam.week.fifth.transmit.lib.serializeUtils import SerializeUtils

d1 = {'name': 'alex', 'age': 18}

d2 = SerializeUtils.json_dumps(d1)
print(d2)

print(SerializeUtils.__dict__)