"""
目标：计算目录及子目录下所有文件的大小
理解递归中函数的值传递
"""
import os


def show_file_size(path: str):
    """
    计算目录下所有的文件大小
    :param path:
    :return:
    """
    sum_file_size = 0
    file_list = os.listdir(path)
    for name in file_list:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            sum_file_size += os.path.getsize(abs_path)
        else:
            sum_file_size += show_file_size(abs_path) # 每次递归，都会return当前文件夹内的文件大小之和，再累加

    return sum_file_size

if __name__ == '__main__':
    path = "/home/zew/PycharmProjects/R2CodingForPython/day21_递归习题讲解、shutil、logging模块/exam"
    ret = show_file_size(path)
    print(ret)