from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, ls1: Optional[ListNode], ls2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        pointer = head
        carry = 0
        while ls1 is not None and ls2 is not None:
            value = ls1.val + ls2.val + carry
            carry = 1 if value > 9 else 0
            pointer.next = ListNode(value % 10)
            pointer = pointer.next
            ls1 = ls1.next
            ls2 = ls2.next
        while ls1 is not None:
            value = ls1.val + carry
            carry = 1 if value > 9 else 0
            pointer.next = ListNode(value % 10)
            pointer = pointer.next
            ls1 = ls1.next
        while ls2 is not None:
            value = ls2.val + carry
            carry = 1 if value > 9 else 0
            pointer.next = ListNode(value % 10)
            pointer = pointer.next
            ls2 = ls2.next
        if carry > 0:
            pointer.next = ListNode(carry)
        return head.next
