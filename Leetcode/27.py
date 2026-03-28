from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        arr = nums
        n = len(arr)

        head, tail = 0, n - 1
        while head <= tail:
            if arr[head] == val:
                arr[tail], arr[head] = arr[head], arr[tail]
                tail -= 1
            else:
                head += 1

        return tail + 1


def main():
    obj = Solution()

    arr = [3, 2, 2, 3]
    k = 3

    # arr = [0, 1, 2, 2, 3, 0, 4, 2]
    # k = 2

    # arr=[1]
    # k=1

    ans = obj.removeElement(arr, k)

    print(arr[:ans], arr)


if __name__ == "__main__":
    main()
