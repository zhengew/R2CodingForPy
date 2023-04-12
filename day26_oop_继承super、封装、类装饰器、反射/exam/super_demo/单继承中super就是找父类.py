# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 单继承中super就是找父类.py
# @datatime: 2023/4/7 下午1:12

"""
目标：理解super在单继承中的用法
super 在单继承中就是找父类
"""
class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating~")

class Cat(Animal):
    def __init__(self, name, age, eye_color):
        super(Cat, self).__init__(name, age)
        self.eye_color = eye_color # 派生属性
    def sleep(self):
        super(Cat,self).eat()
        print(f'{self.name}开始睡觉～')

if __name__ == '__main__':
    xiaobai = Cat('小白', 2, 'blue')
    xiaobai.eat() # 小白 is eating~
    xiaobai.sleep() # 小白 is eating~  小白开始睡觉～



