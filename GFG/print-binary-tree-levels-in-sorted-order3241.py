class Solution:
    def levelSort(self, arr: list[int]) -> list[list[int]]:
        n = len(arr)
        ans: list[list[int]] = []
        idx = 1
        break_point = 1
        curr: list[int] = []
        curr_cnt: int = 0

        for i in range(n):
            curr.append(arr[i])
            curr_cnt += 1
            if curr_cnt == break_point:
                ans.append(sorted(curr))
                curr = []
                curr_cnt = 0
                break_point = break_point << 1

        if curr:
            ans.append(sorted(curr))

        return ans


def main():
    obj = Solution()

    arr = [7, 6, 5, 4, 3, 2, 1]

    ans = obj.levelSort(arr)

    # print(ans)


if __name__ == "__main__":
    main()
