#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: yehaizi time:2019/9/3:8:38

# （1）：

def quick_sort(array,first,last):
    if first>=last:
        return
    mid_value=array[first]
    low=first
    high=last
    while low<high:
        while low<high and array[high]>=mid_value:
            high-=1
        array[low]=array[high]

        while low<high and array[low]<mid_value:
            low+=1
        array[high]=array[low]

    array[low]=mid_value

    quick_sort(array,first,low-1)
    quick_sort(array,low+1,last)

if __name__=='__main__':
    li=[98,13,98,19,20,78,56,78,12]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)


# （2）
def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i])