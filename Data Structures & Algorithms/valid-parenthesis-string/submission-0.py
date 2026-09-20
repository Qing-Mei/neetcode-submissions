from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @cache
        def dfs(i, balance):
            if balance < 0:
                return False
            
            if i == n:
                return balance == 0
            
            if s[i] == "(":
                return dfs(i + 1, balance + 1)
            
            if s[i] == ")":
                return dfs(i + 1, balance - 1)
            
            if s[i] == "*":
                return dfs(i + 1, balance) or dfs(i + 1, balance + 1) or dfs(i + 1, balance - 1)
        
        return dfs(0, 0)
