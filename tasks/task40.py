from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        weights = [[float("inf") for from_ in range(n)] for to_ in range(n)]

        for from_, to_, weight in edges:
            weights[from_][to_] = weight
            weights[to_][from_] = weight

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    weights[j][k] = min(weights[j][i] + weights[i][k], weights[j][k])

        city_index = 0
        min_amount = float("inf")

        for i in range(n):
            counter = 0
            for j in range(n):
                counter += i != j and weights[i][j] <= distanceThreshold
            if counter <= min_amount:
                city_index = max(i, city_index)
                min_amount = counter

        return city_index