from collections import defaultdict
from typing import List, Dict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colorings = defaultdict(set)
        ball_color_mapping: Dict[int, int] = {}
        ans: List[int] = []
        for ball, color in queries:
            if ball in ball_color_mapping:
                current_color = ball_color_mapping[ball]
                colorings[current_color].remove(ball)
                if not colorings[current_color]:
                    del colorings[current_color]
            colorings[color].add(ball)
            ball_color_mapping[ball] = color
            ans.append(len(colorings))
        return ans
