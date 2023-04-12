# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 16:35
# 文件名称: 注册登录练习.py

# 登录程序
import json
import hashlib

def get_md5(username, password):
    m = hashlib.md5(username.encode('utf-8'))
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def register():
    name = input('请输入用户名:').strip()
    password = input('请输入密码:').strip()

    md5_str = get_md5(name, password)
    with open('register.txt', mode='at', encoding='utf-8') as f:
        f.write(json.dumps({'name': name, 'password': password, 'md5': md5_str}) + '\n')
        f.flush()
        f.close()

    print('恭喜您，注册成功~')


def login():
    name = input("用户名:").strip()
    pwd = input('密码:')
    md5_value = get_md5(name, pwd)
    with open('register.txt', mode='rt', encoding='utf-8') as f:
        for i in f:
            user = json.loads(i.strip())
            if name == user['name'] and md5_value == user['md5']:
                print('登录成功')
                return True

    print('登录失败，用户名或密码错误')
    return False

def main():
    # register()
    login()

if __name__ == '__main__':
    main()
