#!/usr/bin/env python3
"""
冒泡排序每一轮都是从左到右比较元素，并进行单向的位置交换。
"""


def bubble_sort_v1(array=[]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def bubble_sort_v2(array=[]):
    for i in range(len(array) - 1):
        # 初始设置为有序的
        is_sorted = True
        for j in range(len(array) - i -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                # 假如有元素替换那就是无序的，还需要接着下一轮冒泡
                is_sorted = False
        if is_sorted:
            break


def bubble_sort_v3(array=[]):
    # 记录最后一次交换的位置
    last_exchange_index = 0
    # 无序数列的边界，每次比较只需比到这里
    sort_border = len(array) - 1
    for i in range(len(array) - 1):
        # 初始设置为有序的
        is_sorted = True
        for j in range(sort_border):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                # 假如有元素替换那就是无序的，还需要接着下一轮冒泡
                is_sorted = False
                # 把无需数列的边界更新为最后一次交换元素的位置
                last_exchange_index = j
        sort_border = last_exchange_index
        if is_sorted:
            break


if __name__ == "__main__":
    my_array1 = list([3, 4, 14, 1, 5, 6, 7, 8, -1, 0, 9, 11])
    bubble_sort_v1(my_array1)
    print(my_array1)
    my_array2 = list([2, 1, 3, 4, 5, 6])
    bubble_sort_v2(my_array2)
    print(my_array2)
    my_array3 = list([3, 4, 2, 1, 5, 6, 7, 8])
    bubble_sort_v3(my_array3)
    print(my_array3)
