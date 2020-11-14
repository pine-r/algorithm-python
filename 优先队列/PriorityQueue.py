# _*_ coding: utf-8 _*_
__author__ = 'rentingsong'
__date__ = '2020/11/14 11:04'
"""
功能：实现最大优先队列
"""


class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, element):
        self.array.append(element)
        self.size += 1
        self.up_adjust()

    def dequeue(self):
        if self.size < 0:
            raise Exception("队列为空！")
        head = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.down_adjust()
        return head

    def up_adjust(self):
        child_index = self.size - 1  # 子节点的取值范围
        parent_index = (child_index - 1) // 2  # 父节点的取值范围
        # temp保存插入的叶子节点值，用于最后的赋值
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index  # 子节点上浮
            parent_index = (parent_index - 1) // 2  # 父节点上浮
        self.array[child_index] = temp

    def down_adjust(self):
        # temp保存父节点值，用于最后的赋值
        parent_index = 0
        temp = self.array[parent_index]
        child_index = 1
        while child_index < self.size:
            # 如果有右孩子，且右孩子的值小于左孩子的值,定位到右孩子
            if child_index + 1 < self.size and self.array[child_index + 1] > self.array[child_index]:
                child_index += 1
            # 如果父节点的值小于任何一个孩子的值，直接跳出
            if temp >= self.array[child_index]:
                break
            # 无需真正的交换，单向赋值即可
            self.array[parent_index] = self.array[child_index]
            parent_index = child_index
            child_index = 2 * parent_index + 1
        self.array[parent_index] = temp  # 下沉操作结束，把父节点的值放到最终下沉的位置


if __name__ == "__main__":
    queue = PriorityQueue()
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(7)
    print(queue.dequeue())
    print(queue.dequeue())
