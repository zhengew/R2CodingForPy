# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 14:42
# 文件名称: serialization_demo.py

"""
序列化
"""
# json: 将数据转换成字符串，用于存储或网络传输
import json

# s = json.dumps([1, 2, 3]) # 把指定的对象转换成json格式的字符串
# print(s, type(s)) # [1, 2, 3] <class 'str'>
#
# s2 = json.loads(s)
# print(s2, type(s2)) # [1, 2, 3] <class 'list'>


# 序列化,多次序列化与反序列化

def serialization(path, obj):
    with open(path, mode='at', encoding='utf-8') as f:
        f.write(json.dumps(obj) + '\n')

def deserialization(path):
    with open(path, mode='rt', encoding='utf-8') as f:
        for i in f:
            yield json.loads(i.strip())


if __name__ == '__main__':
    dict1 = {'name': 'alex', 'age': 20}
    lst1 = ['zhangsan', 'lisi', 'wangerma']
    path = 'test.txt'

    serialization(path, dict1)
    serialization(path, lst1)

    ret1 = deserialization(path)
    res = ret1.__next__()
    print(res, type(res))
    print(next(ret1))
    for i in ret1:
        print(i)
