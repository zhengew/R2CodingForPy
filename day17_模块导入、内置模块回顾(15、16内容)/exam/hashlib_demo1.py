# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/21 22:11
# 文件名称: hashlib_demo1.py
import hashlib
import os
import time

path = os.path.join('/Users/erwei.zheng/Downloads', 'pycharm-professional-2022.3.2.dmg')
print(path)

def timmer(f):
    def inner(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        end_time = round((time.time() - start), 2)
        print(f"{f.__name__}耗时:{end_time}秒")
        return ret

    return inner


def bytes_from_files(filename: str, chunksize=1024):
    with open(filename, mode='rb') as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                yield chunk
            else:
                break

@timmer
def get_file_md5(filename, chunksize=1024):
    """
    任意文件的md5值
    :param filename:
    :param chunksize:
    :return:
    """
    m = hashlib.md5()
    with open(filename, mode='rb') as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                m.update(chunk)
            else:
                break
        f.close()
    return m.hexdigest()




if __name__ == '__main__':
    m = hashlib.md5()
    for b in bytes_from_files(filename=path):
        m.update(b)
    ret = m.hexdigest()
    print(ret)

    ret2 = get_file_md5(filename=path)
    print(ret2)

