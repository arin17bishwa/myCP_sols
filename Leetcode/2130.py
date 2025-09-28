from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        prev = slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        mid = self.reverse_ll(slow)
        h1, h2 = head, mid
        ans = 0
        while h1 and h2:
            ans = max(h1.val + h2.val, ans)
            h1 = h1.next
            h2 = h2.next
        return ans

    @staticmethod
    def reverse_ll(head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next, prev = prev, curr
            curr = temp
        return prev
