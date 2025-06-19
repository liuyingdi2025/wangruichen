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
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def add_first(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self

    def add_batch(self, nums):
        if self.head is None:
            self.add_first(nums[0])
            return self.add_batch(nums[1:])
        current = self.head
        while current.next is not None:
            current = current.next
        for num in nums:
            node = ListNode(num)
            current.next = node
            current = current.next
        return self

    def get(self, index):
        if self.head is None or index >= self.size():
            raise IndexError('linked list index out of range')
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.val, end=' -> ')
            current = current.next
        print('None')


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ll = LinkedList(head)
        # ll.traverse()
        if ll.size() == k:
            ll.head = ll.head.next
        else:
            prev_node = ll.get(ll.size() - k - 1)
            prev_node.next = prev_node.next.next
        # ll.traverse()
        return ll.head