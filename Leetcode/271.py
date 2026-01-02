from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        ans = []
        curr_str = []
        curr_idx = 0
        curr_num = 0
        n = len(s)
        while curr_idx < n:
            while curr_idx < n and s[curr_idx] != "#":
                curr_num = curr_num * 10 + int(s[curr_idx])
                curr_idx += 1
            curr_idx += 1
            for inc in range(curr_num):
                curr_str.append(s[curr_idx + inc])
            curr_idx += curr_num
            ans.append("".join(curr_str))
            curr_str = []
            curr_num = 0
        return ans


def main():
    obj = Solution()

    arr = ["Hello", "World12345"]

    enc = obj.encode(arr)
    print(enc)
    dec = obj.decode(enc)
    print(dec)


if __name__ == "__main__":
    main()
