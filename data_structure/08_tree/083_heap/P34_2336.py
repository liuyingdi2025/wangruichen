from typing import *


class Heap:
    MIN_HEAP = 'MIN_HEAP'  # root <= left and root <= right
    MAX_HEAP = 'MAX_HEAP'  # root >= left and root >= right

    def __init__(self, category):
        self.category = category
        self.values = []

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def contains(self, value):
        return value in self.values

    def peek(self):
        return self.values[0]

    def add(self, value):
        self.values.append(value)
        self._heapify_up(len(self.values) - 1)
        return self

    def add_batch(self, values):
        for value in values:
            self.add(value)
        return self

    def pop(self):
        value = self.values[0]
        self.values[0] = self.values[len(self.values) - 1]
        self.values = self.values[:len(self.values) - 1]
        self._heapify_down(0)
        return value

    def _swap(self, p, q):
        self.values[p], self.values[q] = self.values[q], self.values[p]

    def _heapify_up(self, current):
        if current > 0:
            parent = (current - 1) // 2
            if self.category == self.MIN_HEAP and self.values[current] < self.values[parent]:
                self._swap(current, parent)
                self._heapify_up(parent)
            if self.category == self.MAX_HEAP and self.values[current] > self.values[parent]:
                self._swap(current, parent)
                self._heapify_up(parent)

    def _heapify_down(self, current):
        left, right = 2 * current + 1, 2 * current + 2
        min_child, max_child = None, None
        if left < self.size():
            min_child, max_child = left, left
        if right < self.size():
            if self.values[right] < self.values[min_child]:
                min_child = right
            if self.values[right] > self.values[max_child]:
                max_child = right
        if self.category == self.MIN_HEAP and min_child is not None and self.values[current] > self.values[min_child]:
            self._swap(current, min_child)
            self._heapify_down(min_child)
        if self.category == self.MAX_HEAP and max_child is not None and self.values[current] < self.values[max_child]:
            self._swap(current, max_child)
            self._heapify_down(max_child)


class SmallestInfiniteSet:
    def __init__(self):
        self.min_heap = Heap(Heap.MIN_HEAP).add_batch([_ for _ in range(1, 2001)])

    def popSmallest(self) -> int:
        return self.min_heap.pop()

    def addBack(self, num: int) -> None:
        if not self.min_heap.contains(num):
            self.min_heap.add(num)
