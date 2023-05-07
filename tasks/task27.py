from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dct = defaultdict(int)
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if not key:
                break
            if not dct.get(key):
                dct[key] = 1
            else:
                dct[key] += 1

        result = list()
        for item in dct:
            if dct[item] > 1:
                result.append(item)
        return result
