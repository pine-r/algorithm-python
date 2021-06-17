#!/usr/bin/env python3
"""
    计数排序适用于一定范围内的整数排序
"""


def count_sort(array=None):
    # 1.得到数列的最大值
    if array is None:
        array = []
    max_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
    # 2.根据数列最大值确定统计数组的长度
    count_array = [0] * (max_value + 1)
    # 3. 遍历数列，填充统计数组
    for i in range(0, len(array)):
        count_array[array[i]] += 1
    # 4.遍历统计数组，输出结果
    sorted_array = []
    for i in range(0, len(count_array)):
        for j in range(0, count_array[i]):
            sorted_array.append(i)
    return sorted_array


if __name__ == "__main__":
    my_array = list([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
    print(count_sort(my_array))
