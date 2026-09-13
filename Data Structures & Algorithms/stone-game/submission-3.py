from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(i, j):
            if i > j:
                return 0

            return max(piles[i] - dfs(i + 1, j), piles[j] - dfs(i, j - 1))
        
        res = dfs(0, len(piles) - 1)

        if res > 0:
            return True
        else:
            return False
