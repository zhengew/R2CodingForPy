# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/18 19:42
# 文件名称: datetime_demo.py

"""
datetime: 日期时间模块
封装了一些和日期时间相关的类

date
time
timedelta
"""
import datetime
# date类
d = datetime.date(2023, 3, 18)
print(d, type(d)) # 2023-03-18 <class 'datetime.date'>

##  获取date对象的各个属性
print(d.year)
print(d.month)
print(d.day)


# time类
t = datetime.time(19, 47, 59)
print(t, type(t)) # 19:47:59 <class 'datetime.time'>

## time类的属性
print(t.hour)
print(t.minute)
print(t.second)

# datetime类
dt = datetime.datetime(2023, 3, 18, 19, 49, 59)
print(dt, type(dt)) # 2023-03-18 19:49:59 <class 'datetime.datetime'>


# datetime中的类主要用于数学计算的
## timedelta：时间的变化量
td = datetime.timedelta(days=1)
print(td) # 1 day, 0:00:00

## 参与时间计算
### 创建时间对象：
### 只能和以下三类进行时间计算: date, datetime, timedelta
d = datetime.date(2010, 10, 10)
res = d - td
print(res) # 2010-10-09

### 时间变化量的计算，是否会产生进位？会进位
t = datetime.datetime(2010, 10, 10, 10, 10, 59)
td = datetime.timedelta(seconds=3)
res = t + td

print(res) # 2010-10-10 10:11:02











