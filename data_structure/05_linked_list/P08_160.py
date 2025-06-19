from typing import *


class ListNode:
    def __init__(self, val, next=None):
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

    def merge(self, ll):
        if self.head is None:
            return ll
        if ll.head is None:
            return self
        ans = LinkedList().add_first(-1)
        pointer1 = self.head
        pointer2 = ll.head
        pointer3 = ans.head
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val <= pointer2.val:
                pointer3.next = pointer1
                pointer1 = pointer1.next
            else:
                pointer3.next = pointer2
                pointer2 = pointer2.next
            pointer3 = pointer3.next
            pointer3.next = None
        while pointer1 is not None:
            pointer3.next = pointer1
            pointer3 = pointer3.next
            pointer1 = pointer1.next
        while pointer2 is not None:
            pointer3.next = pointer2
            pointer3 = pointer3.next
            pointer2 = pointer2.next
        ans.head = ans.head.next
        return ans

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.val, end=' -> ')
            current = current.next
        print('None')


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myset = set()
        pointerA = headA
        while pointerA is not None:
            myset.add(pointerA)
            pointerA = pointerA.next
        pointerB = headB
        while pointerB is not None:
            if pointerB in myset:
                return pointerB
            pointerB = pointerB.next
        return None


print(Solution().getIntersectionNode(
    LinkedList().add_batch([4, 1, 8, 4, 5]).head,
    LinkedList().add_batch([5, 6, 1, 8, 4, 5]).head

))
