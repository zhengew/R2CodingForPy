# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 20:46
# 文件名称: sysDemo.py
import os
import sys

# print(sys.path)

print(os.path.dirname(__file__))

sys.path.append(os.path.dirname(__file__) + os.sep + 'abc')
print(sys.path)
