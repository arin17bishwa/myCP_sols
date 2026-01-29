from typing import List


class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        arr = nums
        n = len(arr)
        mapping: dict[int, int] = {}
        negs = []

        for i in range(n):
            if arr[i] >= 0:
                mapping[len(negs)] = i
                negs.append(arr[i])
        m = len(negs)

        if m < 2:
            return arr

        k %= m

        if k:
            negs = negs[k:] + negs[:k]

        for neg_idx, og_idx in mapping.items():
            arr[og_idx] = negs[neg_idx]

        return arr


def main():
    obj = Solution()

    arr = [1, -2, 3, -4]
    k = 3

    # arr = [-3, -2, 7]
    # k = 1

    # arr = [5, 4, -9, 6]
    # k = 2

    ans = obj.rotateElements(arr, k)

    print(ans)


if __name__ == "__main__":
    main()
