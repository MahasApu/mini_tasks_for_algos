from typing import List

class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        grid_counter = [[-1 for i in range(n)] for j in range(m)]

        def find_path(line, column):

            if line >= m or column >= n:
                return float('inf')

            curr_hp = grid_counter[line][column]
            dmg = dungeon[line][column]

            if line == m - 1 and column == n - 1:
                return 1 if dmg >= 0 else 1 - dmg

            if curr_hp != -1:
                return curr_hp

            dmg_down = max(1, find_path(line + 1, column) - dmg)
            dmg_right = max(1, find_path(line, column + 1) - dmg)
            grid_counter[line][column] = min(dmg_down, dmg_right)

            return grid_counter[line][column]

        return find_path(0, 0)
