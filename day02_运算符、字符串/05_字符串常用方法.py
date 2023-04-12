# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/514:07
# 文件名称: 07_字符串常用方法.py


# count 统计字符中元素出现次数
str = "abcabcabc"
print(str.count("abc")) # 3

# startswith  以...开头， endswith 以...结尾
str2 = "abcdefg"
print(str2.startswith("abc")) # True
print(str2.endswith("efg")) # True
print(str2.startswith("abc", 0, 4)) # 支持切片，顾头不顾尾

# split 以...分割元素，保存到列表中
## 重载功能  rsplit
str3 = "abc,def,ghi,jkl"
res = str3.split(",")
print(res)

print(str3.rsplit(",", 1)) # 匹配几次 不常用把

# 格式化输出
print("姓名:%s, 年龄:%d, 性别:%s" % ("lucy", 18, "女"))

# strip 去空格或获取指定字符
str4 = "   abc    ***  "
print(str4.strip().strip("*").strip()) # abc
print(str4.rstrip()) # 去除右边指定字符，默认取空格 #    abc    ***
print(str4.lstrip()) # abc    ***

# is系列 判断字符串由什么组成
str5 = "123"
print(str5.isalnum()) # true
print("abc".isalnum())
print("abc123".isalnum())
print("123".isdecimal())
print("123".isdigit())

# find 指定字符串在元素中是否存在，存在返回索引位置，不存在返回-1
str6 = "abc123def"
index = str6.find("1")
if index != -1:
    print(str6[index:])
else:
    print(f"{str6}中不存在指定元素: 1")


# index 返回指定元素的索引位置，找不到则抛出异常 ValueError: substring not found
str7 = "abc123abc"
index = str7.index("3")

print(index)

# 字符串格式转换
# 1.首字母大写
str8 = "test1 test2"
print(str8.capitalize())
# 2.大小写翻转
print(str8.swapcase())
# 3.每个单词的首字母大写
print(str8.title())
# 4.居中展示
print(str8.center(20, "*"))

print("转账功能".center(100, "*"))