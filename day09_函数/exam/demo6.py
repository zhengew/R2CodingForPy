# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:35
# 文件名称: demo6.py

# 7.写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def func(data: dict):
    result = None
    if type(data) == dict:
        for k, v in data.items():
            if "__iter__" in dir(v): # 判断字典中的value是否可迭代
                data[k] = v[:2]
        result = data
    else:
        result = "参数非法，请传入dict类型数据"

    return result

d1 = {1: "abc", 2: "def", 3: "gh", 4:(1,2), 5: 123456, 6: [1, 2, 3]}

print(func(d1))

