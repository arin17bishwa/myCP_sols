from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t
        return prev
