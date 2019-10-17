#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/10/17:17:19

# 入栈（压栈）
# 定义栈
class Stack(object):
    def __init__(self):
        self._list=[]
    pass

    # 添加一个新的元素item到栈顶
    def push(self,item):
        self._list.append(item)


    #  弹出栈顶元素
    # pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
    def pop(self):
        return self._list.pop()

    # 返回栈顶元素
    def peek(self):
        if self._list:
            return self._list[-1]
        else:
            return None

    # 判断栈是否为空
    def is_empty(self):
        return self._list==[]


    # 返回栈的元素个数
    def size(self):
        return len(self._list)


if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())