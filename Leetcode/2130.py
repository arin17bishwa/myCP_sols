from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        ans: int = 0
        fast = slow = prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        mid = prev.next
        prev.next = None
        h2 = self.reverse(mid)

        h1 = head

        while h1:
            ans = max(ans, h1.val + h2.val)
            h1 = h1.next
            h2 = h2.next

        return ans

    @staticmethod
    def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        curr = head

        while curr:
            t = curr.next
            curr.next = prev
            prev = curr
            curr = t

        return prev
