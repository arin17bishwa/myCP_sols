import string
from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        arr = list(zip(businessLine, code, isActive))
        allowed_code_chars: str = string.ascii_letters + string.digits + "_"
        allowed_business_lines: list[str] = [
            "electronics",
            "grocery",
            "pharmacy",
            "restaurant",
        ]

        def is_valid_code(s: str) -> int:
            nonlocal allowed_code_chars

            return len(s) != 0 and all(ch in allowed_code_chars for ch in s)

        return [
            i[1]
            for i in sorted(
                filter(
                    lambda x: x[2] == True
                    and is_valid_code(x[1])
                    and x[0] in allowed_business_lines,
                    arr,
                )
            )
        ]


def main():
    obj = Solution()
    code = ["SAVE20", "", "PHARMA5", "SAVE@20"]
    bl = ["restaurant", "grocery", "pharmacy", "restaurant"]
    act = [True, True, True, True]

    ans = obj.validateCoupons(code, bl, act)

    print(ans)


if __name__ == "__main__":
    main()
