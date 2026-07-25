class Solution:
    def levelSort(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        ans: list[list[int]] = []
        break_point: int = 1
        curr: list[int] = []
        curr_cnt: int = 0

        for i in range(n):
            curr.append(arr[i])
            curr_cnt += 1
            if curr_cnt == break_point:
                ans.append(sorted(curr))
                curr = []
                curr_cnt = 0
                break_point <<= 1

        if curr:
            ans.append(sorted(curr))

        return ans
