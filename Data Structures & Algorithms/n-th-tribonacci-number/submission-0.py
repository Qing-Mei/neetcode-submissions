from functools import cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @cache
        def dfs(i):
            if i <= 1:
                return i
            
            if i == 2:
                return 1
            
            return dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
        
        return dfs(n)
        