from itertools import groupby


class Solution:
    def findPattern(self, s: str) -> bool:
        freq = [(ch, len(tuple(it))) for ch, it in groupby(s)]
        if len(freq) & 1 or (freq and freq[-1][0] != 'y'):
            return False
        n = len(freq)
        for i in range(0, n - 1, 2):
            if not ((freq[i][0] == 'x' and freq[i + 1][0] == 'y') and (freq[i][1] == freq[i + 1][1])):
                return False
        return True


def main():
    obj = Solution()

    s = 'xxxyyyxy'
    s='xxxyyyx'

    ans = obj.findPattern(s)

    print(ans)


if __name__ == '__main__':
    main()
