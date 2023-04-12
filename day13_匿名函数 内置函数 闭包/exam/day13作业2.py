# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/13 19:28
# 文件名称: day13.py
# 1.
# 都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：
#
# 1.
# 用map来处理字符串列表, 把列表中所有人都变成sb, 比方alex_sb

# name = ['alex', 'wusir', 'taibai']
# ret = list(map(lambda args: args+'_sb', name))
# print(ret)
#
# ret2 = [i+'_sb' for i in name]
# print(ret2)

# 执行结果：
# ['alex_sb', 'wusir_sb', 'taibai_sb']

# 1.
# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾

# l = [{'name': 'alex'}, {'name': 'y'}]

# ret = list(map(lambda args: args['name']+'sb', l))
# print(ret)

# 执行结果：
# ['alexsb', 'ysb']

# 1.
# 用filter来处理, 得到股票价格大于20的股票名字

# shares = {
#     'IBM': 36.6,
#     'Lenovo': 23.2,
#     'oldboy': 21.2,
#     'ocean': 10.2,
# }
#
# ret = list(filter(lambda args: shares[args] > 20, shares))
# print(ret)


# 执行结果：['IBM', 'Lenovo', 'oldboy']
# ```
#
# 1.
# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0, ......]

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# ret = map(lambda args: args['shares'] * args['price'], portfolio)
# print(list(ret))


# 执行结果：[9110.0, 27161.0, 4218.0, 1111.25, 735.7500000000001, 8673.75]

# 1.
# 还是上面的字典，用filter过滤出单价大于100的股票。

# ret = map(lambda args: args['name'], list(filter(lambda args: args['price'] > 100, portfolio)))
# print(list(ret)) # ['AAPL', 'ACME']

# ret = filter(lambda x: x['price'] > 100, portfolio)
# print(list(ret))
#
# 执行结果：[{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
# ```
#
# 1.
# 有下列三种数据类型，

l1 = [1, 2, 3, 4, 5, 6]
l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
tu = ('**', '***', '****', '*******')
# ```
#
# 写代码，最终得到的是（每个元祖第一个元素 > 2, 第三个 * 至少是4个。）
# `[(3, 'wusir', '****'), (4, '太白', '*******')]`
# 这样的数据。

# ret = filter(lambda args: args[0] > 2 and len(args[2]) >= 4, zip(l1, l2, tu))
# print(list(ret))


# ret = list(zip([i for i in l1 if i > 2], l2, [i for i in tu if len(i) >= 4]))
# print(ret) # [(3, 'oldboy', '****'), (4, 'alex', '*******')]


# 方法一：分着写
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# ret = zip(l1, l2, tu)
# li = list(ret)
# f = filter(lambda x: x[0] > 2 and len(x[2]) >= 4, li)
# print(list(f))
#
# 执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
# ```
#
# ```
# 方法二：方法一，不对ret进行list，直接迭代（迭代器一定是可迭代对象）
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# ret = zip(l1, l2, tu)
# f = filter(lambda x: x[0] > 2 and len(x[2]) >= 4, ret)
# print(list(f))
#
# 执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
# ```
#
# ```
# 方法三：将方法二合起来写
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')
# print(list(filter(lambda x: x[0] > 2 and len(x[2]) >= 4, zip(l1, l2, tu))))
#
# 执行结果：[(3, 'wusir', '****'), (4, '太白', '*******')]
# ```
#
# ```
#
# ​
#
#
#
# 1.
# 有如下数据类型(**实战题 **)：
l1 = [{'sales_volumn': 0},
      {'sales_volumn': 108},
      {'sales_volumn': 337},
      {'sales_volumn': 475},
      {'sales_volumn': 396},
      {'sales_volumn': 172},
      {'sales_volumn': 9},
      {'sales_volumn': 58},
      {'sales_volumn': 272},
      {'sales_volumn': 456},
      {'sales_volumn': 440},
      {'sales_volumn': 239}]

# 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。

# ret = sorted(l1, key=lambda args: args['sales_volumn'])
# print(list(ret))


# 执行结果：[{'sales_volumn': 0}, {'sales_volumn': 9}, {'sales_volumn': 58}, {'sales_volumn': 108}, {'sales_volumn': 172},
#           {'sales_volumn': 239}, {'sales_volumn': 272}, {'sales_volumn': 337}, {'sales_volumn': 396},
#           {'sales_volumn': 440}, {'sales_volumn': 456}, {'sales_volumn': 475}]


