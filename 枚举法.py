#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/8/30:16:29

# 例子1 a+b+c=1000,a**2+b**2=c**2,求abc的所有组合
# 法1：
# import time
# start_time=time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print('a,b,c:%d,%d,%d',a,b,c)
# end_time=time.time()
# print('times:%d'% (end_time-start_time))
# print('finish')

# 法2：

# import time
# start_time=time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         c=1000-a-b
#         if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#             print('a,b,c:%d,%d,%d',a,b,c)
# end_time=time.time()
# print('times:%d'% (end_time-start_time))
# print('finish')


# def sum_late(*args):
#     def calc_sum():
#         ax=0
#         for n in args:
#             ax=ax+n
#         return ax
#     return calc_sum()
# print('result:',sum_late(1,2,3,4))

# def sum():
#     fs=[]
#     def sum_late():
#         for i in range(1,4):
#             return i*i
#         fs.append(sum_late())
#     print('result:',fs)
#
# sum()
#
# class Myclass(object):
#     i=123
#     def __init__(self,name,score):
#         self.score=score
#         self.name=name
#     def info(self):
#         print('xuesheng:%s;score:%s'%(self.score,self.name))
#
# a=Myclass('xiaomin',100)
# print(a.score)
# a.info()

# import numpy as np
# a=np.array([[1,2,3,5],[4,5,6,5],[7,8,9,5]])
# print(len(a))
# print(len(a[0]))
#
# class Solution(object):
#     def Find(self,target,array):
#         for i in range(len(array)):
#             for j in range(len(array[0])):
#                 if target==array[i][j]:
#                     print(True)
#                     print(i,j)
#
# a=Solution()
# a.Find(10,[[12,10,13],[19,12,18],[45,85,20]])


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # 法1：return s.replace(" ","%20")
        d=' '
        for i in range(len(s)):
            if s[i]==' ':
                d=d+'%20'
            else:
                d=d+s[i]
        return d
a=Solution()
print(a.replaceSpace('we are family'))