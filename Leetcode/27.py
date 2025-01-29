from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = nums
        n = len(arr)

        curr_idx = pointer = 0
        while pointer < n:
            while pointer < n and arr[pointer] == val:
                pointer += 1
            if pointer >= n:
                break
            arr[curr_idx] = arr[pointer]
            curr_idx += 1
            pointer += 1

        return curr_idx
