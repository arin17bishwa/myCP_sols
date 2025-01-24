def iin() -> int:
    return int(input())


def main():
    arr = [input() for _ in range(iin())]
    ans = func(arr)
    print(ans)


def func(arr: list[str]) -> int:
    m, n = len(arr), len(arr[0])
    ans = 0
    if m == 1:
        return ans

    for j in range(n):
        last = arr[0][j]
        for i in range(1, m):
            if arr[i][j] < last:
                ans += 1
                break
    return ans


def rough():
    arr = ["cba", "daf", "ghi"]
    arr = ["abcdef"]
    arr = ["zyx", "wvu", "tsr"]
    ans = func(arr)

    print(ans)


if __name__ == "__main__":
    rough()
