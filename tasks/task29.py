from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        colors = [0 for _ in range(len(graph))]
        visited = set()

        def nice_dfs(node: List, color: int) -> bool:
            res = True
            colors[node] = color
            if len(graph[node]) == 0:
                return True
            if node in visited:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor in visited:
                    if colors[neighbor] == color:
                        return False
                res = res and nice_dfs(neighbor, -color)
            return res

        for i in range(len(graph)):
            if not nice_dfs(i, 1):
                return False

        return True

