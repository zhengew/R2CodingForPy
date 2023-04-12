# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 反射的例子.py
# @datatime: 2023/4/11 07:21

"""
目标: 理解反射的又一个例子
"""
class FileOpt(object):

    __func_list = [('写文件', 'write'), ('读文件', 'read')]
    @property
    def func_list(self):
        """对外提供私有属性的查询权限"""
        return self.__func_list

    def __init__(self, path):
        self.path = path
    def write(self):
        print('in write')
    def read(self):
        print('in read')

if __name__ == '__main__':
    f = FileOpt('file_test.txt')
    while True:
        for id, func in enumerate(f.func_list, 1):
            print(id, func[0])
        option = input("请选择: ")
        if option.isdigit() and int(option) >=1 and int(option) <= len(f.func_list):
            if hasattr(f, f.func_list[int(option)-1][1]):
                obj = getattr(f, f.func_list[int(option)-1][1])
                if callable(obj):
                    obj()
        elif option.upper() == 'Q':
            break
        else:
            print("输入错误, 请重新输入～")