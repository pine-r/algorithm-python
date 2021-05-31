#!/usr/bin/env python3
"""
鸡尾酒排序基于冒泡排序的一种升级排序算法，鸡尾酒排序的元素比较和交换过程是双向的。
排序过程就像钟摆一样，第1轮从左到右，第2轮从右到左，第3轮再从左到右...
适用场景：大部分元素已经有序的情况。
"""


def cock_tail_sort(array=[]):
    for i in range(len(array) // 2):
        # 有序标记，每一轮的初始都是True
        is_sorted = True
        # 奇数轮，从左向右比较和交换
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                # 假如有元素替换那就是无序的，还需要接着下一轮冒泡
                is_sorted = False
        if is_sorted:
            break
        # 偶数轮之前，重新标记为True
        is_sorted = True
        # 偶数轮，从右向左比较和交换
        for j in range(len(array) -i - 1, i, -1):
            if array[j] < array[j - 1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
                # 假如有元素替换那就是无序的，标记为False
                is_sorted = False
        if is_sorted:
            break


if __name__ == "__main__":
    my_array1 = list([3, 4, 14, 2, 3, 6, 9, -45, 8, 0, 15])
    my_array2 = list([1, 2, 3, 4, 5, 6, 7, 0])
    cock_tail_sort(my_array1)
    print(my_array1)
    cock_tail_sort(my_array2)
    print(my_array2)
