# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 22:02
# 文件名称: 待参数的装饰器.py

# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 20:46
# 文件名称: 装饰器_demo1.py

"""
1. 写一个函数完成三次登陆功能：
   - 用户的用户名密码从一个文件register中取出。
   - register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
   - 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
   - 登陆成功返回True。

     **方法一：使用字典保存用户名、密码更好，详见day14作业第2题**

     **方法二：每次输完都遍历搜索整个数据表，效率低**
"""

login_status = {'status': False}
def getUserInfo(path):
    users = {}
    with open(path, encoding='utf-8') as f:
        for i in f:
            name, pwd = i.strip().split('|')
            users.setdefault(name, pwd)
    return users

users = getUserInfo("register")
print(users, type(users))

def auth2(x):
    def auth(func):
        def inner(*args, **kwargs):
            for i in range(3):
                name = input("用户名:").strip()
                pwd = input("密码：").strip()
                if x == 'QQ':
                    if name in users and pwd == users[name]:
                        login_status['status'] = True
                        return func()
                elif x == 'wechat':
                    if name in users and pwd == users[name]:
                        login_status['status'] = True
                        return func()
                else:
                    print(f"用户名或密码错误，剩余{3-i-1}次" if (3-i-1) != 0 else f"用户被锁定!")

        return inner
    return auth

@auth2('wechat') # auth2('wechat') = auth(index)
def index():
    print("欢迎进入系统首页")

ret = index()

if login_status.get('status'):
    print("登录成功")
else:
    print("登录失败")
