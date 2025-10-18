import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        for k, v in freq.items():
            if v - 1 > n - freq[k]:
                return ""

        heap = [[-j, i] for i, j in freq.items()]
        heapq.heapify(heap)

        last = heapq.heappop(heap)
        ans = [last[1]]
        for _ in range(n - 1):
            curr = heapq.heappop(heap)
            if last[0] != -1:
                heapq.heappush(heap, [last[0] + 1, last[1]])
            ans.append(curr[1])
            last = curr

        return "".join(ans)


def main():
    obj = Solution()

    s = "vvvlo"

    ans = obj.reorganizeString(s)

    print(ans)


if __name__ == "__main__":
    main()
