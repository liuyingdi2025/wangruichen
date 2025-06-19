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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll = LinkedList(head).add_first(-1)
        for idx in range(0, ll.size(), 2):
            node = ll.get(idx)
            if node is None or node.next is None or node.next.next is None:
                break
            node2 = node.next
            node3 = node2.next
            node4 = node3.next
            node.next = node3
            node3.next = node2
            node2.next = node4
        ll = LinkedList(ll.head.next)
        return ll.head


print(Solution().swapPairs(
    head=LinkedList().add_batch([1, 2, 3]).head
))
