from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join((f"#{len(i)}#{i}" for i in strs))

    def decode(self, s: str) -> List[str]:
        ans: list[str] = []
        n = len(s)
        i = str_length = 0
        while i < n:
            if s[i] == "#":
                str_length_digits: list[str] = []
                i += 1
                while s[i] != "#":
                    str_length_digits.append(s[i])
                    i += 1
                str_length: int = int("".join(str_length_digits))
                i += 1
            curr_str: list[str] = []
            j = 0
            while j < str_length:
                curr_str.append(s[i + j])
                j += 1
            i += j
            ans.append("".join(curr_str))
        return ans


def main():
    obj = Solution()

    arr = ["Hello", "World"]
    arr = [""]

    s = obj.encode(arr)
    print(s)
    print(obj.decode(s))


if __name__ == "__main__":
    main()
