from collections import defaultdict, deque
from typing import List, Dict, DefaultDict


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        graph: DefaultDict[int, Dict[int, int]] = defaultdict(dict)
        probabilities: List[float] = [0.0] * n
        probabilities[start_node] = 1
        for (a, b), w in zip(edges, succProb):
            graph[a][b] = w
            graph[b][a] = w
        queue = deque([start_node])
        while queue:
            curr = queue.popleft()

            for neighbour, prob in graph[curr].items():
                new_prob = probabilities[curr] * prob
                if new_prob > probabilities[neighbour]:
                    probabilities[neighbour] = new_prob
                    queue.append(neighbour)
        return probabilities[end_node]
