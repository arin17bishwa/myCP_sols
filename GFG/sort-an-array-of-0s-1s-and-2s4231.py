from collections import Counter


class Solution:
    def sort012(self, arr: list[int]) -> None:
        freq = Counter(arr)
        arr[: freq[0]] = [0] * freq[0]
        arr[freq[0] : freq[0] + freq[1]] = [1] * freq[1]
        arr[freq[0] + freq[1] :] = [2] * freq[2]


def main():
    obj = Solution()

    arr = [0, 1, 1]

    obj.sort012(arr)

    # print(arr)


if __name__ == "__main__":
    main()
