# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 21:24
# 文件名称: demo2.py

"""
把列表中姓周的删掉
"""

l1 = ["周星驰", "周芷若", "草原三剑客", "王宝强", "贾乃亮", "陈羽凡", "周星星"]

for i in range(len(l1)-1, -1, -1):
    if l1[i].strip()[0] == "周":
        l1.pop(i)

print(l1)
