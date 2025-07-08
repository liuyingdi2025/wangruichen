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


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = Heap(category=Heap.MAX_HEAP).add_batch(stones)
        while max_heap.size() > 1:
            weight1 = max_heap.pop()
            weight2 = max_heap.pop()
            differ = abs(weight1 - weight2)
            if differ > 0:
                max_heap.add(differ)
        return max_heap.pop() if max_heap.size() == 1 else 0


print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
