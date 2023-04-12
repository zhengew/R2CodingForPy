# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/30 19:45
# 文件名称: walk_练习题.py

"""
使用os.walk 计算文件夹下的文件大小
"""
import os
import logging
logging.basicConfig(level=logging.DEBUG)

def get_file_size(path: str):
    """
    文件夹大小
    :param path:
    :return:
    """
    ret = os.walk(path)
    file_size_sum = 0
    for i in ret:
        file_path, files = i[0], i[2]
        for file in files:
            abs_path = os.path.join(file_path, file)
            file_size = os.path.getsize(abs_path)
            file_size_sum += file_size
            logging.debug(f"当前文件路径:{abs_path}, 当前文件大小:{file_size}")
            logging.debug(f"文件总大小: {file_size_sum}")
    return file_size_sum

if __name__ == '__main__':
    path = "/home/zew/PycharmProjects/R2CodingForPython/day22_oop第一天/exam"
    file_size_sum = get_file_size(path)
    print(file_size_sum)