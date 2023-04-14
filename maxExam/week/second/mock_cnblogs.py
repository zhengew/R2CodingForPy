# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/17 21:35
# 文件名称: mock_cnblogs.py

""" 第二周函数综合作业 """
import sys
import os

def auth(function):
    """
    装饰器
    :param function:
    :return:
    """
    def inner(*args, **kwargs):
        if login_status['status'] == False:
            print("您尚未登录，无法进入相关页面～")
            login() # 登录不成功，系统将直接退出，因此只要能从这个函数出来，就一定登录成功
        ret = function(*args, **kwargs)
        return ret
    return inner

# 保存已注册用户的路径
PATH = 'register'

# 登录用户及登录状态
login_status = {'login_user': None, 'status': False}

def login():
    """
    登录模块
    三次登录认证，三次认证不通过，退出系统
    :param f:
    :return:
    """
    all_users = get_all_users(path=PATH)
    index = 3 # 三次登录
    while index > 0:
        name = input('请输入登录用户: ').strip()
        password = input('请输入密码: ').strip()
        if name in all_users and password == all_users.get(name):
            login_status['login_user'] = name
            login_status['status'] = password
            print(f'尊敬的{login_status["login_user"]},登录成功~')
            return
        else:
            index -= 1
            print(f'用户名或密码错误，请重新输入，剩余次数: {index}次' if index > 0 else '用户被锁定，请联系管理员解锁~')
    # 如果三次认证都不通过，退出程序
    sys.exit()

def init():
    """
    初始化提示语句
    :return:
    """
    info = """
    1.请登录
    2.请注册
    3.进入文章页面
    4.进入评论页面
    5.进入日记页面
    6.进入收藏页面
    7.注销账号
    8.退出整个程序
    """
    print(''.strip() if login_status['login_user'] else '欢迎访问博客园～'.center(50, '*') )
    print(info.replace(' ', '').strip())

def get_all_users(path: str):
    """
    获取已注册用户
    :return: all_users
    """
    all_users = dict()
    with open(path, encoding='utf-8') as f:
        for i in f:
            name, password = i.strip().split('|')
            all_users.setdefault(name, password)
        f.close()
    return all_users

def register(path: str):
    """
    注册用户
    a. 用户名、密码要记录在文件中。
    b. 用户名要求：只能含有字母或者数字不能含有特殊字符并且确保用户名唯一。
    c. 密码要求：长度要在6~14个字符之间。
    :return:
    """
    # 当前已注册用户
    curr_users = get_all_users(path=path)

    while 1:
        name = input('请输入用户名,字母或数字组成，区分大小写: ').strip()
        if name.isalnum():
            if name not in curr_users:
                while 1:
                    password = input('请输入密码,长度要在6~14个字符之间:').strip()
                    if 6 <= len(password) <= 14:
                        with open(path, mode='a', encoding='utf-8') as f:
                            f.write(f'{name}|{password}\n')
                            f.flush()
                            f.close()
                        print("用户注册成功～")
                        return
                    else:
                        print('密码长度要在6~14个字符之间，请重新输入～')
            else:
                print(f'用户名:{name}已被使用，请重新输入~')
        else:
            print('用户名只能由字母或数组组成，请重新输入～')

def write_article():
    """
    创建文章
    格式:文件名|文章内容
    按q退出
    :return:
    """
    while 1:
        article_info = input('请输入文件名及文件内容，使用"|"分隔，格式[文件名|文章内容]，按Q退出: ').strip()
        if article_info.strip().upper() == 'Q':
            break
        if '|' in article_info:
            file_name, file_content = article_info.split('|', 1)
            article_path = os.path.join((os.path.dirname(__file__) + os.sep + 'articles'), file_name)
            with open(article_path, mode='a', encoding='utf-8') as f:
                f.write(file_content)
                f.write('\n')
                f.flush()
                f.close()
            print(f'<<{file_name}>>创建成功~')
            return
        else:
            print('输入数据非法，文件名与文件内容需要以|分隔，请重新输入～')

