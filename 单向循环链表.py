#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/10/17:11:09

# 和单向链表的区别就是尾部结点由原来的指向None 变为指向头结点

class Node(object):
    # item 存放数据元素 elem存放下一个结点的位置
    def __init__(self,elem):
        self.elem=elem
        self.next=None

# 定义单向循环链表
class SingleCycleLinkList(object):
    def __init__(self,node=None):
        self._head=node
        if node:
            node.next=node

    # 链表是否为空
    def is_empty(self):
        return self._head==None

    # 链表长度
    def length(self):
        # 判空，因为按照下述方法count从1开始，不能判断链表为空的状态
        if self.is_empty():
            return 0
        # cur 为游标，用于移动遍历结点
        cur=self._head
        # count 用于计数
        count=1
        while cur.next !=self._head:         # 对只有一个结点的情况也适用
            count+=1
            cur=cur.next
        return count

    # 遍历整个链表
    def travel(self):
        if self.is_empty():  # 判断是空链表的情况
            return
        cur=self._head
        while cur.next != self._head:       # 也适用于只有一个结点的情况
            print(cur.elem,end=" ")
            cur=cur.next
        # 退出循环，cur指向尾结点，但是尾节点未打印
        print(cur.elem)

    # 链表头部添加元素 称为头插法
    def add(self,item):
        node=Node(item)    # 要插入结点，所以先把结点构造出来先
        if self.is_empty():
            self._head=node
            node.next=node
        else:
            cur=self._head
            while cur.next != self._head:      # 只有一个结点时也适用
                cur=cur.next
            # 退出循环，此时cur指向尾结点
            node.next=self._head
            self._head=node   # 此处和单链表的区别就是还要把尾结点的next指向新的头结点。这时就需要用到遍历，把尾节点的地址找出来
            # cur.next=node  或
            cur.next=self._head



    # 链表尾部添加元素,称为尾插法
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
            node.next=node
        else:
            cur=self._head
            while cur.next != self._head:    # 只有一个结点时也适用
                cur=cur.next
            node.next=cur.next
            cur.next=node          # 或者 cur.next=node  node.next=self._head

    # 指定位置添加元素   和单链表的一样
    # pos 参数是指链表的下标，从0开始 比如，pos为2时，指的是在第三个位置（0,1,2）2中插入元素，也就是原来2中的元素往后挪了一个位置
    def insert(self,pos, item):
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            pre=self._head
            count=0
            while count<(pos-1):
                count+=1
                pre=pre.next
                # 当循环退出后，pre指向pos-1的位置
            node=Node(item)
            node.next=pre.next
            pre.next=node

    # 删除节点,即删除具体数据
    def remove(self,item):
        # 判空
        if self.is_empty():
            return
        cur=self._head
        pre=None
        while cur.next != self._head:
            if cur.elem==item:
                # 先判断是否是头结点
                if cur==self._head:
                    # 头结点的情况
                    # 找尾节点
                    rear=self._head
                    while rear.next != self._head:
                        rear=rear.next
                    # rear指向尾结点 找到了尾节点
                    self._head=cur.next
                    rear.next=self._head  # 或=cur.next 应该行
                else:
                    # 中间结点的情况
                    pre.next=cur.next  # 删除的数据在尾部的特殊情况也可以处理
                return                  # 为什么是return，不是break
            # 如果没找到相等的，往下移动
            else:
                pre=cur
                cur=cur.next
        # 退出循环 cur指向尾节点
        if cur.elem==item:
            # 如果此尾结点是此链表只有一个结点的情况下
            if cur==self._head:   # 为什么不能是cur.next==self._head
                self._head=None
            else:
                pre.next=self._head   # 这里教程里是=cur.next 都可以



    # 查找节点是否存在
    def search(self,item):
        if self.is_empty():
            return False
        cur=self._head
        while cur.next != self._head:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        # 退出循环，cur指向尾节点
        if cur.elem==item:
            return True
        # 执行完整个循环都没找到相同的元素，则返回False
        return False


if __name__=="__main__":
    ll=SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1,9)
    ll.travel()
    ll.insert(2,100)
    ll.travel()
    ll.insert(10,200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
    ll.search(5)  # ? 为什么没有输出


