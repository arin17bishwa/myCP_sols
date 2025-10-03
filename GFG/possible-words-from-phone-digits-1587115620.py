class Solution:
    def possibleWords(self, arr: list[int]):
        mapping: dict[int, str] = {
            0: "",
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        ans: list[str] = []
        n = len(arr)

        def func(idx: int, curr: list[str]):
            if idx == n:
                ans.append("".join(curr))
                return

            if mapping[arr[idx]]:
                for ch in mapping[arr[idx]]:
                    curr.append(ch)
                    func(idx + 1, curr)
                    curr.pop()
            else:
                func(idx+1, curr)

        func(0, [])

        return ans


def main():
    obj = Solution()

    arr = [2, 3]
    arr = [2]
    arr=[8,8,1]

    ans = obj.possibleWords(arr)

    # print(sorted(ans))


if __name__ == "__main__":
    main()
