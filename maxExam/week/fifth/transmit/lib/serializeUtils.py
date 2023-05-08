# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: serializeUtils.py
# @datatime: 2023/5/6 21:33

"""
序列化和反序列化
"""
import json
import pickle

class SerializeUtils(object):

    @staticmethod
    def json_dump(path: str, obj: object):
        """序列化写入文件"""
        with open(path, mode='at', encoding='utf-8') as f:
            f.write(json.dumps(obj) + '\n')

    @staticmethod
    def json_load(path: str):
        """从文件中反序列化"""
        with open(path, mode='rt', encoding='utf-8') as f:
            try:
                for line in f:
                    yield json.loads(line.strip())
            except EOFError:
                pass
    @staticmethod
    def json_dumps(obj: object):
        """序列化对象"""
        return json.dumps(obj)

    @staticmethod
    def json_loads(obj: str):
        """反序列化对象"""
        return json.loads(obj)

    @staticmethod
    def pickle_dump(path: str, obj: object):
        """序列化对象写入文件"""
        with open(path, mode='wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def pickle_load(path: str):
        """从文件中反序列化"""
        with open(path, mode='rb') as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    @staticmethod
    def pickle_dumps(obj: object):
        """序列化对象"""
        return pickle.dumps(obj)

    @staticmethod
    def pickle_loads(obj: object):
        """反序列化对象"""
        return pickle.loads(obj)

if __name__ == '__main__':
    from maxExam.week.fifth.transmit.conf.setting import ConfingHandler

    d1 = {'name': 'alex', 'age': '18'}
    # SerializeUtils.json_dump(ConfingHandler.users_path, d1)
    #
    # print(list(SerializeUtils.json_load(ConfingHandler.users_path)))

    # d2 = SerializeUtils.json_dumps(d1)
    # print(d2)
    #
    # d3 = SerializeUtils.json_loads(d2)
    # print(d3, type(d3))
    # print(d3['name'])

    # SerializeUtils.pickle_dump(ConfingHandler.users_path, d1)
    # obj = SerializeUtils.pickle_load(ConfingHandler.users_path)
    # # print(next(obj))
    # print([i for i in obj])