# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 07:50
# 文件名称: wrapper4.py
import time


def wrapper(func):
    def inner(*args, **kwargs):
        with open('logs', mode='a', encoding='utf-8') as f:
            curr_time = time.localtime()
            f.write(f"函数名:{func.__name__}, 调用时间: {time.strftime('%Y-%m-%d %H:%M:%S', curr_time)}\n")
            f.flush()
            f.close()
        ret = func(*args, **kwargs)
        return ret
    return inner

@wrapper
def func():
    print('in func')

if __name__ == '__main__':
    func()