# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 21:19
# 文件名称: import_demo1.py

import sys
import os

sys.path.append(os.path.dirname(__file__) + os.sep + 'abc')
print(sys.path)

import a
a.abc()

print(a.name)