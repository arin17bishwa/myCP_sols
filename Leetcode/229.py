class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        arr = nums
        n = len(arr)
        candidate1 = candidate2 = -(10**10)
        cnt1 = cnt2 = 0

        for i in arr:
            if cnt1 == 0 and candidate2 != i:
                cnt1 = 1
                candidate1 = i
            elif cnt2 == 0 and candidate1 != i:
                cnt2 = 1
                candidate2 = i
            elif candidate1 == i:
                cnt1 += 1
            elif candidate2 == i:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans: list[int] = []

        for candidate in (candidate1, candidate2):
            if arr.count(candidate) > n // 3:
                ans.append(candidate)

        return ans
