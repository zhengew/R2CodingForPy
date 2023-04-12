# 回顾
 - 自定义模块
 - 模块的两种执行方法
 - '__name__' '__file__' '__all__'
 - 模块导入的多种方式
 - 相对导入
 - random
   - random.random(): [0.0, 1.0)之间的小数
   - random.uniform(a, b): [a, b)的浮点数
   - random.randint(a, b): [a, b)的任意整数
   - random.shuffle(可变的数据类型)：洗牌，打散顺序
   - random.sample(x, k): 从可迭代对象x中取k个元素

# 今日内容
## 常用模块的介绍
- time, datetime
- os, sys
- hashlib, json, pickle, collections

## time: 和时间相关
- 封装了获取时间戳和字符串形式的时间的一些方法
- 

## json模块
 - JavaScript Object Notation: java脚本对象标记语言
 - 一种简单的数据交换格式

# json 和 pkckle 的比较
```python
json:
1.不是所有数据类型都可以序列化，结果是字符串
2.不能多次对同一个文件序列化
3.json 数据可以跨语言

pickle:
1.所有的python数据类型都可以序列化，结果是字节串
2.可以多次对同一个文件序列化
3.不能跨语言
```


### 序列化
 - 序列化：将内存中的数据，转换成字节串，用以保存在文件或通过网络传输，称为序列化过程
 - 反序列化：从文件中或网络中获取的数据，转化成内存中原来的数据类型，称为反序列化过程

## hashlib模块
 - 封装一些用于加密的类
 - md5() ...
 - 加密的目的:用于判断和验证,而并非解密
 - 特点：
   - 把一个大的数据，切分成不同块，分别对不同的块进行加密，在汇总的结果，和直接对整体数据加密的结果是一致的。
   - 单项加密，不可逆
   - 原始数据的一点小的变化，将导致结果的非常大的差异，雪崩效应。

# 总结
 - 自定义模块
 - random
 - time
 - datetime
 - os
 - sys
 - json, pickle
 - hashlib
 - collections : 容器类
   - nametuple
   - defaultdict
   - Counter
