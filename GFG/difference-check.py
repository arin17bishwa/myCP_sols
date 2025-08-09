class Solution:
    def minDifference(self, arr: list[str]) -> int:
        n = len(arr)
        time_array = [self.convert_to_secs(i) for i in arr]
        time_array.sort()
        ans = 24 * 3600

        for i in range(1, n):
            ans = min(ans, time_array[i] - time_array[i - 1])
        return min(ans, 24 * 3600 - time_array[-1] + time_array[0])

    @staticmethod
    def convert_to_secs(s: str):
        ans = 0
        for idx, ele in enumerate(s.split(":")[::-1]):
            ans += int(ele) * pow(60, idx)
        return ans
