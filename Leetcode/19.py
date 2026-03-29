from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        fast = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            curr = curr.next

        t = curr.next
        curr.next = t.next

        return dummy.next
