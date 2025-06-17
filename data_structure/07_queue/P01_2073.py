from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def add_last(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            raise RuntimeError('queue is empty')
        value = self.head.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def remove_last(self):
        if self.head is None:
            raise RuntimeError('queue is empty')
        value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value


class Deque:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def size(self):
        return self.dll.size

    def add_batch(self, values):
        for value in values:
            self.add_last(value)

    def add_first(self, value):
        self.dll.add_first(value)

    def add_last(self, value):
        self.dll.add_last(value)

    def get_first(self):
        return self.dll.head.value

    def get_last(self):
        return self.dll.tail.value

    def remove_first(self):
        return self.dll.remove_first()

    def remove_last(self):
        return self.dll.remove_last()

    def traverse(self):
        current = self.dll.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next
        print('None')


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], index: int) -> int:
        deque = Deque()
        deque.add_batch(tickets)
        time = 0
        while True:
            # print(index, end=':\t')
            # queue.traverse()
            count = deque.remove_first()
            time += 1
            if count > 1:
                deque.add_last(count - 1)
                if index == 0:
                    index = deque.size() - 1
                else:
                    index -= 1
            else:
                if index == 0:
                    return time
                else:
                    index -= 1


print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0))
