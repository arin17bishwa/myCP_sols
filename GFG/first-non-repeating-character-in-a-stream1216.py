from collections import deque, defaultdict


class Solution:
    def firstNonRepeating(self, s: str) -> str:
        ans: list[str] = []
        freq: defaultdict[str, int] = defaultdict(int)
        q: deque[str] = deque()
        for ch in s:
            freq[ch] += 1

            if freq[ch] == 1:
                q.append(ch)
            else:
                while q and freq[q[0]] > 1:
                    q.popleft()

            ans.append("#" if not q else q[0])

        return "".join(ans)


def main():
    obj = Solution()

    s = "aabc"
    # s='bb'

    ans = obj.firstNonRepeating(s)

    # print(ans)


if __name__ == "__main__":
    main()
