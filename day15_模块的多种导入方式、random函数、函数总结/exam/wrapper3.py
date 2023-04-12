# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 07:41
# 文件名称: wrapper3.py

def wrapper(f):
    def inner(*args, **kwargs):
        for i in range(1, 6):
            print(f'被装饰函数[{f.__name__}]被第{i}次调用')
            ret = f(*args, **kwargs)
        return ret
    return inner
@wrapper
def func():
    print("in func")
@wrapper
def func2():
    print('in func2')


if __name__ == '__main__':
    ret = func()
    func2()