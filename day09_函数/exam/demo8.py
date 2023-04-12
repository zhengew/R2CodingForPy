# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:36
# 文件名称: demo8.py

# 9.写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，
# 然后将这四个内容传入到函数中，此函数接收到这四个内容，将内容追加到一个student_msg文件中。

def func(name: str, sex: str, age: int, degree: str):
    """
    :param name: 姓名
    :param sex: 性别
    :param age: 年龄
    :param degree: 学历
    :return:
    """
    with open("student_msg.txt", mode="a", encoding="utf-8") as f:
        f.write(f"{name}|{sex}|{age}|{degree}\n")
        f.seek(2)
        f.flush()
        f.close()


func("lucy", "女", 18, "本科")