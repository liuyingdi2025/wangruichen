from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

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
        return self.get_node(index).val

    def index(self, node):
        pointer = self.head
        count = 0
        while pointer is not None:
            if pointer == node:
                return count
            pointer = pointer.next
        return -1

    def add_first(self, value):
        node = ListNode(value)
        node.next = self.head
        self.head = node
        return self

    def add_first_batch(self, values):
        values = values[::-1]
        for value in values:
            self.add_first(value)
        return self

    def add_last(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = node
        return self

    def add_last_batch(self, values):
        if len(values) == 0:
            return self
        if self.head is None:
            self.head = ListNode(values[0])
            pointer = self.head
            for idx in range(1, len(values)):
                value = values[idx]
                pointer.next = ListNode(value)
                pointer = pointer.next
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            for value in values:
                pointer.next = ListNode(value)
                pointer = pointer.next
        return self

    def remove_first(self):
        if self.head is None:
            raise RuntimeError("linked list is empty")
        item = self.head.val
        self.head = self.head.next
        return item

    def traverse(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.val, end=' -> ')
            pointer = pointer.next
        print('None')


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ll = LinkedList(head)
        if ll.head is None or ll.head.next is None:
            return False
        slow, fast = ll.head, ll.head.next.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
