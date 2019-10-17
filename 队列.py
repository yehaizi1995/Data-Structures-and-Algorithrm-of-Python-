#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/10/17:19:15

# 队列


class Queue(object):
    def __init__(self):
        self._list=[]


    # 往队列中添加一个item元素
    def enqueue(self,item):
        return self._list.append(item)    # 添加进去就好了 不用返回


    # 从队列头部删除一个元素
    def dequeue(self):
        return self._list.pop(0)

    # 判断一个队列是否为空
    def is_empty(self):
        return self._list==[]


    # 返回队列的大小
    def size(self):
        return len(self._list)


if __name__=="__main__":
    q=Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
