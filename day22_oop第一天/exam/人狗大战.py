# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/31 06:42
# 文件名称: 人狗大战.py.py

class Person(object):
    def __init__(self, name, sex, job,  hp, weapon, ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.level = 0
        self.hp = hp
        self.weapon = weapon
        self.ad = ad

    def cuozao(self, dog):
        dog.hp -= self.ad
        print('%s给%s搓了澡,%s掉了%s点血,%s当前血量%s' % (self.name, dog.name,
                                                          dog.name, self.ad, dog.name, dog.hp))

class Dog(object):
    def __init__(self, name, kind, hp, ad):
        self.name = name
        self.variety = kind
        self.hp = hp
        self.ad = ad

    def tian(self, person):
        print(self.__dict__)
        print(person.__dict__)
        if person.hp >= self.ad:
            person.hp -= self.ad
        else:
            person.hp = 0
        print('%s舔了%s,%s掉了%s点血,%s当前血量%s' % (self.name, person.name,
                                                          person.name, self.ad, person.name, person.hp))
alex = Person('alex', '不详', '搓澡工', 250, '搓澡巾', 1)
xiaobai = Dog('小白', '哈士奇', 5000, 249)
print(xiaobai.__dict__) # {'name': '小白', 'variety': '哈士奇', 'hp': 5000, 'ad': 249}


alex.cuozao(xiaobai)
xiaobai.tian(alex)