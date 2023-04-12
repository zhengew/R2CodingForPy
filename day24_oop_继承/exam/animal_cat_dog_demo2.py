# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 15:37
# 文件名称: animal_cat_dog_demo2.py

"""
继承:
1.子类继承父类的成员变量和成员方法
2.子类重写父类中的方法，调用时执行子类自己的
3.子类中没有的方法，则从父类中找
4.子类重写了父类重名方法，同时又想调用父类中的同名方法，则在子类方法中主动调用父类的方法，并把self作为参数传递过去
5.子类中没有，父类中有的方法，则通过self.的方式调用父类方法
"""

class Animal(object):
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.blood = 100
        self.wise = 100

    def eat(self):
        print(f"{self.name}正在吃{self.food}～")

    def drink(self):
        print(f"{self.name}正在喝～")

    def sleep(self):
        print(f"{self.name}正在睡～")

class Cat(Animal):
    def eat(self):
        self.blood += 100
        Animal.eat(self)
        self.drink()
    def climb_tree(self):
        print(f"{self.name}正在爬树～")

class Dog(Animal):
    def eat(self):
        self.wise += 100
        Animal.eat(self)
        self.drink()
    def house_keep(self):
        print(f"{self.name}看家～")


if __name__ == '__main__':
    xiaobai = Cat('小白', '猫粮')
    xiaohei = Dog('小黑', '狗粮')
    xiaobai.eat()
    xiaohei.eat()

    print(xiaobai.__dict__)
    print(xiaohei.__dict__)

"""
小白正在吃～
小白正在喝～
小黑正在吃～
小黑正在喝～
{'name': '小白', 'blood': 200, 'wise': 100}
{'name': '小黑', 'blood': 100, 'wise': 200}
"""
