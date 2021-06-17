#!/usr/bin/env python3
"""
    桶排序：每个桶代表一个区间范围，里面可以承载一个或多个元素
    时间复杂度： O(n)
    空间复杂度： O(n)
"""


def bucket_sort(array=None):
    if array is None:
        array = []
    # 1.得到数列的最大值和最小值，并算出差值d
    max_value = array[0]
    min_value = array[0]
    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    d = max_value - min_value
    # 2.初始化桶
    bucket_num = len(array)
    bucket_list = []
    for i in range(0, bucket_num):
        bucket_list.append([])
    # 3.遍历原始数组，将每个元素放入桶中
    for i in range(0, len(array)):
        num = int((array[i] - min_value) * (bucket_num - 1) / d)
        bucket = bucket_list[num]
        bucket.append(array[i])
    # 4.对每个桶内部进行排序
    for i in range(0, len(bucket_list)):
        # list采用了归并排序或归并的优化版本
        bucket_list[i].sort()
    # 5.输出全部元素
    sorted_array = []
    for sub_list in bucket_list:
        for element in sub_list:
            sorted_array.append(element)
    return sorted_array


if __name__ == "__main__":
    my_array = list([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
    print(bucket_sort(my_array))
