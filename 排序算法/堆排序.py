#!/usr/bin/env python3
"""
堆排序：
1、把无序数组构建成二叉堆
2、循环删除堆顶元素，并将该元素移到集合尾部，调正堆产生新的堆顶
"""


def down_adjust(parent_index, length, array=None):
    if array is None:
        array = []
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        if child_index + 1 < length and array[child_index + 1] > array[child_index]:
            child_index += 1
        if temp >= array[child_index]:
            break
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * child_index + 1
    array[parent_index] = temp


def heap_sort(array=None):
    if array is None:
        array = []
    # 1.把无序数组构建成最大堆
    for i in range((len(array)-2)//2, -1, -1):
        down_adjust(i, len(array), array)
    # 2.循环交换集合尾部元素到堆顶，并调节堆产生新的堆顶
    for i in range(len(array) - 1, 0, -1):
        temp = array[i]
        array[i] = array[0]
        array[0] = temp
        down_adjust(0, i, array)


if __name__ == "__main__":
    my_array = list([3, 4, 14, 1, 5, 6, 7, 8, -1, 0, 9, 11])
    heap_sort(my_array)
    print(my_array)