# 1.
# 求结果(**面试题 **)
#
# ​```python
# v = [lambda: x for x in range(10)]
#
# print(v)
#
# print(v[0])
#
# print(v[0]())
#
# 执行结果：
# [第1个函数地址, 第2个函数地址...第10个函数地址]
# 第1个函数地址
# 9
#
# 解释：
# v = [【lambda: x】 for x in range(10)]
# v是列表推导式，列表里里面有10个元素，每个元素是一个lambda函数的内存地址（输出x）（函数只有在调用时才执行，所以此时尚未执行）
# print(v[0])
# 时输出第1个函数内存地址，依然不执行
# print(v[0]())
# 此时函数才开始执行，x已变为9
# ```
#
# 1.
# 求结果(**面试题 **)
#
# ```
# v = (lambda: x for x in range(10))
#
# print(v)
#
# print(v[0])
#
# print(v[0]())
#
# print(next(v))
#
# print(next(v)())
#
# 执行结果：
# < generator
# object < genexpr > at
# 0x0000000002428308 >
# 报错
# 报错
# < function < genexpr >.< lambda > at 0x000000000242AC80 >
#                                 1
#
#                                 == == == == == == == == == == == == == == == == =
#                                 print(v)：生成器，v仅指向一个内存地址，未运行
#                                 print(v[0])：生成器尚未运行，没有v[0]，报错
#                                 print(v[0]())：生成器尚未运行，没有v[0]，报错
#                                 print(next(v))：第一个函数（输出的x为0）的内存地址
#                                 print(next(v)())：1，因为上一步已经执行了一个next，所以x从0变为1。为什么这题是1而上题是9？生成器表达式满足惰性机制一步一步执行，列表推导式是一次性全部执行
#                                 ```
#
#
#
#
#
#
#
#                                 map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])输出是什么? ( ** 面试题 ** )
#
#                                 答：输出一个生成器，输出的元素分别为'1'、'2'...'9'
#
#
#
#
#
#                                 13题：求结果：（ ** 面试题，比较难，先做其他题 ** ）
#
#                                 ```
#                                 def num():
# return [lambda x: i * x for i in range(4)]
# print([m(2) for m in num()])
#
# 执行结果：
# [6, 6, 6, 6]
# ```
#
# 14
# 题：有一个数组[34，1, 2, 5, 6, 6, 5, 4，3, 3]请写一个函数，找出该数组中没有重复的数
#
# 的总和（上面数据的么有重复的总和为1 + 2 = 3)(** 面试题 **)
#
# ```
# l = [34, 1, 2, 5, 6, 6, 5, 4, 3, 3]
# y = []
# for i in l:
#     y.extend(str(i))
# for j in range(len(y)):
#     y[j] = int(y[j])
# print(y)
# sum = 0
# for k in range(10):
#     if
# y.count(k) == 1:
# sum += k
# print(sum)
#
# 执行结果：
# [3, 4, 1, 2, 5, 6, 6, 5, 4, 3, 3]
# 3
# ```
#
#
#
#
#
#
#
#
#
#
#
#
#
# 1.
# 写一个函数完成三次登陆功能：
# - 用户的用户名密码从一个文件register中取出。
#
# - register文件包含多个用户名，密码，用户名密码通过 | 隔开，每个人的用户名密码占用文件中一行。
#
# - 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
#
# - 登陆成功返回True。
#
# ** 方法一：使用字典保存用户名、密码更好，详见day14作业第2题 **
#
# ** 方法二：每次输完都遍历搜索整个数据表，效率低 **
#
#                                        ```python
#
#
# def login():
#     code = 'qwer'
#     time_left = 3
#     while time_left >= 1:
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         your_code = input('请输入验证码：')
#         if your_code == code:
#             with open('register.txt', encoding='gbk') as f:
#                 for line in f:
#                     line = line.strip().split('|')
#                     if username == line[0].strip() and password == line[1].strip():
#                         print('登录成功')
#                         return True
#                 else:
#                     time_left = time_left - 1
#                     print('账号或者密码错误，您还剩%d次机会' % (time_left))
#         else:
#             print('验证码错误')
#     else:
#         print('您已输错三次')
#         return False
#
#
# login()
# ```
#
# 1.
# 再写一个函数完成注册功能：
# - 用户输入用户名密码注册。
# - 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# - 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# - 注册成功后，返回True, 否则返回False。
#
# ```python
#
#
# def register():
#     code = 'qwer'
#     while 1:
#         username = input('请输入用户名：').strip()
#         password = input('请输入密码：').strip()
#         your_code = input('请输入验证码：').strip()
#         if your_code == code:
#             with open('register.txt', encoding='gbk', mode='r+') as f:
#                 for line in f:
#                     line = line.strip().split('|')
#                     if username == line[0].strip():
#                         print('用户名已存在，请重新输入')
#                         break
#                 else:
#                     f.write(username + '|' + password)
#                     print('注册成功')
#                     return True
#         else:
#             print('验证码错误')
#
#
# register()
# ```
#
# 1.
# 用完成一个员工信息表的增删功能（ ** 选做题，有时间做，没时间周末做 **）。
#
# 文件存储格式如下：
#
# id，name，age，phone，job
#
# 1, Alex, 22, 13651054608, IT
#
# 2, 太白, 23, 13304320533, Tearcher
#
# 3, nezha, 25, 1333235322, IT
#
# 现在要让你实现两个功能：
#
# 第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。
#
# 第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除（删除后下面的id不变，比如此时你输入1，则将第一条数据删除，但是下面所有数据的id值不变，即太白，nezha的
# id不变）。
#
# ```python
#
#
# # 读取本地txt数据，输出字典组成的列表l，以及id最大值max_id
# # l的格式示例l=[{'id': '1', 'name': 'Alex', 'age': '22', 'phone': '13651054608', 'job': 'IT'}, {'id': '2', 'name': '太白', 'age': '23', 'phone': '13304320533', 'job': 'Tearcher'}, {'id': '3', 'name': 'nezha', 'age': '25', 'phone': '1333235322', 'job': 'IT'}]
# def get_information_list():
#     with open('员工信息表.txt', encoding='gbk') as f:
#         title = f.readline().strip()
#         title_list = title.split(',')
#         for i in range(len(title_list)):
#             title_list[i] = title_list[i].strip()
#         l = []
#         max_id = 0
#         for line in f:
#             dic = {}
#             line_list = line.strip().split(',')
#             for i in range(len(title_list)):
#                 # 当字段为id、age、phone时，将数据转化为int格式
#                 if i == 0 or i == 2 or i == 3:
#                     line_list[i] = int(line_list[i].strip())
#                 else:
#                     line_list[i] = line_list[i].strip()
#                 dic[title_list[i]] = line_list[i]
#                 # 计算到目前为止的id最大值
#                 if i == 0:
#                     max_id = max(max_id, line_list[i])
#             l.append(dic)
#     return l, max_id
#
#
# print(get_information_list())
#
#
# # 在文件末尾添加一条数据
# def add_data():
#     input_name = input('请输入姓名：').strip()
#     input_age = input('请输入年龄：').strip()
#     input_phone = input('请输入电话：').strip()
#     input_job = input('请输入工作：').strip()
#     information_list, max_id = get_information_list()
#     with open('员工信息表.txt', encoding='gbk', mode='a') as f:
#         line = f'{max_id + 1},{input_name},{input_age},{input_phone},{input_job}\n'
#         f.write(line)
#         print('添加成功！')
#
#
# # 输入id，将对应的这条数据从源文件中删除
# def delete_data():
#     import os
#     input_id = input('请输入要删除的id：').strip()
#     # 注意input_id不要转化成数字
#     with open('员工信息表.txt', encoding='gbk') as f1, open('员工信息表.txt.bak', encoding='gbk', mode='w') as f2:
#         for line in f1:
#             if line.startswith(input_id + ',') == False:
#                 f2.write(line)
#     os.remove('员工信息表.txt')
#     os.rename('员工信息表.txt.bak', '员工信息表.txt')
#     print('删除成功！')
#
#
# # 主程序
# while 1:
#     user_choice = input('1.增加数据\n2.删除数据\n3.退出程序\n请输入您的选择：').strip()
#     if user_choice == '1':
#         add_data()
#     elif user_choice == '2':
#         delete_data()
#     elif user_choice == '3':
#         print('程序退出！')
#         break
#     else:
#         print('您的输入有误，请重新输入')