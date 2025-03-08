class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = blocks
        ans = n = len(s)
        tail = 0
        curr_cost = 0
        curr_block = 0

        for head in range(n):
            if s[head] == "W":
                curr_cost += 1

            curr_block += 1

            while tail <= head and curr_block > k:
                if s[tail] == "W":
                    curr_cost -= 1
                curr_block -= 1
                tail += 1
            if curr_block >= k:
                ans = min(ans, curr_cost)
        return ans


def main():
    obj = Solution()

    s = "WBBWWBBWBW"
    k = 7

    ans = obj.minimumRecolors(s, k)

    print(ans)


if __name__ == "__main__":
    main()
