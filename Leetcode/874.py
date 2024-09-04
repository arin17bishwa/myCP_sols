from typing import List, Set, Tuple, Optional


class Solution:
    @staticmethod
    def calculate_distance(p1: List[int], p2: Optional = None) -> int:
        if p2 is None:
            p2 = [0, 0]
        return pow(abs(p1[0] - p2[0]), 2) + pow(abs(p1[1] - p2[1]), 2)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_set: Set[Tuple[int, int]] = set(map(tuple, obstacles))
        step_sizes: List[List[int]] = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr_pos = [0, 0]
        step_idx = 0
        ans = 0
        skip = True
        for command in commands:
            if command == -2:
                step_idx = (step_idx - 1) % 4
            elif command == -1:
                step_idx = (step_idx + 1) % 4
            else:
                for _ in range(command):
                    dx, dy = step_sizes[step_idx]
                    new_pos = [curr_pos[0] + dx, curr_pos[1] + dy]
                    if tuple(new_pos) in obs_set:
                        ans = max(ans, self.calculate_distance(curr_pos))
                        break
                    else:
                        curr_pos = new_pos[:]
                ans = max(ans, self.calculate_distance(curr_pos))
        return ans
