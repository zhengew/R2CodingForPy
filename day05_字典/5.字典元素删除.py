# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 19:31
# 文件名称: 5.字典元素删除.py

"""
目标：字典元素删除

1.pop 通过key删除value,返回被删除的元素，可设置返回值
2.popitem() 3.6版本后默认删除最后一个元素, 有返回值，返回被删除的键值对，元组格式:(key, value)
3.claer() 清空字典
4.del dict(key) 通过key删除 键值对
5.del dict 删除字典(注此操作相当于删除了实例对象)
"""

dict1 = {"name": "test1", "age":18, "sex": "男"}

# 1.pop 通过key删除元素，又返回值，可以设置默认返回值
value = dict1.pop("sex")
print(dict1) # {'name': 'test1', 'age': 18}
print(value) # 男

del_value = dict1.pop("sex", None)
print(del_value) # None
if del_value == None:
    print("Key不存在")

# 2.popitem() 默认删除最后一个元素(3.6之后的版本)
dict2 = {"name": "test1", "age":18, "sex": "男"}
value = dict2.popitem()
print(value) # ('sex', '男')
print(dict2) # {'name': 'test1', 'age': 18}

# 3.clear() 清空字典
dict3 = dict2.copy()
print(dict3) # {'name': 'test1', 'age': 18}
dict3.clear()
print(dict3) # {}

# 4. del dict(key) 通过key删除键值对
dict4 = dict1.copy()
print(dict4) # {'name': 'test1', 'age': 18}
del dict4["age"]
print(dict4) # {'name': 'test1'}

# 5.del dict 删除字典
del dict4
# print(dict4) # NameError: name 'dict4' is not defined. Did you mean: 'dict1'?


