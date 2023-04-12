# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/2 15:03
# 文件名称: cat_dog_demo.py

class Cat():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name}正在吃～")
    def drink(self):
        print(f"{self.name}正在喝～")
    def sleep(self):
        print(f"{self.name}正在睡～")
    def climb_tree(self):
        print(f"{self.name}正在爬树～")

class Dog():
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name}正在吃～")
    def drink(self):
        print(f"{self.name}正在喝～")
    def sleep(self):
        print(f"{self.name}正在睡～")
    def house_keep(self):
        print(f"{self.name}看家～")

if __name__ == '__main__':
    huahua = Cat('huahua')
    xiaobai = Dog('taibai')
    huahua.eat()
    huahua.drink()
    huahua.sleep()
    huahua.climb_tree()
