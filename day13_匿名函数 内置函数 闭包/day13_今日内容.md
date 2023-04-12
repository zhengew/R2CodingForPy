# 匿名函数 内置函数 闭包

# 1.今日内容大纲
 - 如何学习
 - 一定要把预习加上
# 2.昨日内容回顾作业讲解
 - 生成器: 生成器就是迭代器，生成器是自己用python代码构建的
   - 1.生成器函数
   - 2.生成器表达式
   - 3.python内部提供的
 - 如何判断函数和生成器函数？
   - 函数内部是否有yield
   - yield return 区别
 - 吃包子案例：一个一个做和一次都做完的区别，节省内存开销
 - yield from: 将一个可迭代对象，变成一个生成器
 - 列表推导式,生成器表达式
   - 循环模式: [变量(加工后的变量) for 变量 in iterable]
   - 筛选模式: [变量(加工后的变量) for 变量 in iterable if 条件]
 - 内置函数: eval exec help callable


# 3.今日内容
 1.匿名函数：一句话函数，比较简单的函数。 
  - 此函数不是没有名字，他是有名字的，他的名字就是你给其设置的变量，比如func. 
  - lambda 是定义匿名函数的关键字，相当于函数的def. 
  - lambda 后面直接加形参，形参加多少都可以，只要用逗号隔开就行。 
  - 返回值在冒号之后设置，返回值和正常的函数一样,可以是任意数据类型。 
  - 匿名函数不管多复杂.只能写一行.且逻辑结束后直接返回数据
   ```python
   # 匿名函数返回2个数的和
   func1 = lambda a, b: a + b
   ret = func1(10, 20)
   print(func1, type(func1)) # <function <lambda> at 0x10c7400d0> <class 'function'>
   print(ret) # 30
   
   # 练习2
   func2 = lambda data: (data[0], data[2])
   ret = func2([1, 2, 3, 3])
   print(ret) # (1, 3)
   
   # 练习3        
   func3 = lambda a, b: a if a > b else b
   ret = func3(10, 5)
   print(ret) # 10
   ```
 2.内置函数
  - eval **
  - exec
  - help **
  - callable ***
  - int: 浮点数取整， 类型转换
  - float
  - bin: 十进制 -> 二进制
  - oct: 十进制 -> 八进制
  - hex: 十进制 -> 十六进制
  - divmod: 除数与被除数的结果 10 / 3 商3余1， divmod(10, 3) -> (3, 1)
  - round: 保留浮点数小数位数 round(3.345, 2) - > 3.35
  - pow: 
    - 求 x 的 y 次幂， pow(2, 3) -> 8
    - 求 x 的 y 次幂, 对 z 取余， pow(2, 3, 3) -> 2
  - bytes *** 编码转换
    -  bytes('中国', encoding='utf-8')
  - ord: 输入字符找到改字符编码的位置
    - ord('a') - > 97
  - chr: 输入位置数字找出其对应的字符 ***
    - char(97) -> a
  - repr: 返回一个对象的String形式(原形毕露) ***
    - s1 = '中国'
    - print(s1) # 中国
    - print(repr(s1)) # '中国'
  - all: 可迭代对象中，全都是True才是True
    - l1 = [1, 2, 3, '']
    - print(all(l1)) # False 有一个是False 就返回False
  - any: 可迭代对象中，又一个是True,就是True
    - l1 = [1, 2, 3, []]
    - print(any(l1)) # True

  - print
    - sep 分割符，默认空格
    - end 默认换行
  - list
    - list(可迭代对象)
    - list('abcd') -> ['a', 'b', 'c', 'd']
  - dict
    - 直接创建
    - dic = dict([(1, 'query'), (2, 'update')])
    - dic = dict(1 = 'query', 2 = 'update')
    - fromkeys
    - update

  - abc() 求绝对值
  - sum 求和
    - sum([1, 2, 3], 100) # 106, 可指定sum的初始值为100，再加上列表中的求和值
  - reversed
    - 获取的是反转的迭代器
    - obj = reversed([1, 2, 3])
    - print(list(obj)) # [3, 2 , 1]
  - zip 拉链方法,以最短的为准 ***
    - 参考创建字典的方式
    - command = dict(zip([1, 2, 3], ['query', 'update', 'delete']))
    - print(command) # {1: 'query', 2: 'update', 3: 'delete'}
  - 以下方法最重要
  - min 最小值
    ```python
    # 以绝对值的方式求最小值
    l1 = [33, 2, 1, 54, 7, -1, -9]
    ret = min(l1, key=abs)
    print(l1)
    ```
    -  注意：凡是可以加key的：它会自动的将可迭代对象中的每个元素按照顺序传入key对应的函数中，以函数返回值比较大小。
    ```python
    # 求最小值对应的键
    dic = {'a': 3, 'b': 2, 'c': 1}
    print(min(dic, key=lambda args: dic[args])) # c
    
    # 年龄最小的元组
    l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
    print(min(l2, key=lambda args: args[1])) # ('太白', 18)
    print(min(l2, key=lambda args: args[1])[0]) # 太白
    print(min(l2, key=lambda args: args[1])[1]) # 18
    ```
  - max: 同 min
  - sorted: 排序
    - 参数 reverse = True, 是否反转
    - 参数 key: 通过函数返回值排序
   ```python
   l2 = [('大壮', 76), ('雪飞', 70), ('纳钦', 94), ('张珵', 98), ('b哥',96)]
   # print(sorted(l2))
   print(sorted(l2,key= lambda x:x[1]))  # 返回的是一个列表，默认从低到高
   print(sorted(l2,key= lambda x:x[1],reverse=True))  # 返回的是一个列表，默认从低到高
   ```
  - filter 过滤 ****
    - 类似于列表推导式的筛选模式
    - 返回的是一个迭代器
   ```python
   l1 = [2, 3 ,4, 5, 7]
   ret = filter(lambda x: x > 3, l1) # 返回值是个迭代器
   print(list(ret)) # [4, 5, 7]
   ```
  - map ****
    - 类似于列表推导式的循环模式
    - 返回值也是一个迭代器
   ```python
   l1 = [1, 4, 9, 16, 25]
   ret = map(lambda x : x ** 2, range(1, 6))
   print(ret) # <map object at 0x1064da680>
   print(list(ret)) # [1, 4, 9, 16, 25]
   ```
  - reduce ***
    - 导包：from functools import reduce
    - 取出可迭代对象中的元素，调用返回返回值，在拿返回值及下一个元素依次作为实参传给函数
   ```python
   from functools import reduce
   def func(x, y):
       return x + y
   ret = reduce(func, [11, 2, 3, 4])
   print(ret) # 30
   ```
