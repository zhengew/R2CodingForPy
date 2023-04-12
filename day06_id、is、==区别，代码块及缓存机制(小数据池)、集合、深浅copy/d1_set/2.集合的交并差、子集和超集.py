# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 21:00
# 文件名称: 2.集合的交并差、子集和超集.py

"""
目标：学习集合交集、并集、差集
交集：& 或者 intersection
并集：| 或者 union
差集：- 或者 difference
反交集：^ 或者 symmetric_difference

子集：<
超集：>
"""

set1 = {1, 2, 3, 7}
set2 = {1, 2, 3, 4, 5, 6}

# 1.交集 &
print(set1 & set2) # {1, 2, 3}
print(set1.intersection(set2)) # {1, 2, 3}

# 2.并集
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7}

# 3.差集
print(set1 - set2) # {7}
print(set1.difference(set2)) # {7}

# 4.反交集
print(set1 ^ set2) # {4, 5, 6, 7}
print(set1.symmetric_difference(set2)) # {4, 5, 6, 7}


# 子集
set3 = {1, 2, 3}
set4 = {1, 2, 3, 4, 5, 6, }
print(set3 < set4) # True

# 超集
print(set4 > set3) # True