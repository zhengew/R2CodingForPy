# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 20:59
# 文件名称: demo1.py

"""
计算水仙花数
三位整数，每一位的三次方的和还等于这个数
"""
print(3 ** 3 + 5 ** 3 + 1 ** 3)
def is_shuixianhua(number: str):
    count = 0
    for i in number:
        count += int(i) ** 3
    return True if count == int(number) else False

while True:
    guess = input("请输入任意三位数字: ")
    if guess.isdigit() and len(guess) == 3:
        result = is_shuixianhua(number=guess)
        print(f"{guess}是水仙花数: {result}")
    else:
        print("输入错误")
