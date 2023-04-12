# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/23 07:14
# 文件名称: re_demo.py

import re

"""
findall
search()
"""

# findall 匹配所有
str = 'abcd2023defgegg2022abd'
ret = re.findall('\d+', str)
print(ret) # ['2023', '2022']

ret2 = re.search('\d+1', str)
print(ret2)
# <re.Match object; span=(4, 8), match='2023'> 得到一个对象, 如果未匹配到返回None
print(ret2.group()) # 2023 如果未匹配到，group会抛出异常
# 优化写法
if ret2:
    print(ret2.group())


# 分组
## 预习一个现象 并找到答案 - 分组 ()
# str = 'abcd2023defgegg2122abd'
# ret3 = re.findall('2(\d)\d', str)
# print(ret3) # ['0', '1']
#
# ret4 = re.search('2(\d)(\d)', str)
# if ret4:
#     print(ret4.group())
#     print(ret4.group(1))
#     print(ret4.group(2))
