class Solution:
    def numSteps(self, s: str) -> int:
        arr: list[str] = list(s)
        n = len(arr)
        ans = 0
        while len(arr) > 1:
            ans += 1
            if arr[-1] == "0":
                arr.pop()
            else:
                carry: int = 1
                idx = len(arr) - 1

                while carry and idx >= 0:
                    if arr[idx] == "0":
                        arr[idx] = "1"
                        carry = 0
                    else:
                        arr[idx] = "0"
                    idx -= 1
                if carry:
                    arr = ["1"] + arr
                    carry = 0

        return ans


def main():
    obj = Solution()

    s = "1101"
    s = "10"
    s = "1"

    ans = obj.numSteps(s)

    print(ans)


if __name__ == "__main__":
    main()
