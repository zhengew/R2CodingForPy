# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/18 20:23
# 文件名称: os_demo.py

"""
os: 和操作系统相关的操作被封装到这个模块中

"""
import os

# 和文件操作相关:
## 删除
# os.remove(r'a.txt')

## 重命名
# os.rename('a.txt', 'b.txt')

## 删除目录：必须是空目录
# os.removedirs(r'a')

## 使用shutil模块可以删除带内容的目录
# import shutil
# shutil.rmtree('a')


# 和路径相关的操作，被封装到另一个自模块中: os.path
res = os.path.dirname(r'/usr/local/bin/') # 不判断路径是否存在
print(res) # /usr/local/bin

# 获取文件名
res = os.path.basename(r'/usr/local/bin/a.txt')
print(res) # a.txt

# 把路径名和文件名切分开，结果是元组
res = os.path.split(r'/usr/local/bin/a.txt')
print(res) # ('/usr/local/bin', 'a.txt')

# 拼接路径
path = os.path.join('/usr', 'local', 'bin', 'a.txt')
print(path) # /usr/local/bin/a.txt

# 如果是/开头的路径，默认是在当前盘符下
# 如果不是/开头，默认当前路径
res = os.path.abspath(r'/usr/local/bin/')
print(res)

# 判断
## 是不是绝对路径
print(os.path.isabs('a.txt')) # False

##
print(os.path.isdir('b.txtb.txt')) # False, 先在路径下找，找到了在判断是目录还是文件，找不到返回False
print(os.path.exists('b.txt')) # True
print(os.path.isfile('b.txt')) # True, 先在路径下找，找到了在判断是文件还是目录，找不到返回False






