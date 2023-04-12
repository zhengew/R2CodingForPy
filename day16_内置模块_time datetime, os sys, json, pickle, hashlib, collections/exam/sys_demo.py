# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/18 21:17
# 文件名称: sys_demo.py

"""
sys: 和python解释器相关的操作
"""
import sys
# 获取命令行方式运行的脚本后面的参数
# print('脚本名:',sys.argv[0]) # 脚本名
# print('第一个参数: ', sys.argv[1]) # 第一个参数

# 解释器存照模块的路径
# sys.path

# 已经加载的模块
# print(sys.modules)

sys.argv[0] = input("请输入用户名:")
sys.argv[1] = input("请输入密码: ")
print(f'用户名:{sys.argv[0]}, 密码:{sys.argv[1]}')