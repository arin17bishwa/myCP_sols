from collections import Counter, defaultdict


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def calc_max_dist() -> int:
            pass

        freq = Counter(s)
        mx_dist = defaultdict(int)
        curr_pos = [0, 0]
        for i in s:
            if i == "N":
                curr_pos[1] += 1
            elif i == "S":
                curr_pos[1] -= 1
            elif i == "E":
                curr_pos[0] += 1
            else:
                curr_pos[0] -= 1
        xs = sorted([[freq["E"], "E"], [freq["W"], "W"]])
        ys = sorted([[freq["N"], "E"], [freq["S"], "W"]])
        # if xs[1][0]>=ys[1][0]:
        #     deductible=min(xs[])

        to_maximise = ["NE", "NW", "SE", "SW"]
        comp_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

        def calc_max(to_max: str, mx_changes: int):
            curr_mx = 0
            curr_pos = [0, 0]
            for i in s:
                if comp_pairs[i] in to_max:
                    if mx_changes:
                        i = comp_pairs[i]
                        mx_changes -= 1

                if i == "N":
                    curr_pos[1] += 1
                elif i == "S":
                    curr_pos[1] -= 1
                elif i == "E":
                    curr_pos[0] += 1
                else:
                    curr_pos[0] -= 1
                curr_mx = max(curr_mx, sum(map(abs, curr_pos)))
            return curr_mx

        ans = 0
        for to_mx in to_maximise:
            ans = max(ans, calc_max(to_mx, k))
        return ans
