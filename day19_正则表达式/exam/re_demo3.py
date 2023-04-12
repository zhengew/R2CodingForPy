# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/23 20:38
# 文件名称: re_demo3.py

"""
re模块练习题
"""
import re

# 匹配整数或者小数(包括正数或负数)

s1 = "123a+122-123+1.1-1.2"
regx = "[-+]?\d+(?:\.\d+)?"
ret = re.findall(regx, s1)
print(ret)

# 匹配年月日  2023-03-23
s2 = "2023-03-23ab202303222023-03-242023-3-2520230012"
regx = "[1-9]\d{3}-(?:0?[1-9]|1[012])-(?:0[1-9]|[12]\d|3[01])"

ret = re.findall(regx, s2)
print(ret)

# 匹配qq号 最小5位最大11位
s3 = "12345agc012345d123456789123"
regx = "[1-9]{4,11}"
ret = re.findall(regx, s3)
print(ret)

# 匹配11位电话号码
s4 = "18910438273#01871234123#1371234123a91812341234"
regx = "[1-9]\d{10}"
ret = re.findall(regx, s4)
print(ret)

# 长度位8到10位的密码，包含数字字母下划线
s5 = "123456a_%12345678"
regx = "\w{8,10}"
ret = re.findall(regx, s5)
print(ret)

# 匹配验证码：4位数字字母组成的
s6 = "12334abd&defA1"
regx = "[\da-zA-Z]{4}"
ret = re.findall(regx, s6)
print(ret)

# 匹配邮箱地址
s7 = "zhengew@foxmail.comzheng_erwei@huper.com"
regx = "\w+@[\da-zA-Z]+\.[a-zA-Z]{2,3}"
ret = re.findall(regx, s7)
print(ret)



# 这样的字符串中，
# 1）匹配出wahaha，banana，qqxing内容。
# 2）匹配出a,b,h1这样的内容
info = \
'''
<a>wahaha</a>
<b>banana</b>
<h1>qqxing</h1>
'''

# 1>
regx = "<.*?>(.*?)<.*?>"
ret = re.findall(regx, info)
print(ret)

# 2>
regx = "<(.*?)>.*?<.*?>"
ret = re.findall(regx, info)
print(ret)

# 9、`1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 1）`从上面算式中匹配出最内层小括号以及小括号内的表达式【即里面没有小括号的小括号】
info = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
regx = "[(]([^()]+)[)]"
ret = re.findall(regx, info)
print(ret)

# a开头至少一位字母组成
regx = "a[a-zA-Z]*"

# 以1开头，中间3-5位数字，x结尾，中间的值不能超过5位
regx = "1\d{3,5}x"





# 10、从类似`9-2*5/3+7/3*99/4*2998+10*568/14`的表达式中匹配出从左到右第一个乘法或除法

info = "9-2*5/3+7/3*99/4*2998+10*568/14"
regx = "\d+[*/]\d+"
ret = re.search(regx, info)
print(ret)
print(ret.group())