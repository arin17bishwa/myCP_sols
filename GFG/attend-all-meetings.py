class Solution:
    def canAttend(self, arr: list[list[int]]) -> bool:
        arr.sort()
        n = len(arr)
        for i in range(1, n):
            if arr[i - 1][1] > arr[i][0]:
                return False
        return True


def main():
    obj = Solution()

    arr = [[1, 4], [10, 15], [7, 10]]
    arr = [[2, 4], [9, 12], [6, 10]]

    ans = obj.canAttend(arr)

    # print(ans)


if __name__ == "__main__":
    main()
