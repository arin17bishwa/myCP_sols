class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        arr = nums
        ans: list[int] = []
        curr_cnt = 0
        prev_num = -1
        for i in arr:
            if i != prev_num:
                curr_cnt = 1
                prev_num = i
            else:
                curr_cnt += 1
            if curr_cnt <= k:
                ans.append(i)

        return ans
