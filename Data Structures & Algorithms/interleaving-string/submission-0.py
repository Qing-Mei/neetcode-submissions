from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        @cache
        def dfs(i, j):
            k = i + j

            if k == len(s3):
                return True
            
            if i < m and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    return True
            
            if j < n and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    return True
            
            return False
            
        return dfs(0, 0)
