from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        self.max_cycle_length = -1

    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        for start in range(len(edges)):
            if start not in visited:
                dist_from_start = defaultdict(int)
                dist_from_start[start] = 1
                self.dfs(edges, start, visited, dist_from_start)

        return self.max_cycle_length

    def dfs(self, edges: List[int], node: int, visited: set, dist_from_start: dict):
        visited.add(node)
        adj_node = edges[node]
        if adj_node == -1:
            return

        if adj_node not in visited:
            dist_from_start[adj_node] = dist_from_start[node] + 1
            self.dfs(edges, adj_node, visited, dist_from_start)

        # if node has already been visited - there's prospective max cycle length
        elif adj_node in dist_from_start:
            self.max_cycle_length = max(self.max_cycle_length, dist_from_start[node] - dist_from_start[adj_node] + 1)