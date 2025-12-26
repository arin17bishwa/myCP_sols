class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n: int = len(customers)
        arr: list[int] = [int(i == "Y") for i in customers]
        tot = sum(arr)
        min_penalty = tot
        ans = 0

        for i in range(1, n):
            arr[i] += arr[i - 1]
            curr_penalty = (i - arr[i - 1]) + (tot - arr[i - 1])
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                ans = i

        return ans if min_penalty <= (n - tot) else n


def func():
    obj = Solution()

    s = "YYNY"

    s = "NNNYNN"

    ans = obj.bestClosingTime(s)

    print(ans)


if __name__ == "__main__":
    func()
