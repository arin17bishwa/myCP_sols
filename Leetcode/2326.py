from typing import Optional, List, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        def is_valid_position(a: int, b: int) -> bool:
            nonlocal m, n, ans
            return 0 <= a < n and 0 <= b < m and ans[b][a] == -1

        def get_next_position(a: int, b: int) -> Tuple[int, int]:
            nonlocal dirs, dir_idx
            dx, dy = dirs[dir_idx]
            new_x, new_y = a + dx, b + dy
            if is_valid_position(new_x, new_y):
                return new_x, new_y
            dir_idx = (dir_idx + 1) % 4
            dx, dy = dirs[dir_idx]
            return a + dx, b + dy

        dirs: List[List[int]] = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        dir_idx = 0
        ans = [[-1] * n for _ in range(m)]
        curr = head
        x, y = -1, 0
        while curr:
            x, y = get_next_position(x, y)
            ans[y][x] = curr.val
            curr = curr.next
        return ans
