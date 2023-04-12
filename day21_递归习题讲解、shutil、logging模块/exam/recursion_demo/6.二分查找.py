# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/28 20:33
# 文件名称: 6.二分查找.py

"""
目标：从有序列表中查找指定元素的索引位置
二分查找法
"""
def binary_lockup(data_list: list, n: int):
    """
    从有许列表中查找数值n的索引位置
    :param data_list: 有序列表
    :param n: 数值n
    :return: n的索引位置
    """
    top = 0
    end = len(data_list) - 1
    index = -1
    while top <= end:
        mid = int((top + end) / 2)
        if n == data_list[mid]:
            index = mid
            break
        elif data_list[mid] > n:
            end = mid - 1
        elif data_list[mid] < n:
            top = mid + 1
    return index


if __name__ == '__main__':
    while 1:
        value = int(input('>>>'))
        data = [i ** 2 for i in range(11)]
        ret = binary_lockup(data, value)
        print(f'index: {ret}, data[ret] = {data[ret]}')
