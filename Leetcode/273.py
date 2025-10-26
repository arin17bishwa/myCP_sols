class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        s = str(num)
        return self.helper(s).strip()

    def router(self, s: str) -> str:
        if len(s) < 2:
            return self.spell_1(s)
        elif len(s) < 3:
            return self.spell_2(s)

        return self.spell_3(s)

    def helper(self, s: str) -> str:
        sub_parts: list[str] = []
        spell_mapping: dict[int, str] = {
            0: "",
            1: "thousand",
            2: "million",
            3: "billion",
            4: "trillion",
        }
        n = len(s)
        s = s[::-1]
        for i in range(0, n, 3):
            sub_part = self.router(s[i : i + 3][::-1])
            if sub_part:
                sub_parts.append(sub_part + " " + spell_mapping[i // 3].title())

        return " ".join(sub_parts[::-1])

    def spell_3(self, s: str) -> str:
        if s == "000":
            return ""
        hundred_num = self.spell_1(s[0])

        if not hundred_num:
            return self.spell_2(s[1:])
        return (self.spell_1(s[0]) + " Hundred " + self.spell_2(s[1:])).strip()

    def spell_2(self, s: str) -> str:
        if s == "00":
            return ""
        if s[0] == "0":
            return self.spell_1(s[1])

        special_spell_map: dict[str, str] = {
            "10": "ten",
            "11": "eleven",
            "12": "twelve",
            "13": "thirteen",
            "14": "fourteen",
            "15": "fifteen",
            "16": "sixteen",
            "17": "seventeen",
            "18": "eighteen",
            "19": "nineteen",
        }

        if s in special_spell_map:
            return special_spell_map[s].title()

        spell_map: dict[str, str] = {
            "2": "twenty",
            "3": "thirty",
            "4": "forty",
            "5": "fifty",
            "6": "sixty",
            "7": "seventy",
            "8": "eighty",
            "9": "ninety",
        }

        return " ".join([spell_map[s[0]].title(), self.spell_1(s[1])]).strip()

    @staticmethod
    def spell_1(s: str) -> str:
        spell_map = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "0": "",
        }

        return spell_map[s].title()


def main():
    obj = Solution()
    n = 1234919
    n = 1234567
    n = 1000000

    ans = obj.numberToWords(n)

    print(ans)


if __name__ == "__main__":
    main()
