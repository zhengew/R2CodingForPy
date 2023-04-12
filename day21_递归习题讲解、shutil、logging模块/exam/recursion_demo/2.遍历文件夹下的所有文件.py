"""
目标：遍历文件夹下的所有文件，理解执行步骤
"""
import os


def show_file(path: str):
    """
    目录下的所有文件
    :param path:
    :return:
    """
    names = os.listdir(path)
    file_list = []
    for name in names:
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            file_list.append(name)
        else:
            file_list += show_file(abs_path) # 递归之后将每一层的file_list累加，将累加后的结果return给上一层调用方
    return file_list

if __name__ == '__main__':
    path = "/home/zew/PycharmProjects/R2CodingForPython/"
    ret = show_file(path)
    print(ret)