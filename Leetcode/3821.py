from math import comb


class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        final_msb = k - 1

        for msb in range(k - 1, 50):
            cnt = comb(msb, k - 1)
            final_msb = msb
            if n > cnt:
                n -= cnt
            else:
                break

        ans = 1 << final_msb
        rem = k - 1

        for bit in reversed(range(final_msb)):
            if rem == 0:
                break

            cnt_zero = comb(bit, rem) if bit >= rem else 0

            if n > cnt_zero:
                n -= cnt_zero
                ans |= 1 << bit
                rem -= 1

        return ans


def main():
    obj = Solution()

    n, k = 4, 2
    # n, k = 3, 1
    # n, k = 7, 3

    ans = obj.nthSmallest(n, k)

    # print(ans)


if __name__ == "__main__":
    main()
