class Solution:
    def getSecondLargest(self, arr: list[int]) -> int:
        mx = max(arr)
        ans = -1

        for ele in arr:
            if ele < mx:
                ans = max(ans, ele)
        return ans


def main():
    obj = Solution()

    arr = [10, 5, 10]
    arr = [10, 10, 1]

    ans = obj.getSecondLargest(arr)

    # print(ans)


if __name__ == "__main__":
    main()
