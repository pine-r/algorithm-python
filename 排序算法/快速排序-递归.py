#!/usr/bin/env python3
"""
快速排序在每一轮挑选一个基准元素，并让其他比它大的元素移动到数列一边，比它小的元素移动到数列的另一边，从而把数列拆解成两个部分。
"""


def quick_sort(start_index, end_index, array=None):
    # 递归结束条件：start_index大等于end_index的时候
    if array is None:
        array = []
    if start_index >= end_index:
        return
    # 得到基准元素的位置
    # pivot_index = partition_v1(start_index, end_index, array)
    pivot_index = partition_v2(start_index, end_index, array)
    # 根据基准元素，分成两部分递归排序
    quick_sort(start_index, pivot_index - 1, array)
    quick_sort(pivot_index + 1, end_index, array)


def partition_v1(star_index, end_index, array=None):
    # 双边循环法
    # 取第一个位置的元素作为基准元素
    if array is None:
        array = []
    pivot = array[star_index]
    left = star_index
    right = end_index
    while left != right:
        # 控制right指针进行比较并左移
        while left < right and array[right] > pivot:
            right -= 1
        # 控制left指针进行比较并右移
        while left < right and array[left] <= pivot:
            left += 1
        # 交换left指针和right指针指向的元素
        if left < right:
            p = array[left]
            array[left] = array[right]
            array[right] = p
    # pivot 和指针重合点交换
    array[star_index] = array[left]
    array[left] = pivot
    return left


def partition_v2(start_index, end_index, array=None):
    # 单边循环法，取第一个位置的元素作为基准元素（也可以选择随机位置）
    if array is None:
        array = []
    pivot = array[start_index]
    mark = start_index
    for i in range(start_index + 1, end_index + 1):
        if array[i] < pivot:
            mark += 1
            p = array[mark]
            array[mark] = array[i]
            array[i] = p
    array[start_index] = array[mark]
    array[mark] = pivot
    return mark


if __name__ == "__main__":
    my_array = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
    quick_sort(0, len(my_array) - 1, my_array)
    print(my_array)
