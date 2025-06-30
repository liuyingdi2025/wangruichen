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

    def is_empty(self):
        return self.dll.size == 0

    def enqueue_front(self, value):
        self.dll.add_first(value)
        return self

    def enqueue_rear(self, value):
        self.dll.add_last(value)
        return self

    def enqueue_rear_batch(self, values):
        for value in values:
            self.dll.add_last(value)
        return self

    def dequeue_front(self):
        value = self.dll.head.value
        self.dll.remove_first()
        return value

    def dequeue_rear(self):
        value = self.dll.tail.value
        self.dll.remove_last()
        return value

    def front(self):
        return self.dll.head.value

    def rear(self):
        return self.dll.tail.value

    def traverse(self):
        current = self.dll.head
        while current is not None:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
