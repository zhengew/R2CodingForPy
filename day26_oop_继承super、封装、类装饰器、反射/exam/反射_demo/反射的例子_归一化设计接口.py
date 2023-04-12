# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 反射的例子_归一化设计接口.py
# @datatime: 2023/4/8 14:56

"""
目标: 使用反射实现归一化设计接口
"""
import sys
class Payment(object):
    def __init__(self, name):
        self.name = name

    def pay(self, money):
        """抽象方法"""
        raise NotImplemented("请重写父类中的pay方法")

class AliPay(Payment):
    def pay(self, money):
        print(f"{self.name}通过{AliPay.__name__}支付了{money}元")

class WechatPay(Payment):
    def pay(self, money):
        print(f"{self.name}通过{WechatPay.__name__}支付了{money}元")

class QQPay(Payment):
    def pay(self, money):
        print(f"{self.name}通过{QQPay.__name__}支付了{money}元")

def pay(name, money, kind):
    """
    利用反射实现归一化设计，对外提供统一的支付接口
    :param name: 姓名
    :param money: 金额
    :param kind: 支付方式
    :return:
    """
    if hasattr(sys.modules['__main__'], kind): # 先判断kind是否存在，是否可以反射
        class_obj = getattr(sys.modules['__main__'], kind)(name) # 再拿到反射的类并实例化对象
        if callable(class_obj.pay): # 再判断实例化对象中的pay方法是否可调用
            class_obj.pay(money) # 再执行实例化对象的pay方法

if __name__ == '__main__':
    pay('alex', 100, 'AliPay') # alex通过AliPay支付了100元
    pay('alex', 102, 'WechatPay') # alex通过WechatPay支付了102元
    pay('alex', 103, 'QQPay') # alex通过QQPay支付了103元
