# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 封装json类.py
# @datatime: 2023/4/5 17:20

"""
目标:封装json类
实现多次写，多次读
"""
import json
class MyJson(object):
    def __init__(self, path):
        """序列化对象保存路径"""
        self.path = path
    def dump(self, obj):
        """序列化"""
        with open(self.path, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(obj) + '\n')
    def load(self):
        """反序列化"""
        with open(self.path, mode='rt', encoding='utf-8') as f:
            try:
                for i in f:
                    yield json.loads(i) # 生成器函数 通过list __next__ for 取数
            except EOFError as e:
                raise e

if __name__ == '__main__':
    alex = {'name': 'alex', 'age': 18}
    wusir = {'name': 'wusir', 'age': 20}

    obj = MyJson('myjson.txt')
    # 序列化
    obj.dump(alex)
    obj.dump(wusir)
    # 反序列化
    ret = [i for i in obj.load()] # 遍历生成器对象
    print(ret) # [{'name': 'alex', 'age': 18}, {'name': 'wusir', 'age': 20}]

