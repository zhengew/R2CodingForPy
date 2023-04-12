# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 22:06
# 文件名称: 1.utf-8转GBk.py

"""
编码进阶:
str -> byte(unicode -> 非unicode)
gbk <-> utf-8

encode 编码
decode 解码
"""


str_byte_utf8 = "中国".encode("utf-8") # str -> byte
print(str_byte_utf8) # b'\xe4\xb8\xad\xe5\x9b\xbd'

str_unicode_utf8 = str_byte_utf8.decode("utf-8") # utf-8 -> unicode
print(str_unicode_utf8) # 中国

str_byte_gbk = str_unicode_utf8.encode("gbk")
print(str_byte_gbk) # b'\xd6\xd0\xb9\xfa'

str_byte_gbk_unicode = str_byte_gbk.decode("gbk") # unicode -> gbk
print(str_byte_gbk_unicode) # 中国

