class Solution:
    def bestClosingTime(self, customers: str) -> int:
        s = customers
        n: int = len(s)
        total_customers = s.count("Y")
        min_penalty = total_customers
        ans = 0
        curr_customers = s[0] == "Y"

        for i in range(1, n):
            curr_penalty = (i - curr_customers) + (total_customers - curr_customers)
            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                ans = i
            curr_customers += s[i] == "Y"

        return ans if min_penalty <= (n - total_customers) else n


def func():
    obj = Solution()

    s = "YYNY"

    # s = "NNNYNN"

    ans = obj.bestClosingTime(s)

    print(ans)


if __name__ == "__main__":
    func()
