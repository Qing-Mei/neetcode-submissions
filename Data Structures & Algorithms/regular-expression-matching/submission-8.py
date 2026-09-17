from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @cache
        def dfs(i, j):
            if j == n:
                return i == m
            
            match = i < m and (s[i] == p[j] or p[j] == ".")

            if j + 1 < n and p[j + 1] == "*":
                return dfs(i, j + 2) or match and dfs(i + 1, j)

            return match and dfs(i + 1, j + 1)
                    
        return dfs(0, 0)