def import_md_file():
    """
    导入md文件，生成新的.txt文件,按q退出
    :return:
    """
    while 1:
        md_file_path = input("请输入要导入的md文件路径:")
        if md_file_path.strip().upper() == 'Q':
            break
        dirs = os.listdir(os.path.dirname(__file__))
        if md_file_path in dirs:
            file_name = md_file_path.split('.')[0]
            article_path = os.path.join((os.path.dirname(__file__) + os.sep + 'articles'), file_name + '.txt')
            with open(md_file_path, encoding='utf-8') as f1, open(article_path, mode='w', encoding='utf-8') as f2:
                for content in f1:
                    f2.write(content)
                f2.flush()
                f2.close()
                f1.close()
            print(f'文章{md_file_path}导入成功，导入路径:{article_path}')
            return
        else:
            print(f'文件名:{md_file_path}不存在，请重新输入～')

@auth # article = auth(article)
def article():
    print(f'用户:{login_status["login_user"]}, 欢迎进入文章页面~'.center(50, '*'))
    commands = dict(zip(list('123'), ['创建文章', '导入md文件', '退出文章页面']))
    while 1:
        for k, v in commands.items():
            print(f'{k}: {v}')
        selected = input('请选择: ')
        match selected:
            case '1':
                write_article()
            case '2':
                import_md_file()
            case '3':
                print('退出文章页面～')
                return
            case _:
                print('输入错误，请重新输入')


def read_article(path):
    """
    读取文章
    :return:
    """
    with open(path, encoding='utf-8') as f:
        for i in f:
            print(i.strip())

@auth
def comment():
    # 敏感字列表
    sensitive_word = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
    print(f'用户:{login_status["login_user"]}, 欢迎进入评论页面~'.center(50, '*'))
    articles = os.listdir(os.path.dirname(__file__) + os.sep + 'articles')
    print(articles)

    while 1:
        for i in enumerate(articles, 1):
            id, article = i
            print(f'{id}: {article}')
        selected = input('请选择要评论的文章:').strip()

        if selected.strip().upper() == 'Q': break
        if selected.isdecimal():
            selected = int(selected)
        else:
            print("请输入数字～")
            continue
        if 0 < selected <= len(articles):
            article_path = os.path.dirname(__file__) + os.sep + 'articles' + os.sep + articles[selected-1]
            read_article(article_path) # 读取需要评论的文章
            with open(article_path, encoding='utf-8') as f1:
                contents = f1.read()
                f1.close()

            comment_flag = '\n评论区:\n-----------------------------------------'

            with open(article_path, mode='a', encoding='utf-8') as f2:
                if comment_flag not in contents:
                    f2.write(comment_flag + '\n')
                comments = input('请输入评论内容: ').strip()
                # 敏感字替换
                for i in sensitive_word:
                    comments = comments.replace(i, '*'*len(i))

                f2.write(f'(用户名){login_status["login_user"]}:\n')
                f2.write('评论内容:')
                f2.write(comments+'\n\n')
                f2.flush()
                f2.close()
        else:
            print(f'输入数据非法，请输入[1~{len(articles)}]之间的数字~')


@auth
def diary():
    print(f'用户:{login_status["login_user"]}, 欢迎进入日记页面~'.center(50, '*'))
@auth
def favorite():
    print(f'用户:{login_status["login_user"]}, 欢迎进入收藏页面~'.center(50, '*'))
@auth # logout = auth(logout)
def logout():
    print(f'用户:{login_status["login_user"]}, 欢迎再次使用，注销成功~'.center(50, '*'))
    login_status['login_user'] = None
    login_status['status'] = False
    return

def exit():
    """
    退出系统
    :return:
    """
    print(f'用户:{login_status["login_user"]}, 退出系统，欢迎再次访问博客园~' if login_status['login_user'] else "退出系统～")
    sys.exit()


def start():
    """
    主程序
    :return:
    """
    commands = dict(zip(list(range(1, 9)), [login, register, article, comment, diary, favorite, logout, exit]))
    while 1:
        # 首页用户选择页面
        init()
        selected = input('请选择:').strip()
        if selected.isdigit() and 1 <= int(selected) <= 8:
            selected = int(selected)
            match selected:
                case 1:
                    commands[selected]()
                case 2:
                    commands[selected](path=PATH)
                case 3:
                    commands[selected]()
                case 4:
                    commands[selected]()
                case 5:
                    commands[selected]()
                case 6:
                    commands[selected]()
                case 7:
                    commands[selected]()
                case 8:
                    commands[selected]()
        else:
            print("输入错误，请重新选择～")
def main():
    start()

if __name__ == '__main__':
    main()