3.闭包
 - 封闭的东西，保证数据安全
 - 整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。
 - 闭包定义：
   - 1.闭包只能存在存在嵌套函数中
   - 2.内层函数对外城函数非全局变量的引用(使用)，就会形成闭包。
   - 被引用的非全局变量，也被称为自由变量，这个自由变量会与内层函数产生一个绑定关系。
   - 自由变量不会在内存中消失。
 - 闭包的作用：保证数据安全
 - 如何判断一个函数是不是闭包？
   - 嵌套函数
   - 内层函数对外层函数非全局变量的引用
 - 如何用代码判断是不是闭包？
   - ret.__code__.co_freevars
   ```python
   def get_avg():
    """
    闭包案例
    1.嵌套函数
    2.内层函数对外层函数非全局变量的引用
    3.引用的外层的非全局变量：被称为自由变量，自由变量不消失，保证数据安全
    :return: 
    """
    data = []
    def average(price: float):
        data.append(price)
        return sum(data) / len(data)
    return average

    ret = get_avg()
    
    avg1 = ret(10000.0)
    print(avg1) # 10000.0
    avg2 = ret(20000.0)
    print(avg2) # 15000.0
    
    print(ret.__code__.co_freevars) # ('data',) 自由变量 data
   ```
# 4.今日总结
 - 匿名函数
 - 内置函数 *** 一定记住， ** 尽量记住
 - 闭包

# 5.预习内容
- 装饰器