# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/4/1 20:02
# 文件名称: user_demo.py

import os
import logging
logging.basicConfig(level=logging.DEBUG)

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_pwd(self):
        """
        修改用户密码
        :param new_pwd:
        :return:
        """
        oldpwd = input("原密码: ")
        newpwd = input("新密码: ")
        change_YN = False # 是否修改成功
        if oldpwd == self.password:
            with open('userinfo', encoding='utf-8') as f1, open('userinfo_back', mode='wt', encoding='utf-8') as f2:
                for i in f1:
                    name, pwd = i.strip().split('|')
                    if name == self.username:
                        f2.write(f"{name}|{newpwd}\n")
                        change_YN = True
                    else:
                        f2.write(i)
                f2.flush()
                f2.close()
                f1.close()
            os.remove('userinfo')
            os.rename('userinfo_back', 'userinfo')
            logging.debug(f"newpwd: {newpwd}, oldpwd: {oldpwd}")
        return change_YN



def login(login_name, password):
    """
    用户登录
    :param login_name: 登录用户名
    :param password: 登录用户密码
    :return: True/False 返回登录成功或失败
    """
    with open('userinfo', encoding='utf-8') as f:
        for i in f:
            name, pwd = i.strip().split('|')
            if name == login_name and pwd == password:
                return True
    return False


def main():
    while True:
        name = input("用户名: ")
        pwd = input("密码: ")
        if login(name, pwd):
            obj = User(name, pwd)
            ret = obj.change_pwd()
            if ret:
                print('密码修改成功～')
                break
            else:
                print('原密码输入错误，修改失败～')
        else:
            print("登录失败，用户名或密码错误～")

if __name__ == '__main__':
    main()