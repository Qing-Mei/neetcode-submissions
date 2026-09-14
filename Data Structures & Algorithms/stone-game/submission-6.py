class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles.copy()
        
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])
            
        return dp[n - 1] > 0
