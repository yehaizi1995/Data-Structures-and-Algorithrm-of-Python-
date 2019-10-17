#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/9/2:15:22

# 定义单链表的结点
# 下一个结点称为后继结点

class Node(object):
    # item 存放数据元素 elem存放下一个结点的位置
    def __init__(self,elem):
        self.elem=elem
        self.next=None

# 定义单链表
class SingleLinkList(object):
    def __init__(self,node=None):
        self._head=node

    # 链表是否为空
    def is_empty(self):
        return self._head==None

    # 链表长度
    def length(self):
        # cur 为游标，用于移动遍历结点
        cur=self._head
        # count 用于计数
        count=0
        while cur != None:
            count+=1
            cur=cur.next
        return count

    # 遍历整个链表
    def travel(self):
        cur=self._head
        while cur != None:
            print(cur.elem,end=" ")
            cur=cur.next
        print("")

    # 链表头部添加元素 称为头插法
    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=node

    # 链表尾部添加元素,称为尾插法
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next != None:    # 个人疑惑：如果写成这样，while cur != None:cur=cur.next cur=node?
                cur=cur.next
            cur.next=node

    # 指定位置添加元素
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
        cur=self._head
        pre=None
        while cur != None:
            if cur.elem==item:
                # 先判断是否是头结点
                # 头结点,(对只有一个结点的特殊情况也可以完成)
                if cur==self._head:
                    self._head=cur.next
                else:
                    pre.next=cur.next  # 删除的数据在尾部的特殊情况也可以处理
                break                  # 找到要删除的元素并删除后即可退出，终止循环
            # 如果没找到相等的，往下移动
            else:
                pre=cur
                cur=cur.next


    # 查找节点是否存在
    def search(self,item):
        cur=self._head
        while cur != None:
            if cur.elem==item:
                return True
            else:
                cur=cur.next
        # 执行完整个循环都没找到相同的元素，则返回False
        return False


if __name__=="__main__":
    ll=SingleLinkList()
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
    ll.search(5)


