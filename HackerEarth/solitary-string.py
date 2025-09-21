def func(s: str) -> int:
    first_occ: dict[str, int] = {}
    ans = -1
    for idx, ch in enumerate(s):
        if ch in first_occ:
            ans = max(ans, idx - first_occ[ch] - 1)
        else:
            first_occ[ch] = idx
    return ans


def main():
    for _ in range(int(input())):
        print(func(input()))


if __name__ == "__main__":
    main()
