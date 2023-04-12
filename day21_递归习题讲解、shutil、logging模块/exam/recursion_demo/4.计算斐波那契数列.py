"""
目标：计算斐波那契数列
继续理解函数的值传递，函数的返回值
"""

# 循环
def loop_feibo(n: int):
    """
    循环模式计算
    :param n:
    :return:
    """
    a, b = 1, 1
    if n == 1 or n == 2:
        return b
    else:
        while n > 2:
            a, b = b, a+b
            n -= 1
        return b

# 递归
def feibo(n: int, a=1, b=1):
    """
    计算第n个斐波那契数  1 1 2 3 5 8 13 21..
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a+b
        return feibo(n-1, a, b)


"""
递归执行步骤

def feibo(5: int, a=1, b=1):
    if 5 == 1 or 5 == 2:
        return b
    else:
        a, b = 1, 1+1
        return feibo(n-1, a, b) # feibo(5-1, 1, 1+1) -> feibo(n=4, a=1, b=2) ; 最外层函数结束，返回值返回给递归函数调用方

def feibo(4: int, a=1, b=2):
    if 4 == 1 or 4 == 2:
        return b
    else:
        a, b = 2, 1+2
        return feibo(n-1, a, b) # feibo(4-1, 2, 3) -> feibo(n=3, a=2, b=3) ; b = 5


def feibo(3: int, a=2, b=3):
    if n == 1 or n == 2:
        return b
    else:
        a, b = 3, 2+3
        return feibo(n-1, a, b) # feibo(3-1, 3, 5) -> feibo(n=2, a=3, b=5) ; 此时n=2,向上return返回值 b=5
        

def feibo(n: int, a=1, b=1):
    if n == 1 or n == 2:
        return b
    else:
        a, b = b, a+b
        return feibo(n-1, a, b)


ret = feibo(5)
"""


# 通过yield 生成器，生成1~n个非波那契数列
def feibo_yield(n: int):
    a, b = 1, 1
    if n == 1:
        yield 1
    else:
        yield from (1, 1)
        while n > 2:
            a, b = b, a+b
            yield b
            n -= 1




if __name__ == '__main__':
    ret = loop_feibo(8)
    print(ret)

    ret = feibo(8)
    print(ret)

    ret = feibo_yield(8)
    print(list(ret))