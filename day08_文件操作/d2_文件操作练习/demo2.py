# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 20:46
# 文件名称: demo2.py

"""
alex是老男孩python发起人，创建人。
alex其实是人妖。
谁说alex是sb？
你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。

将文件中所有的alex都替换成大写的SB。
"""

import os

with open("file2", mode="r", encoding="utf-8") as f, open("file2_temp", mode = "w", encoding="utf-8") as f2:
    for i in f:
        f2.write(i.replace("alex", "SB"))

    f2.flush() # 强制刷新
    f2.close() # 关闭文件句柄

os.remove("file2")
os.rename("file2_temp", "file2")

