# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/19 16:13
# 文件名称: md5_demo.py

"""
md5加密算法

给一个数据加密的三大算法：
1.获取一个加密对象
2.使用加密对象的update方法，进行加密
3.通过hexdigest获取加密结果，或者digest方法

"""
import hashlib

# 获取一个加密对象
m = hashlib.md5()

# 使用加密对象的update，进行加密
m.update('abc中文'.encode('utf-8'))
m.update('def'.encode('utf-8'))
# 通过hexdigest获取加密结果
res = m.hexdigest() # 2f1b6e294e72d25ae196fe4ac2d27de6
# res = m.digest() # b'/\x1bn)Nr\xd2Z\xe1\x96\xfeJ\xc2\xd2}\xe6'
print(res)


# 给一个数据加密
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同，如果不相同，说明原文不同

# 不同加密算法：实际上就是加密结果数据长度不同
m = hashlib.sha224()
m.update(b'abc')
print(len(m.hexdigest())) # 56

print(len(hashlib.md5().hexdigest())) # 32

# 在创建加密对象时，可以指定参数，称为salt(加盐)

m = hashlib.md5(b'abc')
print(m.hexdigest()) # 900150983cd24fb0d6963f7d28e17f72

m1 = hashlib.md5()
m1.update(b'abc')
print(m1.hexdigest()) # 900150983cd24fb0d6963f7d28e17f72