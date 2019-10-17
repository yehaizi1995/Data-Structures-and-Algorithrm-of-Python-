#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/10/17:19:38

# 双端队列

class Dqueue(object):
    def __init__(self):
        self._list=[]

    # 从队头加入一个item元素
    def add_front(self,item) :
        self._list.insert(0,item)

    # 从队尾加入一个item元素
    def add_rear(self,item) :
        self._list.append(item)

    # 从队头删除一个item元素
    def remove_front(self):
        return self._list.pop(0)

    # 从队尾删除一个item元素
    def remove_rear(self):
        return self._list.pop()

    #  判断双端队列是否为空
    def is_empty(self):
        return self._list==[]

    # 返回队列的大小
    def size(self):
        return len(self._list)

if __name__ == "__main__":
    q = Dqueue()
    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    print(q.remove_front())
    print(q.remove_front())
    print(q.remove_front())