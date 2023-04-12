# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 面向对象中的归一化设计.py
# @datatime: 2023/4/5 12:13

"""
目标:理解父类约束子类重写方法，理解归一化设计思路，对外提供统一接口
"""
from abc import ABCMeta, abstractmethod
class Payment(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def pay(self, money):
        """约束子类重写pay方法"""
        pass

class AliPay(Payment):
    def pay(self, money):
        pay_dic = {'name': self.name, 'money': money}
        return pay_dic

class Wechat(Payment):
    def pay(self, money):
        pay_dic = {'name': self.name, 'money': money}
        return pay_dic

def pay(name, money, kind):
    """
    归一化设计:对外提供统一的付款接口
    :param name: 用户名
    :param money: 支付金额
    :param Kind: 付款方式 AliPay, Wechat
    :return:
    """
    if kind.__eq__('AliPay'):
        obj = AliPay(name)
    elif kind.__eq__('Wechat'):
        obj = Wechat(name)
    else:
        raise "参数错误～" # 主动抛异常
    return obj.pay(money)



if __name__ == '__main__':
    pay_dict = pay('alex', 100.00, 'AliPay')
    print(pay_dict) # {'name': 'alex', 'money': 100.0}

    wechat_pay_dic = pay('taibai', 200.00, 'Wechat')
    print(wechat_pay_dic) # {'name': 'taibai', 'money': 200.0}
