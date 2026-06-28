class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = nums
        arr.sort()

        return Solution.k_sum(arr, 0, 3)

    @staticmethod
    def two_sum(arr: list[int], target: int, start: int = 0) -> list[list[int]]:
        n = len(arr)
        ans: list[list[int]] = []
        head, tail = start, n - 1

        while head < tail:
            x = arr[head] + arr[tail]
            if x > target or (tail < n - 1 and arr[tail] == arr[tail + 1]):
                tail -= 1
            elif x < target or (head > start and arr[head] == arr[head - 1]):
                head += 1
            else:
                ans.append([arr[head], arr[tail]])
                head += 1
                tail -= 1
        return ans

    @staticmethod
    def k_sum(arr: list[int], target: int, k: int, start: int = 0) -> list[list[int]]:
        if k == 2:
            x = Solution.two_sum(arr, target, start)
            return x

        n = len(arr)
        ans = []

        for curr in range(start, n):
            if curr == start or (arr[curr] != arr[curr - 1]):
                results = Solution.k_sum(arr, target - arr[curr], k - 1, start=curr + 1)

                for res in results:
                    ans.append([arr[curr]] + res)

        return ans
