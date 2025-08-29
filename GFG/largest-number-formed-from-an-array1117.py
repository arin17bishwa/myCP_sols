from functools import cmp_to_key


def comparator(a: str, b: str) -> int:
    return -1 if a + b < b + a else 1


class Solution:

    def findLargest(self, arr: list[int]) -> str:
        return (
            "0"
            if not any(arr)
            else "".join(
                sorted(map(str, arr), reverse=True, key=cmp_to_key(comparator))
            )
        )
