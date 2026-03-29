class Solution:
    def findLatestTime(self, s: str) -> str:
        hh, mm = s.split(":")

        def match(original: str, possible: str) -> bool:
            for a, b in zip(original, possible.zfill(2)):
                if a != "?" and a != b:
                    return False
            return True

        def find_mx(original: str, mx: int) -> str:
            for i in range(mx, -1, -1):
                candidate = str(i).zfill(2)
                if match(original, candidate):
                    return candidate
            return original

        return ":".join((find_mx(hh, 11), find_mx(mm, 59)))
