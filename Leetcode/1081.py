from collections import deque


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        bitmask = 0
        ans: deque[str] = deque()
        last_occ = {}
        for idx, ch in enumerate(s):
            last_occ[ch] = idx

        for idx, ch in enumerate(s):
            ch_bitmask = 1 << (ord(ch) - 97)
            if not bitmask & ch_bitmask:
                while ans and ch <= ans[-1] and last_occ[ans[-1]] > idx:
                    popped = ans.pop()
                    bitmask &= ~(1 << (ord(popped) - 97))
                ans.append(ch)
                bitmask |= ch_bitmask
        return "".join(ans)


def main():
    obj = Solution()

    # s = "bcabc"
    s = "cbacdcbc"
    # s = "bcbcbcababa"
    s = "cbaacabcaaccaacababa"

    ans = obj.smallestSubsequence(s)
    print(ans)


if __name__ == "__main__":
    main()
