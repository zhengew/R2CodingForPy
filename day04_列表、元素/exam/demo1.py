# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 16:12
# 文件名称: demo1.py

# 1.使用for循环对s="asdfer"进行循环，但是每次打印的内容都是"asdfer"。
# s = "asdfer"
# for i in s:
#     print(s)


# 1.使用for循环对s="abcdefg"进行循环，每次打印的内容是每个字符加上sb， 例如：asb, bsb，csb,...gsb。

# s="abcdefg"
# for i in s:
#     print(i + "sb")

# 3.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"。
# s = "321"
# for i in s:
#     # print("倒计时%s秒" %(i))
#     print(f"倒计时{i}秒")

# 实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9，然后进行分割再进行计算。

# content = input("请输入内容(1 + 2):")
# data = content.replace(" ", "").split("+")
# sum = 0
# for i in data:
#     sum += int(i)
# print(sum)

# 选做题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+ 13，然后进行分割再进行计算。
# content = input("请输入内容(1 + 2):")
# data = content.replace(" ", "").split("+")
# sum = 0
# for i in data:
#     sum += int(i)
# print(sum)



# 计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：") # 如fhdal234slfh9876+=9fjdla

content = input("请输入内容：")
countNumber = 0
for i in content:
    if i.isdigit():
        countNumber += 1

print(countNumber)