from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]) -> List[int]:
            n = len(arr)
            if n < 2:
                return arr
            start = 0
            end = n - 1
            _merge_sort(arr, start, end)

        def _merge_sort(arr: List[int], start: int, end: int):
            if end - start < 1:
                return
            mid = (start + end) >> 1
            h1 = start
            l1 = mid
            h2 = mid + 1
            l2 = end
            _merge_sort(arr, h1, l1)
            _merge_sort(arr, h2, l2)
            merge(arr, h1, l1, h2, l2)

        def merge(arr: List[int], h1: int, l1: int, h2: int, l2: int):
            new_arr = []
            start = h1
            while h1 <= l1 and h2 <= l2:
                if arr[h1] <= arr[h2]:
                    new_arr.append(arr[h1])
                    h1 += 1
                else:
                    new_arr.append(arr[h2])
                    h2 += 1
            while h1 <= l1:
                new_arr.append(arr[h1])
                h1 += 1
            while h2 <= l2:
                new_arr.append(arr[h2])
                h2 += 1
            arr[start : l2 + 1] = new_arr[:]

        merge_sort(nums)
        return nums
