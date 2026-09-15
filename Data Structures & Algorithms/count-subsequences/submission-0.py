from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dfs(i, j):
            if j == n:
                return 1

            if i == m:
                return 0

            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            
            return dfs(i + 1, j)
            
        return dfs(0, 0)
