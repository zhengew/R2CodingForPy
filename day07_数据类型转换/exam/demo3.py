# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/6 21:36
# 文件名称: demo3.py

"""
根据车牌区域划分，计算各个省份车牌持有量
车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (**选做题**)
cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041'.....]
locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南'.....}
结果: {'黑龙江':2, '山东': 1, '北京': 1}
"""
cars = ['鲁A32444','鲁B12333','京B8989M','黑C49678','黑C46555','沪B25041', '鄂A88888']
locals = {'沪':'上海', '黑':'黑龙江', '鲁':'山东', '鄂':'湖北', '湘':'湖南', "京": "北京"}

# result = dict().fromkeys(list(locals.values()), 0)
#
# for car in cars:
#     for key in locals:
#         if car.strip()[0] == key:
#             result[locals[key]] += 1
#
# print(result)

# 方式二
dic = {}
for car in cars:
    if locals[car[0]] not in dic:
        dic[locals[car[0]]] = 1
    else:
        dic[locals[car[0]]] += 1
print(dic)


# 方式三 用 get 判断

# dic = {}
# for car in cars:
#     dic[locals[car[0]]] = dic.get(locals[car[0]], 0) + 1
# print(dic)