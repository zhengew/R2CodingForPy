# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/25 12:00
# 文件名称: 带参数装饰器_demo2.py

"""
有100个函数，分别添加一个计算函数执行时间的装饰器
有的时候需要计算时间，有的时候不需要计算时间
希望能通过修改一个变量，控制这100个函数的装饰器是否执行
"""
import time

def timmer(yn_execute='Y'):
    """
    计算函数执行时间
    :param yn_execute: Y - 计算执行时间 N-不计算执行时间
    :return:
    """
    def wrapper(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            ret = func(*args, **kwargs)
            if yn_execute.upper() != 'Y':
                return ret
            end_time = time.time()
            func_run_time = round((end_time - start_time), 4)
            print(f"{func.__name__}函数执行时间: {func_run_time}秒～")
            return ret
        return inner
    return wrapper
@timmer()
def login():
    time.sleep(0.51)
    print("login函数执行完毕～～")

@timmer(yn_execute='N')
def register():
    time.sleep(0.75)
    print("regisger函数执行完毕～～")

@timmer()
def check():
    time.sleep(1.5)
    print('check函数执行完毕～～')

if __name__ == '__main__':
    login()
    register()
    check()

'''
login函数执行完毕～～
login函数执行时间: 0.5149秒～
regisger函数执行完毕～～
check函数执行完毕～～
check函数执行时间: 1.5048秒～
'''