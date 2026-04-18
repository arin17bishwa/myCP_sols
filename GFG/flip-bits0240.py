class Solution:
    def maxOnes(self, arr: list[int]) -> int:
        n = len(arr)
        kd = [-1 if i == 1 else 1 for i in arr]

        mx = curr = 0
        for i in kd:
            curr += i
            mx = max(mx, curr)
            if curr < 0:
                curr = 0

        return sum(arr) + mx


def main():
    obj = Solution()

    arr = [1, 0, 0, 1, 0]
    # arr = [1, 0, 0, 1, 0, 0, 1]

    ans = obj.maxOnes(arr)

    # print(ans)


if __name__ == "__main__":
    main()
