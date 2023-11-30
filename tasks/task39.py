class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matched = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        matched[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                matched[0][j] = matched[0][j - 1]

        for j in range(1, len(s) + 1):
            for i in range(1, len(p) + 1):
                if (p[i - 1] == s[j - 1]) or p[i - 1] == '?':
                    matched[j][i] = matched[j - 1][i - 1]
                elif p[i - 1] == '*':
                    match = matched[j][i - 1] or matched[j - 1][i] or matched[j - 1][i - 1]
                    matched[j][i] = match
                else:
                    matched[j][i] = False
        return matched[len(s)][len(p)]
