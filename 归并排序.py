#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/9/3:15:23

# 归并排序：首先需要把序列全部拆分，拆分到最后只有一个元素，不可拆分即可。最后再按拆分顺序
# array=[1,2,3,4,8,9,7,5,6,10,12]
# a=len(array)
# b=a//2
# print(b)
# print(array[5])
# print(array[:b])
# print(array[b:])

# 第一步：拆分过程
def merge_sort(array):
    n=len(array)
    if n<=1:
        return
    mid=n//2
    merge_sort(array[:mid])
    merge_sort(array[mid:])