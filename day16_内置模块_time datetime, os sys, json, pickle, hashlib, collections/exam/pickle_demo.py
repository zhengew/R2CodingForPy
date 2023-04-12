# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 15:47
# 文件名称: pickle_demo.py

"""
pickle:
将python中所有的数据类型，转换成字节串，序列化过程
将字节串转换成python中的数据类型，反序列化
"""
import pickle

# json 和 pkckle 的比较
"""
json:
1.不是所有数据类型都可以序列化，结果是字符串
2.不能多次对同一个文件序列化
3.json 数据可以跨语言

pickle:
1.所有的python数据类型都可以序列化，结果是字节串
2.可以多次对同一个文件序列化
3.不能跨语言
"""