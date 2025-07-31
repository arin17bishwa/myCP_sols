from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        ans = 0
        curr = head
        while curr:
            ans <<= 1
            if curr.val:
                ans |= 1
            curr = curr.next
        return ans
