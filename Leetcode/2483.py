class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n: int = len(customers)
        arr: list[int] = [int(i == "Y") for i in customers]
        for i in range(1, n):
            arr[i] += arr[i - 1]

        if arr[-1] == 0:
            return 0

        min_penalty = arr[-1]
        ans = 0
        for i in range(1, n + 1):
            curr_penalty = (i - arr[i - 1]) + (arr[-1] - arr[i - 1])
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                ans = i

        return ans


def func():
    obj = Solution()

    s = "YYNY"

    s="NNNYNN"

    ans = obj.bestClosingTime(s)

    print(ans)


if __name__ == "__main__":
    func()
