class Solution:
    def sort012(self, arr: list[int]) -> None:
        n = len(arr)
        head, tail = 0, n - 1
        curr = 0

        while curr <= tail:
            if arr[curr] == 0:
                arr[curr], arr[head] = arr[head], arr[curr]
                curr += 1
                head += 1
            elif arr[curr] == 2:
                arr[curr], arr[tail] = arr[tail], arr[curr]
                tail -= 1
            else:
                curr += 1
