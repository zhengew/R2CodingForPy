import re

exp= '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
print(exp)
# 先匹配小括号里的内容
# 然后先计算乘除法
# 再计算加减法

# 用循环用正则
# 调用函数

def get_bracket_exp(s):
    """
    匹配首个最内层小括号
    :return:
    """
    regx = "[(]([^()]+)[)]"
    ret = re.search(regx, s)
    return ret.group(1)

def tow_num_cal(s):
    """
    给定str格式的两个数字字符串[可能是整数或小数，正数或负数]组成的四则运算表达式，返回float型的计算结果
    :param s: str格式的四则运算
    :return: float型的计算结果
    """
    regx = "([-+]?\d+(?:\.\d+)?)([-+*/])([-+]?\d+(?:\.\d+)?)"
    ret = re.search(regx, s)
    print(ret.group(2))

    if ret.group(2) == '+': return float((ret.group(1))) + float((ret.group(3)))
    elif ret.group(2) == '-': return float((ret.group(1))) - float((ret.group(3)))
    elif ret.group(2) == '*': return float((ret.group(1))) * float((ret.group(3)))
    elif ret.group(2) == '/': return float((ret.group(1))) / float((ret.group(3)))







if __name__ == '__main__':
    ret = get_bracket_exp(exp)
    print(ret)
    res = tow_num_cal(ret)
    print(res)





