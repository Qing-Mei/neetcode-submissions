from functools import cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 0
            
            res = 1 + dfs(i + 1)

            for word in dictionary:
                if s.startswith(word, i):
                    res = min(res, dfs(i + len(word)))
            
            return res

        return dfs(0)
