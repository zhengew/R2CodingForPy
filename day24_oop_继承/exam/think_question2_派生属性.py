# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 16:18
# 文件名称: think_question2_派生属性.py

"""
思考：如何给子类添加特有的属性
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
    def __init__(self, name, food, eye_color):
        Animal.__init__(self, name, food) # 调用父类的初始化，去完成通用属性的初始化
        self.eye_color = eye_color # 派生属性
    def eat(self):
        self.blood += 100
        Animal.eat(self)
        self.drink()
    def climb_tree(self):
        print(f"{self.name}正在爬树～")

class Dog(Animal):

    def __init__(self, name, food, size):
        Animal.__init__(self, name, food)
        self.size = size # 派生属性
    def eat(self):
        self.wise += 100
        Animal.eat(self)
        self.drink()
    def house_keep(self):
        print(f"{self.name}看家～")

if __name__ == '__main__':
    xiaobai = Cat('小白', '猫粮', '蓝色')
    xiaohei = Dog('小黑', '狗粮', '大型犬')
    xiaobai.eat()
    xiaohei.eat()
    print(xiaobai.__dict__)
    print(xiaohei.__dict__)