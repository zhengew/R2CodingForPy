# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:36
# 文件名称: demo9.py

"""
10.对第9题升级：支持用户持续输入，Q或者q退出，性别默认为男，如果遇到女学生，则把性别输入女。
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（选做题）。
**三个参数：path, old_content, new_content**
"""

def func(name: str, age: int, degree: str, sex="男"):
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


if __name__ == '__main__':
    while True:
        name = input("姓名: ")
        if name.upper() == "Q": break
        age = input("年龄: ")
        if age.upper() == "Q": break
        sex = input("性别: ")
        if sex.upper() == "Q": break
        degree = input("学历: ")
        if degree.upper() == "Q": break

        func(name=name, age=age, degree=degree) if sex != "女" else func(name=name, age=age, degree=degree, sex=sex)
