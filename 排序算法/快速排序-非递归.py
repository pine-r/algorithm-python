#!/usr/bin/env python3
"""
使用非递归实现快速排序
重点：栈
"""


def partition(start_index, end_index, array=None):
    """
    单边循环法：将最左边的元素作为基准元素，从后一个元素开始循环，如果有小于基准元素的，mark右移一位，然后与mark位置的元素交换。
    mark相当于记录了比基准元素小的范围。
    :param start_index: 起始坐标
    :param end_index: 结束坐标
    :param array: 数组
    :return: 返回mark：基准元素最终的位置
    """
    # 单边循环法
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


def quick_sort(start_index, end_index, array=None):
    if array is None:
        array = []
    quick_sort_stack = []
    root_param = {"startIndex": start_index, "endIndex": end_index}
    quick_sort_stack.append(root_param)
    while len(quick_sort_stack) > 0:
        param = quick_sort_stack.pop()
        pivot_index = partition(param.get("startIndex"), param.get("endIndex"), array)
        if param.get("startIndex") < pivot_index - 1:
            left_param = {"startIndex": param.get("startIndex"), "endIndex": pivot_index - 1}
            quick_sort_stack.append(left_param)
        if pivot_index + 1 < param.get("endIndex"):
            right_param = {"startIndex": pivot_index + 1, "endIndex": param.get("endIndex")}
            quick_sort_stack.append(right_param)


if __name__ == "__main__":
    my_array = list([3, 4, 14, 1, 5, 6, 7, 8, -1, 0, 9, 11])
    quick_sort(0, len(my_array) - 1, my_array)
    print(my_array)
