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

        arr: list[int] = []

        curr = head

        while curr:
            arr.append(curr.val)
            curr = curr.next

        n = len(arr)

        return max(arr[i] + arr[n - 1 - i] for i in range(n // 2 + 1))
