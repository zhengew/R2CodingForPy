# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/24 22:16
# 文件名称: RecursionError_demo.py

import sys

sys.setrecursionlimit(100000000)

# 测试递归最大深度

count = 0

def func():
    global count
    count += 1
    print(count)
    if count == 3: return
    func()
    print(456)

func() # 21837

# 函数的调用
# 函数的参数
# 函数的返回值