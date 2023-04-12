# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:34
# 文件名称: demo4.py

# 5.写函数，计算传入函数的字符串中,[数字]、[字母] 以及 [其他]的个数，并返回结果。

def func(data: str):
    digit = 0 # 数字
    alpha = 0 # 字母
    other = 0 # 其他
    if type(data) == str:
        for i in data:
            if i.isdigit():
                digit += 1
            elif i.isalpha():
                alpha += 1
            else:
                other += 1
        flag = {"数字": digit, "字母": alpha, "其他": other}
    else:
        flag = "数据非法，请输入字符串数据"
    return flag

print(func("abcd1234####$")) # {'数字': 4, '字母': 4, '其他': 5}
print(func(1)) # 数据非法，请输入字符串数据