class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        arr.sort()
        ans = k
        for ele in arr:
            if ele <= ans:
                ans += 1
        return ans


def main():
    obj = Solution()

    arr = [1, 9, 5, 2]
    k = 6

    ans = obj.findKthSmall(arr, k)

    # print(ans)


if __name__ == "__main__":
    main()
