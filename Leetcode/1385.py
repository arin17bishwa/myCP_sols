class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)


def main():
    obj = Solution()

    arr1 = [4, 5, 8]
    arr2 = [10, 9, 1, 8]
    d = 2

    ans = obj.findTheDistanceValue(arr1, arr2, d)

    print(ans)


if __name__ == "__main__":
    main()
