# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: file_operate.py
# @datatime: 2023/4/12 07:19

"""
# 用反射完成
# python3 xx.py cp path1 path2
# python3 xx.py rm path
# python3 xx,py mv path1 path2
"""
import os
import sys
import shutil

class FileOper(object):
    """
    文件的拷贝、删除、剪切
    """
    @staticmethod
    def cp(path1: str, path2: str):
        """拷贝文件"""
        if os.path.exists(path1) and os.path.exists(path2):
            shutil.copy2(path1, path2)
    @staticmethod
    def rm(path: str):
        """删除文件或目录"""
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)

    @staticmethod
    def mv(path1: str, path2: str):
        """移动文件或目录，如果存在则判断是否覆盖"""
        if os.path.exists(path1) and os.path.exists(path2):
            filename = os.path.basename(path1)
            if filename in next(os.walk(path2))[2]:
                command = input(f"{path2}中已存在文件{filename}, 是否覆盖? Y/N")
                if command.upper() == 'Y':
                    abspath = os.path.join(path2, filename)
                    FileOper.rm(abspath)
                    shutil.move(path1, path2)
                elif command.upper() == 'N':
                    print(f"取消移动文件:{filename}至{path2}~")
            else:
                shutil.move(path1, path2)

def run():
    """
    在主方法中进行脚本操作
    :return:
    """
    # python xx,py mv path1 path2
    if len(sys.argv) == 4:
        if hasattr(FileOper, sys.argv[1]):
            obj = getattr(FileOper, sys.argv[1])
            if callable(obj):
                obj(path1=sys.argv[2], path2=sys.argv[3])
    elif len(sys.argv) == 3:
        if hasattr(FileOper, sys.argv[1]):
            obj = getattr(FileOper, sys.argv[1])
            if callable(obj):
                obj(path=sys.argv[2])

if __name__ == '__main__':
    run()
    """
        python3 file_operate.py cp testcp a
        python3 file_operate.py mv a/testcp b
        python3 file_operate.py rm a/testcp
        """

    # FileOper.cp(r'file_operate.py', 'a')
    # f = open('a/test1', mode='w', encoding='utf-8')
    # f.close()
    #
    # # os.remove('test1')
    # FileOper.rm('a/test1')
    #
    # f = open('a/test3', mode='w', encoding='utf-8')
    # f.close()
    # FileOper.mv('a/test3', 'b')



