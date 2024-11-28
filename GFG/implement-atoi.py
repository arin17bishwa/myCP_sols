class Solution:
    def myAtoi(self, s: str):
        unsigned_ans: int = 0
        sign: int = 1
        max_int: int = (1 << 31) - 1
        min_int: int = -(1 << 31)
        digit_seen: bool = False
        for ch in s.lstrip():
            if ch == " ":
                continue

            if ch == "-":
                if not digit_seen:
                    sign = -1
                    continue
                else:
                    break

            if ch == "+":
                if not digit_seen:
                    sign = 1
                else:
                    break

            if not ch.isdigit():
                break

            unsigned_ans = unsigned_ans * 10 + int(ch)
            digit_seen = True
            signed_ans = sign * unsigned_ans
            if signed_ans > max_int:
                return max_int
            if signed_ans < min_int:
                return min_int
        return sign * unsigned_ans


def main():
    obj = Solution()
    s: str = " 325-"

    ans = obj.myAtoi(s)
    print(ans)


if __name__ == "__main__":
    main()
