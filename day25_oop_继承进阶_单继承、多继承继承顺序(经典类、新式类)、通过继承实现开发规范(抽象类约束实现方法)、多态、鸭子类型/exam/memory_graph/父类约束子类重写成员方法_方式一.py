# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 父类约束子类必须实现的成员方法.py
# @datatime: 2023/4/5 11:38

"""
目标:理解软件开发规范，通过父类约束子类必须重写父类的同名方法
"""
# 方式一: 代码实现，方法中主动抛出异常: raise NotImplementedError
class Payment(object):
    def __init__(self, name):
        self.name = name
    def pay(self, money):
        """父类约束子类必须重写父类同名方法"""
        raise NotImplementedError("请在子类中重写同名pay方法")
class Wechat(Payment):

    def fuqian(self, money):
        print(f"{self.name}通过微信支付了{money}元")

if __name__ == '__main__':
    wechat = Wechat('alex')
    wechat.pay(30) # NotImplementedError: 请在子类中重写同名pay方法