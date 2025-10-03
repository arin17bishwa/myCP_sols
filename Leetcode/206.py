from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        curr: Optional[ListNode] = head
        prev: Optional[ListNode] = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev
