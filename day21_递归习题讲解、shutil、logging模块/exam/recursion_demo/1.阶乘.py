"""
目标：理解阶乘的调用步骤
"""
def func(n: int):
    """
    计算 1～n的阶乘
    :param n:
    :return:
    """
    if n == 1:
        return n
    else:
        return n * func(n - 1)

ret = func(5)
print(ret) # 120

"""
# 执行步骤

def func(5): # 第一层 n = 5
    if 5 == 1:
        return n
    else:
        return 5 * func(5 - 1) # return 5 * func(4)   注意：此时就要开始调用func本身了  # 递归返回 return 5 * 4 3 * 2 * 1, 此时最外层函数也执行完毕了，结果返回给递归调用方
        
  def func(4):
    if 4 == 1:
        return n
    else:
        return 4 * func(4 - 1) # return 4 * func(3)  # 递归返回 return 4 * 3 * 2 * 1
        
def func(3):
    if 3 == 1:
        return n
    else:dbnq
    7
        return 3 * func(3 - 1) # return 3 * func(2) # 递归返回 return 3 * 2 * 1
        
def func(2):
    if 2 == 1:
        return n
    else:
        return 2 * func(2 - 1) # return 2 * func(1) #  递归返回  return 2 * 1
        
def func(1):
    if 1 == 1:
        return n # 此时 n == 1: retrun 1  本层递归执行结束，返回上一层，返回值给上一曾的 func(1)
    else:
        return n * func(n - 1)
      
"""