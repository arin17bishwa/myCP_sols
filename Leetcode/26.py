from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)
        pointer = 1
        curr_idx = 1

        while pointer < n:
            while pointer < n and arr[pointer] == arr[curr_idx - 1]:
                pointer += 1
            if pointer >= n:
                break
            arr[curr_idx] = arr[pointer]
            pointer += 1
            curr_idx += 1
        return curr_idx
