# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/15 20:59
# 文件名称: demo7.py


# 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
import time

def wrapper(func):
    def inner(*args, **kwargs):
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        with open('callable_time', mode='a', encoding='utf-8') as f:
            f.seek(2, 0)
            f.write(f"{func.__name__}: {t}")
            f.write('\n')
            f.flush()
            f.close()
        ret = func(*args, **kwargs)
        return ret
    return inner

@wrapper
def func():
    print("请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。")

if __name__ == '__main__':
    time.sleep(0.5)
    func()
    t = time.strptime('2023-03-15 21:21:10', '%Y-%m-%d %H:%M:%S')
    print(t)