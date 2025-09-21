import heapq
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        bit_len = n.bit_length()

        st_max: list[list[int]] = [[0] * bit_len for _ in range(n)]
        st_min: list[list[int]] = [[0] * bit_len for _ in range(n)]

        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]

        for j in range(1, bit_len):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j - 1], st_max[i + (1 << (j - 1))][j - 1])
                st_min[i][j] = min(st_min[i][j - 1], st_min[i + (1 << (j - 1))][j - 1])

        def subarray_value(_l, _r):
            length = _r - _l + 1
            _bit_len = length.bit_length() - 1
            mx = max(st_max[_l][_bit_len], st_max[_r - (1 << _bit_len) + 1][_bit_len])
            mn = min(st_min[_l][_bit_len], st_min[_r - (1 << _bit_len) + 1][_bit_len])
            return mx - mn

        visited: set[tuple[int, int]] = set()

        heap: list[tuple[int, int, int]] = []
        heapq.heappush(heap, (-subarray_value(0, n - 1), 0, n - 1))
        visited.add((0, n - 1))

        cnt = ans = 0
        while cnt < k and heap:
            val, left, right = heapq.heappop(heap)
            ans += -val
            cnt += 1
            if left < right:
                left_sub = (left, right - 1)
                right_sub = (left + 1, right)
                if left_sub not in visited:
                    visited.add(left_sub)
                    heapq.heappush(heap, (-subarray_value(*left_sub), left, right - 1))
                if right_sub not in visited:
                    visited.add(right_sub)
                    heapq.heappush(heap, (-subarray_value(*right_sub), left + 1, right))

        return ans
