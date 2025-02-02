from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr = nums

        n = len(arr)
        if n < 3:
            return n
        curr_idx = 2
        pointer = 2

        while pointer < n:
            # print(curr_idx, pointer)
            while pointer < n and arr[pointer] == arr[curr_idx - 2]:
                pointer += 1
            if pointer >= n:
                break

            arr[curr_idx] = arr[pointer]
            curr_idx += 1
            pointer += 1
        return curr_idx


def main():
    obj = Solution()

    arr = [1, 1, 1, 2, 2, 3]

    print(arr)
    ans = obj.removeDuplicates(arr)
    print(arr)


if __name__ == "__main__":
    main()
