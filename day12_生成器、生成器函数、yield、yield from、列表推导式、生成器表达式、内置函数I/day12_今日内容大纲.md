# 1.今日内容大纲
1.毒鸡汤

2.生成器
 - yield
 - yield return
 - yield from
 - 
3.生成器表达式, 列表推导式

4.内置函数I

# 2.昨日内容回顾作业讲解
1.可迭代对象：
- 可以更新迭代的实实在在的值
- 内部含有'__iter__'方法的
- str, list, tuple, dict, set, range
- 优点：操作方法多，操作灵活，直观
- 缺点：占用内存

2.迭代器
- 可以更新迭代的一个工具(数据结构)
- 内部含有'__iter__' 和 '__next__'方法的
- 文件句柄
- 优点：节省内存，惰性机制
- 缺点：不直观，速度相对慢，操作方法单一，不走回头路。
3.格式化输出
4.函数名的应用
5.默认参数是可变的数据类型的坑；作用域的坑；

# 3.今日内容
1.生成器
 - 生成器:python社区，生成器与迭代器看成是一种，生成器的本质就是迭代器， 唯一的区别：生成器是我们用python代码构建的数据结构。迭代器是提供的或者转化得来的。
   - 获取生成器的三种方式：
     - 生成器函数
     - 生成器表达式
     - python内部提供的一些
   - 生成器函数获取生成器：
    ```python
    def gen_buns2(number: int):
        for i in range(number):
            yield f'{i+1}号包子'

    ret = gen_buns2(2000)
    print(ret) # <generator object gen_buns2 at 0x104e21690>
    
    for i in range(200):
        print(ret.__next__())
    
    for i in range(200):
        print(ret.__next__())
    ```
 - yield
 - yield return
 - yield from: 依次返回可迭代对象中的每个元素
    ```python
    def gen_demo(data:list):
        yield from data

    ret = gen_demo([1, 2, 3, 4])
    for i in range(4):
        print(ret.__next__())
    ```

2.生成器表达式, 列表推导式
 - 用一行代码构建一个比较复杂且有规律的列表
 - 列表推导式分为2中模式：
   - 循环模式: [变量(加工后的变量) for 变量 in iterable]
   - 筛选模式: [变量(加工后的变量) for 变量 in iterable if 条件]
   - 生成器遇到 next, list 或 生成器外的for才会执行，否则代码在内存中保存不执行
   - 

3.内置函数I

# 4.今日总结
1. 生成器
2. 生成器函数 yield
3. yield 与 return 的区别， yield from
4. 列表推导式，生成器表达式
5. 内置函数：今天讲的内置函数了解
   - callable 是否可调用
   - help 帮助
   - eval 剥去字符串外衣运算里面的代码，又返回值(了解)
   - exec 代码流， 运算多行字符串里的代码

# 5.预习内容
1. lambda 表达式
2. 内置函数II
3. 闭包
4. 后天讲装饰器