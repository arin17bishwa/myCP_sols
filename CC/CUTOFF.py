from typing import Iterable, Callable


def int_arr() -> Iterable[int]:
    return map(int, input().split())


def iin() -> int:
    return int(input())


def yn_dec(function) -> Callable:
    letter_case: str = "upper"

    def inner1(*args, **kwargs) -> str:
        res = function(*args, **kwargs)
        ans = "yes" if res else "no"
        if letter_case == "upper":
            return ans.upper()
        if letter_case == "title":
            return ans.title()
        if letter_case == "lower":
            return ans.lower()
        return res

    return inner1


def func():
    n, x = int_arr()
    arr = sorted(int_arr(), reverse=True)
    return arr[x - 1] - 1


def main():
    for _ in range(iin()):
        print(func())


if __name__ == "__main__":
    main()
