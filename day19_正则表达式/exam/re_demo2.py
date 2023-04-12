# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/23 19:27
# 文件名称: re_demo2.py

import re

exp = "2-3*(5+6)"

regx = "(\d+)[+](\d+)"

ret = re.search(regx, exp)
print(ret)

print(int(ret.group(1)) + int(ret.group(2)))


regx = "1(\d)(\d)"
ret = re.findall(regx, '123143')
print(ret) # [('2', '3'), ('4', '3')]

regx2 = "1(\d)(?:\d)"
ret = re.findall(regx2, "123143")
print(ret) # ['2', '4']