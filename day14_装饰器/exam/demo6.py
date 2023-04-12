# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/15 20:50
# 文件名称: demo6.py

# 请实现一个装饰器，通过一次调用使函数重复执行5次。

def decorators(func):
    def inner(*args, **kwargs):
        for i in range(5):
            ret = func(*args, **kwargs)
        return ret
    return inner
@decorators
def func():
    print('请实现一个装饰器，通过一次调用使函数重复执行5次。')


if __name__ == '__main__':
    func()