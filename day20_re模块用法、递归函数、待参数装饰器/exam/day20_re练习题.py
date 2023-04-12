# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/25 12:34
# 文件名称: day20_re练习题.py
import re

# 1、匹配一篇英文文章的标题 类似 <<The Voice Of China>> <<Hello Python>>
# title = "<<The Voice Of China>> <<Hello Python>>"
# regx = "<<([A-Z][a-z]*(?: [A-Z][a-z]*)*?)>>"
# ret = re.findall(regx, title)
# print(ret)
#
# # 2、【★】匹配一个网址
# add = "www.baidu.com www.jd.com"
# regx = "((http|https)://)?www([.][a-zA-Z]+){2,}"
# ret = re.search(regx, add)
# print(ret)
#
# # 3、【★】匹配年月日日期 类似 2018-12-06 2018/12/06 2018.12.06，年首位不为0，月、日可以是一位数或两位数】【连接符任意但是前后要一致】
# info = "2023-03-25" #  2018/12/06 2018.12.06
# regx = re.compile("[1-9]\d{3}(?P<sep>.*?)(0?[1-9]|1[0-2])(?P=sep)(0?[1-9]|[12]\d|3[01])$")
# res = regx.match(info)
# print(res.group('sep'))
# print(res.group())
#
# # 4、【★】匹配15位或者18位身份证号
# regx = re.compile("^[1-9]\d{14}(?:\d{2}[\dX])?$") # ^[1-9]\d{14}(\d{2}[\dx])?$
# id1 = '130123412341234'
# id2 = '130123412341234120'
# id3 = '13012341234123412X'
#
# res = regx.findall(id3)
# print(res)

# 5、从lianjia.html（html文件在群文件中）中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅   单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]

# regx = '.*?data-sl="">(?P<name>.*?)</a>.*?<div class="houseInfo">.*?<span class="divide">/</span>(?P<type>.*?)<span class="divide">/</span>(?P<area>.*?)<span class="divide">.*?<div class="flood">'
regx = r'.*?data-sl="">(?P<name>.*?)</a>.*?<span class="divide">/</span>(?P<type>.*?)<span class="divide">/</span>(?P<area>.*?)<span class="divide">'

with open('lianjia.html', encoding='utf-8') as f:
    content = f.read()
    res = re.finditer(regx, content, re.S)

for i in res:
    print(i.group('name'), i.group('type'), i.group('area'))

# print([i.group('name') for i in res])

# 6、1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
content = "1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
regx = "[(]([^()]+)[)]"
res = re.findall(regx, content) # ['-40/5', '9-2*5/3+7/3*99/4*2998+10*568/14', '-4*3', '16-3*2']
print(res)

# 7、从类似9-2*5/3+7/3*99/4*2998+10*568/14的表达式中匹配出乘法或除法
content = "9-2*5/3+7/3*99/4*2998+10*568/14"
regx = "\d+(?:(?:[*]|/)\d+)+" # \d+(([*]|/)\d+)+
res = re.findall(regx, content)
print(res)