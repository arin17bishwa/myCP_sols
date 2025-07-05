from collections import defaultdict


def two_sum(arr: list[int], target: int) -> list[int]:
    indices = defaultdict(list)
    for idx, val in enumerate(arr):
        indices[val].append(idx)
    for i in arr:
        if target != (i << 1):
            if indices[target - i]:
                return [indices[i][0], indices[target - i][0]]
        else:
            if len(indices[target - i]) > 1:
                return indices[target - i][:2]

    return []


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(arr, target)
    print(" ".join(map(str, res)))
