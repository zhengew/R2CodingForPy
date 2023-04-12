# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/22 07:38
# 文件名称: 模版.py

status_dic = {
    'username': None,
    'status': False,
}
flag = True


def login():
    i = 0
    with open('register', encoding='utf-8') as f1:
        dic = {i.strip().split('|')[0]: i.strip().split('|')[1] for i in f1}
    while i < 3:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        if username in dic and dic[username] == password:
            print('登录成功')
            return True
        else:
            print('用户名密码错误，请重新登录')
            i += 1


def register():
    with open('register', encoding='utf-8') as f1:
        dic = {i.strip().split('|')[0]: i.strip().split('|')[1] for i in f1}
    while 1:
        print('[1;45m 欢迎来到注册页面 [0m')
        username = input('请输入用户名：').strip()
        if not username.isalnum():
            print('[1;31;0m 用户名有非法字符，请重新输入 [0m')
            continue
        if username in dic:
            print('[1;31;0m 用户名已经存在，请重新输入 [0m')
            continue
        password = input('请输入密码：').strip()
        if 6 <= len(password) <= 14:
            with open('register', encoding='utf-8', mode='a') as f1:
                f1.write(f'\n{username}|{password}')
            status_dic['username'] = str(username)
            status_dic['status'] = True
            print('[1;32;0m 恭喜您，注册成功！已帮您成功登录~ [0m')
            return True
        else:
            print('[1;31;0m 密码长度超出范围，请重新输入 [0m')


def auth(func):
    def inner(*args, **kwargs):
        if status_dic['status']:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('[1;31;0m 请先进行登录 [0m')
            if login():
                ret = func(*args, **kwargs)
                return ret

    return inner


@auth
def article():
    print(f'[1;32;0m 欢迎{status_dic["username"]}访问文章页面[0m')


@auth
def diary():
    print(f'[1;32;0m 欢迎{status_dic["username"]}访问日记页面[0m')


@auth
def comment():
    print(f'[1;32;0m 欢迎{status_dic["username"]}访问评论页面[0m')


@auth
def enshrine():
    print(f'[1;32;0m 欢迎{status_dic["username"]}访问收藏页面[0m')


def login_out():
    status_dic['username'] = None
    status_dic['status'] = False
    print('[1;32;0m 注销成功 [0m')


def exit_program():
    global flag
    flag = False
    return flag


choice_dict = {
    1: login,
    2: register,
    3: article,
    4: diary,
    5: comment,
    6: enshrine,
    7: login_out,
    8: exit_program,
}

while flag:
    print('''
    欢迎来到博客园首页
    1:请登录
    2:请注册
    3:文章页面
    4:日记页面
    5:评论页面
    6:收藏页面
    7:注销
    8:退出程序''')

    choice = input('请输入您选择的序号:').strip()
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(choice_dict):
            choice_dict[choice]()
        else:
            print('[1;31;0m 您输入的超出范围，请重新输入 [0m')

    else:
        print('[1;31;0m 您您输入的选项有非法字符，请重新输入 [0m')