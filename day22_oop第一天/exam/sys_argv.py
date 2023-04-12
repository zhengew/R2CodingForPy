# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/29 06:55
# 文件名称: sys_argv.py.py

"""
目标：ys.argv练习
通过脚本方式执行文件操作
"""
import os.path
# 写一个python脚本,在cmd里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址
# python xxx.py alex sb cp D:\python_22\day22\1.内容回顾.py D:\python_22\day21
# python xxx.py alex sb rm D:\python_22\day22
# python xxx.py alex sb rename D:\python_22\day22  D:\python_22\day23

import shutil
import sys

def copy_self(source_path, to_path):
    """
    脚本方式执行拷贝
    :param source_path:
    :param to_path:
    :return:
    """
    if os.path.exists(source_path):
        if os.path.exists(to_path) is False:
            os.mkdir(to_path)
        shutil.copy2(source_path, to_path)
        return f'{os.path.basename(source_path)}文件拷贝成功'
    else:
        return f'源路径不存在:{source_path}'

def rename_self(source_path, to_path):
    """
    脚本方式执行重命名
    :param source_path:
    :param to_path:
    :return:
    """
    if os.path.exists(source_path):
        os.rename(source_path, to_path)
        return f'重命名成功，{os.path.basename(source_path)}重命名为: {os.path.basename(to_path)}'
    else:
        return f'源路径不存在:{source_path}'

def remove_self(source_path):
    """
    脚本方式删除目录
    :param source_path:
    :return:
    """
    if os.path.exists(source_path):
        if os.path.isfile(source_path):
            os.remove(source_path)
        else:
            shutil.rmtree(source_path)
        return f'{source_path}文件/目录删除成功～'
    else:
        return f'源路径不存在:{source_path}'

def main():
    """
    主程序
    :return:
    """
    if len(sys.argv) >= 5: # sys.argv 终端是一个列表，第0个元素是脚本的路径，第一个元素开始是需要用户输入的命令
        name = sys.argv[1]
        pwd = sys.argv[2]
        command = sys.argv[3]
        source_path = sys.argv[4]

        match command:
            case 'cp':
                res = copy_self(source_path, to_path=sys.argv[5])
                print(res)
            case 'rename':
                res = rename_self(source_path, to_path=sys.argv[5])
                print(res)
            case 'rm':
                res = remove_self(source_path)
                print(res)
            case _:
                print(f'[{command}] 命令不存在～')
    else:
        print('您输入的命令无效～')

if __name__ == '__main__':
    main()

"""
# 测试 cp
python sys_argv.py test1 123  cp './a/test_copy2.txt' './b/'
# 测试 rename
python sys_argv.py test1 123  rename './b/test_copy2.txt' './b/test_copy3.txt'
# 测试删除文件或目录 rm 
python sys_argv.py test1 123  rm './b/test_copy3.txt'

"""
