# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 19:58
# 文件名称: file_IO.py

bytes_str = b""
with open("test1", mode="r", encoding="utf-8") as f:
    # content = f.readlines()
    # print(content)
    for i in f:
        bytes_str += i.encode("utf-8")


# print(bytes_str) # b'\xe5\xba\x8a\xe5\x89\x8d\xe6\x98\x8e\xe6\x9c\x88\xe5\x85\x89\n\xe7\x96\x91\xe6\x98\xaf\xe5\x9c\xb0\xe4\xb8\x8a\xe9\x9c\x9c\n\xe4\xb8\xbe\xe5\xa4\xb4\xe6\x9c\x9b\xe6\x98\x8e\xe6\x9c\x88\n\xe4\xbd\x8e\xe5\xa4\xb4\xe6\x80\x9d\xe6\x95\x85\xe4\xb9\xa1'


# 文件写入
with open("file3.txt", mode="w", encoding="utf-8") as f:
    f.write("窗前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡")
    f.flush() # 强制保存


with open("file3.txt", mode="r") as f1, open("file4.txt", mode="wb") as f2:
    for i in f1:
        b_str = i.encode("utf-8")
        f2.write(b_str)


# 文件追加
with open("file5.txt", mode="a", encoding="utf-8") as f:
    with open("file3.txt", mode="r", encoding="utf-8") as r:
        for i in r:
            f.write(i)
        f.seek(0,2)
        print(f.tell())
        num = f.tell()
