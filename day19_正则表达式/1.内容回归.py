# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/10 07:16
# 文件名称: 1.内容回归.py

# 基础数据类型
# 流程控制：条件判断 循环
# 文件操作
# 函数
    # 基础：定义 传参 返回值 嵌套
    # 装饰器
        # 带参数的装饰器
    # 迭代器 生成器
    # 递归函数 --
# 常用模块
    # random
    # hashlib
    # time datetime
    # collections
    # sys
    # os
    # json/pickle
    # re 模块
    # logging模块
    # 包的导入

# 面向对象 - 6天
# 网络编程 - 4天
# 并发编程 - 5-6天
# 数据库 - 5天

# 21天

# * 函数形参角度：聚合
def func(*args, **kwargs):
    print(args) # ('lucy', '18', 'nv')
    print(kwargs) # {'hoby': 'running', 'score': 100}


func('lucy', '18', 'nv', hoby= 'running', score = 100)


# * 函数调用，实参角度：打散

def func2(*args):
    print(args)

func2(*[1, 2 ,3], *[4, 5, 6])