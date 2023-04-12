# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 18:22
# 文件名称: 日期相关练习.py

"""
time
datetime 日期运算(timedelta)
"""
import time
import datetime
#
# # time 模块
# # 1.时间戳
# t = time.time() # 截止到1970.1.1 00:00:00，经过了多少秒(java中是毫秒)
# print(t) # 1679221526.210119
#
# # 2.结构化时间
# # a, GMT时间
# ret = time.gmtime()
# print(ret)
# '''
# time.struct_time(tm_year=2023, tm_mon=3, tm_mday=19, tm_hour=10, tm_min=26, tm_sec=45, tm_wday=6, tm_yday=78, tm_isdst=0)
# '''
#
# # b,本时区时间
# ret = time.localtime()
# print(ret)
# '''
# time.struct_time(tm_year=2023, tm_mon=3, tm_mday=19, tm_hour=18, tm_min=28, tm_sec=8, tm_wday=6, tm_yday=78, tm_isdst=0)
# '''
#
# # 3.时间和字符串的相互转换
# ## a, 时间对象转换成时间字符串
# sf = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# print(sf) # 2023-03-19 18:31:36
#
# ## b, 时间字符串转成时间对象
# sp = time.strptime(sf, '%Y-%m-%d %H:%M:%S')
# print(sp)
# '''
# time.struct_time(tm_year=2023, tm_mon=3, tm_mday=19, tm_hour=18, tm_min=36, tm_sec=56, tm_wday=6, tm_yday=78, tm_isdst=-1)
# '''
#
# # 4.时间对象转成时间戳
# mt = time.mktime(time.localtime())
# print(mt) # 1679222499.0
# print(time.time())
#
#
# # datetime类,主要三大类 date time datetime  timedelta
# ## 1.date 类，属性 year, month, day
# d = datetime.date(2023, 3, 20)
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.today()) # 2023-03-19
#
# ## 2.time类 hour minute seconds
# t = datetime.time() #
# print(t) # 默认 00:00:00
# t = datetime.time(18, 46, 50)
# print(t) # 18:46:50
#
# ## 3.datetime类
# dt = datetime.datetime(2023, 3, 19, 18, 48, 59)
# print(dt) # 2023-03-19 18:48:59
#
# print(dt.date())
# print(dt.time())
# print(dt.year)
#
# ## 4.timedelta 类 时间运算
# dt = datetime.timedelta(days=1)
# t = datetime.datetime(2023, 3, 19, 18, 50, 1)
# print(t)
# res = t + dt
# print(res) # 2023-03-20 18:50:01

# 练习
## 1.计算当前时间加1天

def get_gap_date(format: str, num: int):
    """
    计算间隔多少天后的日期
    :param num:
    :return:
    """
    t = time.time() + num * 24 * 60 * 60
    res = time.strftime(format, time.localtime(t))
    return res


res = get_gap_date('%Y-%m-%d', -19)
print(res)

# 计算两个日期之间相差多少天?
## 使用 datetime里的 date 和 timedelta类处理

def get_gap_days(first_date: str, second_date: str):
    first_date = time.mktime(time.strptime(first_date, '%Y-%m-%d'))
    second_date = time.mktime(time.strptime(second_date, '%Y-%m-%d'))

    res = abs((second_date - first_date) / 24 / 60 / 60)
    print(int(res))


get_gap_days('2022-12-31', '2023-03-19')



