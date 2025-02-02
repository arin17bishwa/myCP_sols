class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        to_maximise = ["NE", "NW", "SE", "SW"]
        complementary_pairs = {"N": "S", "S": "N", "E": "W", "W": "E"}

        def calc_max(to_max: str, mx_changes: int):
            curr_mx = 0
            curr_pos = [0, 0]
            for i in s:
                if complementary_pairs[i] in to_max:
                    if mx_changes:
                        i = complementary_pairs[i]
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

        return max(map(lambda to_max: calc_max(to_max, k), to_maximise))
