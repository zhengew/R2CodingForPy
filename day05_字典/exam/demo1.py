# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 20:25
# 文件名称: demo1.py

# 1.
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,
# 将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。

li= [11,22,33,44,55,66,77,88,99,90]
result = {'k1':[],'k2':[]}
for i in li:
    if i > 66:
        result["k1"].append(i)
    elif i < 66:
        result["k2"].append(i)

print(result) # {'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55]}

# 2.有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}

res = dict()
str = "k: 1|k1:2|k2:3 |k3 :4"
list_data = str.replace(" ", "").split("|")
for i in list_data:
    key, value = i.split(":")
    res[key] = int(value)

print(res) # {'k': 1, 'k1': 2, 'k2': 3, 'k3': 4}

# 3.请循环打印k2对应的值中的每个元素
print("".center(50, "*"))
info = {
    'k1':'v1',
    'k2':[('alex'),('wupeiqi'),('oldboy')],
}

for i in info["k2"]:
    print(i)
