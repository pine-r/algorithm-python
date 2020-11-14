# _*_ coding:utf-8 _*_
"""
功能：实现二叉堆的插入、删除、创建
"""


def up_adjust(array=[]):
    """
    二叉堆的尾节点上浮操作
    :param array: 原数组
    :return:
    """
    child_index = len(array) - 1  # 子节点的取值范围
    parent_index = (child_index - 1) // 2   # 父节点的取值范围
    # temp保存插入的叶子节点值，用于最后的赋值
    temp = array[child_index]
    while child_index > 0 and temp < array[parent_index]:
        array[child_index] = array[parent_index]
        child_index = parent_index  # 子节点上浮
        parent_index = (parent_index - 1) // 2  # 父节点上浮
    array[child_index] = temp


def down_agjust(parent_index, length, array=[]):
    """
    二叉堆的节点下沉操作
    :param parent_index: 待下沉的节点下标
    :param length: 堆的长度范围
    :param array: 原数组
    :return:
    """
    # temp保存父节点值，用于最后的赋值
    temp = array[parent_index]
    child_index = 2 * parent_index + 1
    while child_index < length:
        # 如果有右孩子，且右孩子的值小于左孩子的值,定位到右孩子
        if child_index + 1 < length and array[child_index + 1] < array[child_index]:
            child_index += 1
        # 如果父节点的值小于任何一个孩子的值，直接跳出
        if temp <= array[child_index]:
            break
        # 无需真正的交换，单向赋值即可
        array[parent_index] = array[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    array[parent_index] = temp  # 下沉操作结束，把父节点的值放到最终下沉的位置


def build_heap(array=[]):
    """
    二叉堆的构建操作
    :param array: 原数组
    :return:
    """
    # 从最后一个非叶子节点开始，依次下沉调整
    for i in range((len(array) - 2) // 2, -1, -1):
        down_agjust(i, len(array), array)


if __name__ == "__main__":
    my_array = list([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
    up_adjust(my_array)
    print("尾节点上浮：", my_array)
    my_array = list([7, 1, 3, 10, 5, 2, 8, 9, 6])
    build_heap(my_array)
    print("构建二叉堆：", my_array)
