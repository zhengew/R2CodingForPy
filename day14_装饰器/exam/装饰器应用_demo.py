# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/14 06:50
# 文件名称: 装饰器应用_demo.py

# 装饰器的应用：登录认证
# 这周的周末作业：模拟博客园登录的作业。装饰器的认证功能。

PATH = 'register'
def get_users_info(path: str):
    """
    已注册用户信息
    :param path:
    :return: users: dict, 字典形式放回 用户信息
    """
    users = {}
    with open(path, encoding='utf-8') as f:
        for i in f:
            name, password = i.strip().split('|')
            users.setdefault(name, password)
        f.close()
    return users

# 登录状态
status_dict = {
    'username': None,
    'status': False,
}

def login():
    """
    登录模块，3次登录失败，账户锁定
    :return: login_status: True / False
    """
    users = get_users_info(PATH) # 用户信息
    index = 3 # 剩余次数
    login_status = False # 登录状态，默认False
    while index > 0:
        login_name = input('请输入用户名:').strip()
        login_pwd = input('请输入密码:').strip()
        if login_name in users and login_pwd == users[login_name]:
            login_status = True
            status_dict['username'] = login_name
            status_dict['status'] = login_status
            break
        else:
            index -= 1
            print(f'用户名或密码错误，剩余次数:{index}' if index > 0 else "用户被禁用，请联系管理员解锁～")

    return login_status

def register():
    return

def auth(f):
    '''
    你的装饰器完成：访问被装饰函数之前，写一个三次登录认证的功能。
    登录成功：让其访问被装饰得函数，登录没有成功，不让访问。
    :param f:
    :return:
    '''
    def inner(*args,**kwargs):
        if status_dict['status']:
            ret = f(*args, **kwargs)
            return ret
        else:
            if login():
                ret = f(*args, **kwargs)
                return ret
    return inner

@auth
def article():
    print('欢迎访问文章页面')
@auth
def comment():
    print('欢迎访问评论页面')
@auth
def dariy():
    print('欢迎访问日记页面')

def main():
    print(status_dict)
    article()  # inner()
    print(status_dict)
    comment()
    dariy()

if __name__ == '__main__':
    main()