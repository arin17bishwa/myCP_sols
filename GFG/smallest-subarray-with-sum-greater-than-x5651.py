class Solution:
    def smallestSubWithSum(self, arr: list[int], x: int):
        n = len(arr)
        ans = n + 1
        tail = curr = 0
        for head in range(n):
            curr += arr[head]
            while tail <= head and curr > x:
                ans = min(ans, head - tail + 1)
                curr -= arr[tail]
                tail += 1

        return 0 if ans == n + 1 else ans


def main():
    obj = Solution()

    arr = [1, 4, 45, 6, 0, 19]
    x = 51

    arr = [1, 10, 5, 2, 7]
    x = 100

    ans = obj.smallestSubWithSum(arr, x)

    print(ans)


if __name__ == "__main__":
    main()
