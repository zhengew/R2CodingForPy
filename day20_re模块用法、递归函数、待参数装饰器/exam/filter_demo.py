# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/24 21:42
# 文件名称: filter_demo.py

l1 = ['1', '20', '', '', '30']
# ret = filter(lambda n:n, l1) # 列表去除空
# print(list(ret)) # ['1', '20', '30']

ret = filter(lambda x: x != '', l1)  #  lambda 筛选模式 return 条件为真的，字符串非空才是True
print(list(ret))

# 带参数装饰器有两个自由变量， args和func
def xxx(*args):
    def wrapper(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            return ret
        return inner
    return wrapper
