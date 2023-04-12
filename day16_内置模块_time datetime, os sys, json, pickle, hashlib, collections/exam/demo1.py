# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/18 20:05
# 文件名称: demo1.py

"""
练习：计算某一年的二月份有多少天
"""
import datetime


# 普通算法根据年份是否时闰年：是 29天，否 28天

# 用 datetime默亏啊
# 首先创建出指定年份的3月1号，然后让它往前走一天

year = int(input('请输入年份:'))
d = datetime.date(year, 3, 1)
print(d)
td = datetime.timedelta(days=1)
res = d - td # res 的数据类型以前面为准，d 的数据类型是 datetime.date类
print(res.day)
