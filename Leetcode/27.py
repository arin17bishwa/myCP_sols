from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = nums
        n = len(arr)

        head, tail = 0, n - 1
        while head <= tail:
            if arr[head] == val:
                arr[tail], arr[head] = arr[head], arr[tail]
                tail -= 1
            else:
                head += 1

        return tail + 1
