# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/507:54
# 文件名称: switch_case.py

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(300))

selected = input("请选择:")
match selected:
    case "1":
        print("case1")
    case "2":
        print("case2")
    case _:
        print("默认case")


