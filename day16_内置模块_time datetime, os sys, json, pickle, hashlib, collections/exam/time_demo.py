# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/18 18:53
# 文件名称: time_demo.py

"""
time 模块
三大对象：
时间戳
结构化时间对象(9大字段)
时间字符串
"""
import datetime
import time

# 时间戳
print(time.time())

# 获取格式化时间对象
## 格林尼治时间
print(time.gmtime())
'''
time.struct_time(tm_year=2023, tm_mon=3, tm_mday=18, tm_hour=11, tm_min=4, tm_sec=9, tm_wday=5, tm_yday=77, tm_isdst=0)
'''

## 本地时间
print(time.localtime())
'''
time.struct_time(tm_year=2023, tm_mon=3, tm_mday=18, tm_hour=19, tm_min=8, tm_sec=40, tm_wday=5, tm_yday=77, tm_isdst=0)
'''

# 格式化时间对象和字符串之间的转换
s = time.strftime('%Y-%m-%d %H:%M:%S')
print(s)

# 把时间字符串转换成时间对象
struct_time = time.strptime('2023-03-18 19:17:29', '%Y-%m-%d %H:%M:%S')
print(struct_time)

# 时间对象转换成时间戳
t1 = time.localtime() # 时间对象
t2 = time.mktime(t1) # 时间戳
print(t2) # 1679139299.0

# 暂停当前的线程,睡眠xxx秒
for i in range(5):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(1)

# 和时间段进行运算的结果类型：和另一个操作数保持一致
d = datetime.date(2023, 3, 18)
dt = datetime.timedelta(days=1)
ret = d + dt
print(ret, type(ret)) # 2023-03-19 <class 'datetime.date'>