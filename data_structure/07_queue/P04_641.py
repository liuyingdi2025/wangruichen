from typing import *


class MyCircularDeque:
    def __init__(self, length: int):
        self.values = [-1 for _ in range(length)]
        self.front = 0
        self.rear = length - 1
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.values)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.values[(self.front - 1 + len(self.values)) % len(self.values)] = value
        self.front = (self.front - 1 + len(self.values)) % len(self.values)
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.values[(self.rear + 1) % len(self.values)] = value
        self.rear = (self.rear + 1) % len(self.values)
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % len(self.values)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + len(self.values)) % len(self.values)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.values[self.rear]
