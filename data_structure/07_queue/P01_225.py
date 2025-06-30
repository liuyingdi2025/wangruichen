from typing import *


class Queue:
    def __init__(self):
        self.values = []

    def size(self):
        return len(self.values)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, value):
        self.values.append(value)
        return self

    def dequeue(self):
        value = self.values[0]
        self.values = self.values[1:]
        return value

    def get(self):
        return self.values[0]


class MyStack:
    def __init__(self):
        self.queue = Queue()
        self.queue_tmp = Queue()

    def empty(self) -> bool:
        return self.queue.size() == 0

    def push(self, value: int) -> None:
        """
        stack = [1, 2, 3]
        queue = [3, 2, 1]
        push 0
        queue_tmp = [3, 2, 1]
        queue = [0]
        queue = [3, 2, 1, 0]
        stack = [3, 2, 1, 0]
        （1）queue 中所有元素出队，放入到 queue_tmp 中
        （2）新元素放入 queue
        （3）queue_tmp 所有元素出队，放入 queue 中
        """
        while not self.queue.is_empty():
            self.queue_tmp.enqueue(self.queue.dequeue())
        self.queue.enqueue(value)
        while not self.queue_tmp.is_empty():
            self.queue.enqueue(self.queue_tmp.dequeue())

    def top(self) -> int:
        return self.queue.get()

    def pop(self) -> int:
        return self.queue.dequeue()


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())
