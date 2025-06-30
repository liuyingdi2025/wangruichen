from typing import *


class MyCircularQueue:

    def __init__(self, length: int):
        self.values = [-1 for _ in range(length)]
        self.front = 0
        self.rear = length - 1
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.values)

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.rear]

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.values[(self.rear + 1) % len(self.values)] = value
        self.size += 1
        self.rear = (self.rear + 1) % len(self.values)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.values)
        self.size -= 1
        return True


# queue = MyCircularQueue(8)
# print(queue.enQueue(3))  # True
# print(queue.enQueue(9))  # True
# print(queue.enQueue(5))  # True
# print(queue.enQueue(0))  # True
# print(queue.deQueue())  # True
# print(queue.deQueue())  # True
# print(queue.isEmpty())  # False
# print(queue.isEmpty())  # False
# print(queue.Rear())  # 9
# print(queue.Rear())  # 9
# print(queue.deQueue())  # True
