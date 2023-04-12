# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 父类约束子类重写成员方法_方式二.py
# @datatime: 2023/4/5 11:56

"""
目标:理解软件开发规范，通过父类约束子类必须重写父类的同名方法
"""
# 方式二: 通过abc模块下的ABCMeta类、abstractmethod函数实现
# 缺点:依赖第三方模块
# 优点:强约束，子类如果未重写父类中被abstractmethod装饰的方法，子类在实例化的时候就会报错

from abc import ABCMeta, abstractmethod
class Payment(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def pay(self, money):
        """父类约束子类必须重写父类同名方法"""
        pass
class Wechat(Payment):
    def fuqian(self, money):
        print(f"{self.name}通过微信支付了{money}元")
if __name__ == '__main__':
    wechat = Wechat('alex')
    # TypeError: Can't instantiate abstract class Wechat with abstract method pay