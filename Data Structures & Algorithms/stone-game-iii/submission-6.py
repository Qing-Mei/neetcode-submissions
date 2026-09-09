from functools import cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        @cache
        def dfs(i): # how many points curr player higher than other player
            if i == n:
                return 0
            
            best = float("-inf")
            take = 0

            for j in range(i, min(i + 3, n)):
                take += stoneValue[j]
                best = max(best, take - dfs(j + 1)) # how many points other player higher than curr player
            return best
        
        res = dfs(0)

        if res > 0:
            return "Alice"
        if res < 0:
            return "Bob"
        return "Tie"
