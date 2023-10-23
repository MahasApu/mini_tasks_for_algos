class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        columns = len(s)
        lines = len(p)
        matched = [[False for j in range(lines + 1)] for i in range(columns + 1)]
        matched[0][0] = True

        for line in range(1, lines + 1):
            if p[line - 1] == '*':
                matched[0][line] = matched[0][line - 1]

        for column in range(1, columns + 1):
            for line in range(1, lines + 1):
                if (p[line - 1] == s[column - 1]) or p[line - 1] == '?':
                    matched[column][line] = matched[column - 1][line - 1]
                elif p[line - 1] == '*':
                    match = matched[column][line - 1] or matched[column - 1][line] or matched[column - 1][line - 1]
                    matched[column][line] = match
                else:
                    matched[column][line] = False
        return matched[columns][lines]
