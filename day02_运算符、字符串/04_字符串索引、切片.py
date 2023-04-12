# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/514:04
# 文件名称: 06_字符串索引、切片.py

str = "abcdefghigklmn"
print(str[0]) # a
print(str[-1]) # n

print(str[0:5]) # abcde

print(str[::2]) # acegikm

print(str[1::2]) # bdfhgln
print(str[-1::-2]) # nlghfdb
print(str[-2::-2]) # mkigeca