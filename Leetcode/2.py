from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentry: ListNode = ListNode()
        curr = sentry
        h1, h2 = l1, l2
        carry: int = 0
        while h1 and h2:
            sm = h1.val + h2.val + carry
            curr.next = ListNode(sm % 10)
            carry = sm // 10
            curr = curr.next
            h1 = h1.next
            h2 = h2.next
        if h1:
            remaining = h1
        elif h2:
            remaining = h2
        else:
            remaining = None

        while remaining:
            sm = remaining.val + carry
            curr.next = ListNode(sm % 10)
            carry = sm // 10
            curr = curr.next
            remaining = remaining.next

        if carry:
            curr.next = ListNode(carry)

        return sentry.next
