from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        
        # time complexity without cache 2 ^ n
        # time ocmplexity with cache i n ^ 3
        # space complexity n ^ 2
        @cache
        def dfs(i, M):
            if n - i <= 2 * M:
                return suffix[i]
            
            best = 0

            for x in range(1, 2 * M + 1):
                best = max(best, suffix[i] - dfs(i + x, max(M, x)))
            
            return best
        
        return dfs(0, 1)

