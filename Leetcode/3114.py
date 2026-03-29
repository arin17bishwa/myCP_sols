class Solution:
    def findLatestTime(self, s: str) -> str:
        hh, mm = s.split(":")

        def match(original: str, possible: int) -> bool:
            for a, b in zip(original, str(possible).zfill(2)):
                if a != "?" and a != b:
                    return False
            return True

        final_hh = "00"
        for i in range(11, -1, -1):
            if match(hh, i):
                final_hh = str(i).zfill(2)
                break

        final_mm = "00"
        for i in range(59, -1, -1):
            if match(mm, i):
                final_mm = str(i).zfill(2)
                break

        return ":".join((final_hh, final_mm))
