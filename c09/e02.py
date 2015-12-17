#! /usr/bin/python3
# -*- coding:utf8 -*-

"""
写个表达式，修改元组中第一个元素。在此过程中，（4,5,6）应该变成（1,5,6）。

答：由于元组具有不可变性，因此不能在原处修改元素，可以利用分片运算和合并运算完成，或者将元组转换成列表，修改后再转换成元组。
"""

#Answer

T = (4,5,6)
T1 = (1,)+T[1:]
print("利用切片合并的方法修改：",T1)

tmp = list(T)
tmp[0] = 1
T2 = tuple(tmp)
print("利用转换为列表的方法修改：",T2)