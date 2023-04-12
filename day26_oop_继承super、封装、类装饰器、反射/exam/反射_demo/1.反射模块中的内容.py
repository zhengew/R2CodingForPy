# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 1.反射模块中的内容.py
# @datatime: 2023/4/8 13:07

"""
目标: 理解反射原理
1.反射模块中的内容
"""

import Animal
import sys

obj = getattr(sys.modules['Animal'], 'Animal') # <class 'Animal.Animal'>
print(obj.Counter) # 0
xiaobai = obj('小白', 20)
print(xiaobai.__dict__) # {'name': '小白', 'age': 20, 'Counter': 1}
xiaobai.eat()# 小白 is eating
pi = getattr(sys.modules['Animal'], 'pi')
print(pi) # 3.14
