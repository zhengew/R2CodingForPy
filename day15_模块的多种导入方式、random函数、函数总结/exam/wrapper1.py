# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/16 07:29
# 文件名称: wrapper1.py

def wrapper(f):
    def inner(*args, **kwargs):
        """执行前"""
        print(f"每次执行被装饰函数[{f.__name__}]之前，都得先经过这里")
        ret = f()
        """执行后"""
        return ret
    return inner
@wrapper # fun1 = wrapper(fun1)
def fun1():
    print('in func1')
@wrapper # func2 = wrapper(func2)
def func2():
    print('in func2')

if __name__ == '__main__':
    fun1() # inner()
    func2()

