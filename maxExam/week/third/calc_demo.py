# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/29 20:16
# 文件名称: calc_demo.py

"""
通过re模块实现计算器四则运算
# (1+2)*3/4
# 计算乘法(表达式):
   # 记录日志:计算乘法表达式是什么,结果是什么
   # return
# 计算除法
    # 记录日志:表达式是什么,结果是什么
   # return
# 计算小括号内的
# 计算加法
# 计算减法
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))
"""

import re
import logging

# 日志级别
logging.basicConfig(level=logging.DEBUG)

# 正则表达式
mul_and_div_regex = "(\d+(?:\.\d+)?)([*]|[/])([-]?\d+(?:\.\d+)?)"
add_and_sub_regex = "(-?\d+(?:\.\d+)?)([-]|[+])(-?\d+(?:\.\d+)?)"
inner_bracket_regex = "[(]([^()]+)[)]"
def cal_mul_and_div(regex: str, expression: str):
    """
    乘法和除法
    :param regex: 正则
    :param expression: 表达式
    :return: 计算结果
    """
    expression = re.sub("\s", "", expression) # 表达式去空白
    while '*' in expression or '/' in expression:
        ret = re.search(regex, expression)
        if ret.group(2) == '*':
            result = str(float(ret.group(1)) * float(ret.group(3)))
        elif ret.group(2) == '/':
            result = str(float(ret.group(1)) / float(ret.group(3)))
        # 打印表达式执行结果
        logging.debug(f'计算乘法和除法： {ret.group(1)} {ret.group(2)} {ret.group(3)} == {result}')
        expression = expression.replace(ret.group(0), result)
    return expression

def cal_add_and_sub(regex: str, expression: str):
    """
    加法和减法
    :param regex: 乘法
    :param expression: 表达式
    :return: 计算结果
    """
    expression = re.sub("\s", "", expression) # 表达式去空白
    while re.findall('-?(\d+(?:\.\d+)?[-+])', expression):
        ret = re.search(regex, expression)
        if ret.group(2) == '+':
            result = str(float(ret.group(1)) + float(ret.group(3)))
        elif ret.group(2) == '-':
            result = str(float(ret.group(1)) - float(ret.group(3)))
        expression = expression.replace(ret.group(0), result)
        # 打印表达式执行结果
        logging.debug(f'计算加法和减法： {ret.group(1)} {ret.group(2)} {ret.group(3)} == {result}')
    return expression

def cal_inner_bracket(regex: str, expression: str):
    """
    小括号内的表达式
    :param regex:
    :param expression:
    :return:
    """
    bracket_flag = re.findall('[()]', expression)
    while bracket_flag:
        expression = re.sub("\s", "", expression)  # 表达式去空白
        ret = re.finditer(regex, expression)
        for i in ret:
            inner_exp = i.group(1)
            ret1 = cal_mul_and_div(mul_and_div_regex, inner_exp)
            ret2 = cal_add_and_sub(add_and_sub_regex, ret1)
            expression = expression.replace(i.group(), ret2)
        bracket_flag = re.findall('[()]', expression)
        # print(expression)
    return expression

def run(expression: str):
    """
    四则运算主程序
    :param expression:
    :return:
    """
    exp_inner = cal_inner_bracket(inner_bracket_regex, expression)
    exp_mul_div = cal_mul_and_div(mul_and_div_regex, exp_inner)
    result = cal_add_and_sub(add_and_sub_regex, exp_mul_div)
    return result


if __name__ == '__main__':
    exp = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))"
    result = 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))
    ret = run(exp)
    print(ret, result, ret==str(result))
