# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/27 22:11
# 文件名称: hashlib_demo.py


import hashlib

m = hashlib.md5('test'.encode('utf-8')) # 盐，参数字节类型
m.update('1234565'.encode('utf-8'))
ret = m.hexdigest()

print(ret) # ec8f3408f459b1792eea0e25045deafd