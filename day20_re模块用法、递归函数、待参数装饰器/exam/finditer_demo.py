# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/24 20:50
# 文件名称: finditer_demo.py
import re

ret = re.compile('\d+')
res = ret.finditer('abdefg123agckki;l;j456as789')
print(res) # <callable_iterator object at 0x10896d840>
for i in res:
    print(i.group())
'''
<callable_iterator object at 0x10cee9840>
123
456
789
'''
