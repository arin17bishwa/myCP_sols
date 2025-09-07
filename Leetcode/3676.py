from typing import List


class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        arr = nums
        n = len(arr)

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(n):
            if left[i] != -1 and right[i] != n:
                ans += 1
        return ans
