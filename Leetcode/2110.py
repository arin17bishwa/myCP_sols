from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        arr = prices
        n = len(arr)
        ans = 0
        curr = 1
        for i in range(1, n):
            if arr[i] == arr[i - 1] - 1:
                curr += 1
            else:
                ans += (curr * (curr + 1)) >> 1
                curr = 1

        return ans + ((curr * (curr + 1)) >> 1)


def main():
    obj = Solution()
    arr = [3, 2, 1, 4]
    arr = [8, 6, 7, 7]
    arr = [1]

    ans = obj.getDescentPeriods(arr)

    print(ans)


if __name__ == "__main__":
    main()
