class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def size(self):
        count = 0
        pointer = self.head
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

    def get_node(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("linked list index out of range")
        pointer = self.head
        for idx in range(index):
            pointer = pointer.next
        return pointer

    def get_value(self, index):
        return self.get_node(index).value

    def add_first(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return self

    def add_first_batch(self, values):
        values = values[::-1]
        for value in values:
            self.add_first(value)
        return self

    def add_last(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return self

    def add_last_batch(self, values):
        for value in values:
            self.add_last(value)
        return self

    def traverse(self):
        if self.head is None:
            print('None')
        else:
            print('None', end=' <-> ')
            pointer = self.head
            while pointer is not None:
                print(pointer.value, end=' <-> ')
                pointer = pointer.next
            print('None')
