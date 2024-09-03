class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str: str = "".join(map(str, (ord(i) - 96 for i in s)))
        return int(transform(num_str, k))


def transform(s: str, k: int) -> str:
    if k < 1 or len(s) == 1:
        return s
    return transform(str(sum(map(int, s))), k - 1)
