# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/12 21:33
# 文件名称: 简单的装饰器demo.py

"""
装饰器模拟博客园登录
"""
user = {'test1': '123456', 'test2': '123456'}

def auth(func):
    def inner(*args, **kwargs):
        for i in range(3):
            name = input("用户名:").strip()
            pwd = input("密码：").strip()
            if name in user and pwd == user[name]:
                func()
                return
            else:
                print(f"用户名或密码错误，剩余{3-i-1}次" if (3-i-1) != 0 else f"用户被锁定!")
    return inner

@auth
def index():
    print("欢迎登录首页")

print('test1' in user)
index()